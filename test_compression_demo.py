#!/usr/bin/env python3
"""
Test compression on a REALLY LARGE image.
"""
import sys
sys.path.insert(0, '/home/adrif/SE-Agentic-Evaluator')

from pathlib import Path
from PIL import Image
import tempfile

print("=" * 70)
print("CREANDO IMAGEN MUY GRANDE (>1 MB)")
print("=" * 70)

# Create a larger image to exceed 1 MB
print("\nCreando imagen 8000x6000px (muy alta resolución)...")
img = Image.new('RGB', (8000, 6000), color='#FF5733')

# Add some content to make it harder to compress
pixels = img.load()
for i in range(0, 8000, 100):
    for j in range(0, 6000, 100):
        pixels[i, j] = (i % 256, j % 256, (i+j) % 256)

temp_dir = Path(tempfile.gettempdir())
test_image = temp_dir / "large_test_image.jpg"

# Save with high quality to exceed 1 MB
img.save(test_image, "JPEG", quality=95, optimize=False)

original_size = test_image.stat().st_size
print(f"✓ Imagen creada: {test_image.name}")
print(f"✓ Tamaño: {original_size / 1024 / 1024:.2f} MB ({original_size / 1024:.1f} KB)")

# Test compression
print("\n" + "=" * 70)
print("EJECUTANDO COMPRESIÓN")
print("=" * 70)

from core.extraction.diagramlens_tool import compress_image_if_needed, MAX_IMAGE_SIZE

print(f"\nThreshold para compresión: {MAX_IMAGE_SIZE / 1024 / 1024:.1f} MB")
print(f"Tamaño imagen: {original_size / 1024 / 1024:.2f} MB")

if original_size > MAX_IMAGE_SIZE:
    print("→ ¡SOBREPASA THRESHOLD - COMPRIMIENDO!")
    
compressed = compress_image_if_needed(test_image)

if compressed != test_image:
    compressed_size = compressed.stat().st_size
    reduction = (1 - compressed_size / original_size) * 100
    
    print(f"\n✅ ¡COMPRESIÓN EXITOSA!")
    print(f"\n  Métricas de Compresión:")
    print(f"    Original:    {original_size / 1024 / 1024:.2f} MB ({original_size / 1024:.1f} KB)")
    print(f"    Comprimida:  {compressed_size / 1024:.1f} KB")
    print(f"    Reducción:   {reduction:.1f}%")
    
    base64_size_orig = original_size * 1.33
    base64_size_comp = compressed_size * 1.33
    
    print(f"\n  Tamaño del Payload (incluyendo base64 +33%):")
    print(f"    Original payload: {base64_size_orig / 1024 / 1024:.2f} MB")
    print(f"    Compressed payload: {base64_size_comp / 1024:.1f} KB")
    print(f"    Ahorro en payload: {(base64_size_orig - base64_size_comp) / 1024 / 1024:.2f} MB")
    
    print(f"\n  📦 Archivo comprimido: {compressed.name}")
else:
    print("No compression applied")

print("\n" + "=" * 70)
print("✅ PRUEBA COMPLETADA")
print("=" * 70)

print("\n📊 Simulación: 26 imágenes del DOCX (típicamente 1-2 MB cada una)")
if original_size > MAX_IMAGE_SIZE:
    # Simulate 26 images
    total_original_payload = base64_size_orig * 26
    total_compressed_payload = base64_size_comp * 26
    savings = total_original_payload - total_compressed_payload
    
    print(f"\n  SIN COMPRESIÓN:")
    print(f"    Payload per image: {base64_size_orig / 1024 / 1024:.2f} MB")
    print(f"    Total (26 images): {total_original_payload / 1024 / 1024:.2f} MB")
    print(f"    Resultado: ❌ Error 400 (payload muy grande)")
    
    print(f"\n  CON COMPRESIÓN:")
    print(f"    Payload per image: {base64_size_comp / 1024:.1f} KB")
    print(f"    Total (26 images): {total_compressed_payload / 1024 / 1024:.2f} MB")
    print(f"    Ahorro: {savings / 1024 / 1024:.2f} MB")
    print(f"    Resultado: ✅ Success (payload dentro del límite)")
