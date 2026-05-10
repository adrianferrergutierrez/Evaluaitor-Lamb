# docx_extract_skill

## Role

Fase 0 del pipeline: **conversió de DOCX a Markdown estructurat** amb extracció d'imatges. Úsala quan l'input sigui un fitxer `.docx`.

### Principis

- **Fidelitat al contingut.** No alteris ni reinterpretis el text del DOCX.
- **Imatges preservades.** Cada imatge s'extreu com a fitxer independent amb referència al Markdown.
- **Privacitat RGPD.** Tot el processament és local.

## Tools

| # | Nom | Descripció |
|---|-----|-----------|
| 1 | `python-docx` | Extracció de text, taules i imatges del DOCX |
| 2 | `pandoc` (opcional) | Conversió directa DOCX → Markdown si està instal·lat |

## Arguments

`$ARGUMENTS` ha de contenir:
- `input=<path>` — Ruta al DOCX d'entrada
- `output=<path>` — Directori de sortida

Exemple: `/docx_extract input=/path/to/memoria.docx output=/path/to/results/phase0_extract`

## Execution

### 1. Validar inputs
- Verificar que el DOCX d'entrada existeix
- Crear el directori de sortida si no existeix

### 2. Convertir a Markdown

**Opció A: pandoc (si està instal·lat)**
```bash
pandoc "$INPUT_DOCX" -t markdown -o "$OUTPUT_DIR/contents.md" --extract-media="$OUTPUT_DIR/img"
```

**Opció B: python-docx (fallback)**
```python
python3 -c "
import docx, os, re, base64
from pathlib import Path

doc = docx.Document('$INPUT_DOCX')
out_dir = Path('$OUTPUT_DIR')
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / 'img').mkdir(exist_ok=True)

lines = []
img_count = 0

for para in doc.paragraphs:
    style = para.style.name if para.style else ''
    text = para.text.strip()
    if not text:
        lines.append('')
        continue

    if 'Title' in style:
        lines.append(f'# {text}')
    elif 'Heading 1' in style:
        lines.append(f'## {text}')
    elif 'Heading 2' in style:
        lines.append(f'### {text}')
    elif 'Heading 3' in style:
        lines.append(f'#### {text}')
    elif 'List' in style:
        lines.append(f'- {text}')
    else:
        lines.append(text)

# Extract tables as Markdown
for i, table in enumerate(doc.tables):
    lines.append(f'\n### Tabla {i+1}\n')
    header = [cell.text for cell in table.rows[0].cells]
    lines.append('| ' + ' | '.join(header) + ' |')
    lines.append('| ' + ' | '.join(['---'] * len(header)) + ' |')
    for row in table.rows[1:]:
        cells = [cell.text.replace('|', '\\|') for cell in row.cells]
        lines.append('| ' + ' | '.join(cells) + ' |')

# Extract images
for i, rel in enumerate(doc.part.rels.values()):
    if 'image' in rel.reltype:
        ext = rel.target_ref.split('.')[-1] if '.' in rel.target_ref else 'png'
        img_name = f'img_{i}.{ext}'
        img_path = out_dir / 'img' / img_name
        try:
            with open(img_path, 'wb') as f:
                f.write(rel.target_part.blob)
            lines.append(f'\n![Imagen {i+1}](img/{img_name})\n')
            img_count += 1
        except Exception:
            pass

md_content = '\n\n'.join(lines)
(out_dir / 'contents.md').write_text(md_content, encoding='utf-8')
print(f'Extracted: {len(md_content)} chars, {img_count} images')
"
```

Usar `timeout: 300000` (5 minuts) — DOCX grans poden trigar.

### 3. Validar output
Després de completar:
- Verificar que `$OUTPUT_DIR/contents.md` existeix i té contingut substancial (>500 caràcters)
- Verificar que `$OUTPUT_DIR/img/` existeix i comptar imatges
- Informar: mida de `contents.md`, nombre d'imatges extretes

### 4. Control de qualitat ràpid
Llegir les primeres 50 línies de `contents.md` per verificar que és Markdown ben estructurat.

## Error Handling

- **python-docx no instal·lat**: `pip install python-docx`
- **DOCX corrupte**: verificar integritat del fitxer
- **Imatges no extraïbles**: registrar advertència però continuar amb el text
- **Taules complexes**: poden perdre estructura; verificar manualment

## Inputs esperats

- **DOCX** del entregable.

## Output esperat

- `$OUTPUT_DIR/contents.md` — Markdown estructurat amb referències a imatges i taules.
- `$OUTPUT_DIR/img/` — Carpeta amb totes les imatges extretes.
- Resum: `{chars: N, images: M, file_size_kb: X}`.
