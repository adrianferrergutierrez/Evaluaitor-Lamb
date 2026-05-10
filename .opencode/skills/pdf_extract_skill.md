# pdf_extract_skill

## Role

Convierte un PDF a Markdown estructurado con imágenes extraídas. Úsala cuando el input sea un PDF.

## Tools

| # | Herramienta | Qué hace |
|---|-------------|----------|
| 1 | PyMuPDF | Extrae texto e imágenes del PDF |

## Uso

```
/pdf_extract input=<ruta_al_pdf> output=<directorio_salida>
```

### Ejemplo

```
/pdf_extract input=/path/to/memoria.pdf output=/tmp/phase0_extract
```

## Proceso

1. Verificar que el PDF existe
2. Ejecutar extracción con PyMuPDF
3. Validar que `contents.md` tiene >500 caracteres
4. Contar imágenes en `img/`
5. Leer primeras 50 líneas para verificar calidad

## Manejo de errores

- **PyMuPDF no instalado**: `pip install pymupdf`
- **PDF corrupto/encriptado**: verificar integridad del fichero
- **Disco lleno**: verificar con `df -h`
- **PDF escanejado**: necesita OCR (DeepSeekOCR-MLX)

## Output

- `<output>/contents.md` — Markdown con referencias a imágenes
- `<output>/img/` — Imágenes extraídas
