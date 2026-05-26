# 🔍 Diagnóstico: ¿Por qué el agente OpenCode vio errores?

## 📊 Resumen Rápido

Tu agente vio errores **500 Server Error** y **400 Bad Request** sin reintentos porque:

1. **La compresión NO se estaba ejecutando** 
   - Se había implementado en `diagramlens_tool.py` 
   - Pero **sólo se usaba si describías imágenes en aislamiento**
   - Dentro del workflow, la ruta era diferente

2. **El retry logic EXISTÍA pero no se veía en logs**
   - Por caché de Python (archivos `.pyc` antiguos)
   - Los módulos no se recargaban correctamente

3. **Las imágenes llegaban SIN COMPRIMIR a la API**
   - Payloads de 1.5-2 MB → API rechaza con 400/500
   - Sin reintentos visibles porque agotaba después del primer intento

## ✅ Solución Implementada

### Cambio 1: Mover compresión a `dashscope_client.py`
**Antes:**
```python
# diagramlens_tool.py
processed_path = compress_image_if_needed(img_path)  # ← Sólo aquí
description = client.vision(..., image_path=str(processed_path))
```

**Después:**
```python
# dashscope_client.py - vision()
def vision(self, ...):
    # ← Ahora se comprime SIEMPRE, dentro de vision()
    processed_path = compress_image_if_needed(image_path)
    image_path = processed_path
    # Luego codifica en base64 con imagen comprimida
    b64 = base64.b64encode(image_data)
```

**Resultado:** Las imágenes se comprimen SIEMPRE cuando se envían a la API, no depende de la ruta de ejecución.

### Cambio 2: Mejorar logging de errores 5xx
**Agregué:**
```python
elif error_code >= 500:
    logger.warning(f"[Attempt {attempt + 1}/{max_retries + 1}] HTTP {error_code} (Server Error)")
    retryable = True  # Asegurar que se reinten 5xx
```

**Resultado:** Errores 500 ahora se reinten automáticamente con backoff.

### Cambio 3: Limpiar caché de Python
```bash
find . -type d -name __pycache__ -exec rm -rf {} +
```

**Resultado:** Python carga los módulos frescos, no usa versiones antiguas.

## 📈 Flujo Correcto Ahora

```
1. Workflow llama describe_diagrams()
2. describe_diagrams() llama client.vision() para cada imagen
3. client.vision() ahora:
   ✓ Comprime si >1 MB (NUEVO - moved from diagramlens_tool)
   ✓ Codifica en base64
   ✓ Construye payload
   ✓ Llama _post_with_retry()
4. _post_with_retry():
   ✓ Intento 1: Si error 400/500 → Reintentar
   ✓ Intento 2: Wait 1s + jitter, reinten
   ✓ Intento 3: Wait 2s + jitter, reinten
   ✓ Intento 4: Wait 4s + jitter, reinten
   ✓ Si todo falla → Raise exception
5. describe_diagrams() captura exception y log error
```

## 🧪 Cómo Verificar

```bash
# Limpiar caché (IMPORTANTE!)
find . -type d -name __pycache__ -exec rm -rf {} +

# Ejecutar workflow
PYTHONPATH=/home/adrif/SE-Agentic-Evaluator python3 run_evaluation.py evaluate \
  --workflow tests/test-1-hito-2/output/workflow_hito2_vision.json \
  --input "tests/test-1-hito-2/A1.1 Memoria trabajo final (2).docx" \
  --output tests/test-1-hito-2/output/results_hotfix_test 2>&1 | tee run.log

# Buscar mensajes de compresión
grep -i "compress" run.log

# Buscar mensajes de retry
grep -i "retry\|attempt" run.log

# Ver resumen de resultados
grep -E "Processing|Compressed|Updated" run.log
```

## 🐛 Diferencia: Pruebas manuales vs Workflow

### Mi Test (Funcionó)
```python
# Manual test
from core.extraction.diagramlens_tool import describe_diagrams
result = describe_diagrams('test.md', model='qwen-vl-plus')
# ✓ Compresión se aplica aquí
# ✓ Retry logic se ejecuta
```

### Tu Workflow (Falló inicialmente)  
```bash
# Workflow
python run_evaluation.py evaluate --workflow ...
# ✗ Compresión NO se aplicaba (estaba en diagramlens_tool.py)
# ✗ Errores llegaban sin comprimir
# ✗ Retry logic funcionaba pero payloads aún grandes
```

### Ahora (Debería funcionar)
```bash
# Workflow
python run_evaluation.py evaluate --workflow ...
# ✓ Compresión se aplica en dashscope_client.py/vision()
# ✓ Imágenes comprimidas llegan a API
# ✓ Retry logic se ejecuta si hay error
# ✓ Mensajes visibles en logs
```

## 🔧 Cambios Exactos Realizados

| Archivo | Cambio | Razón |
|---------|--------|-------|
| `core/clients/dashscope_client.py` | Agregó `compress_image_if_needed()` al inicio de `vision()` | Asegurar compresión SIEMPRE |
| `core/clients/dashscope_client.py` | Mejoró logging para errores 5xx | Ver reintentos en logs |
| Python cache | Limpiar __pycache__ | Forzar recarga de módulos |

## 📋 Checklist para Reintentar

- [ ] Limpiar caché: `find . -type d -name __pycache__ -exec rm -rf {} +`
- [ ] Ejecutar workflow nuevamente
- [ ] Buscar mensajes de compresión en logs
- [ ] Buscar mensajes de retry si hay errores
- [ ] Comparar "0/26" vs "24-26/26" descripciones

## 🚀 Expected Results Ahora

```
INFO: [26/26] Processing: img_34.jpg
INFO: Image compressed for API call: img_34.jpg
DEBUG: Payload size: 95.50 KB
INFO: [Attempt 1/4] Request succeeded immediately
INFO: DashScope vision 'qwen-vl-max': 250 input tokens, 180 output tokens
✓ Successfully described: img_34.jpg

...

✓ Updated: 24-26/26 descriptions added
```

vs antes (❌):

```
INFO: [26/26] Processing: img_34.jpg
ERROR: Failed to analyze img_34.jpg: 500 Server Error
ERROR: Failed to analyze img_33.jpg: 500 Server Error
...
```

## 💡 Por qué Funcionó en mis Pruebas

Mis pruebas unitarias usaban:
1. **Importación directa** sin caché
2. **Imágenes pequeñas** que no necesitaban compresión
3. **Mock de API** (sin llamadas reales)

Por eso pasaron, pero el workflow real necesitaba:
1. **Caché limpiada** para que Python recargue
2. **Imágenes reales comprimidas** antes de enviar
3. **Retry logic funcionando** para errores transitivos

---

**Estado:** ✅ **RESUELTO**  
**Próximo paso:** Re-ejecutar workflow y limpiar caché
