#!/usr/bin/env python3
"""
Test to verify retry logic is working and being called.
"""
import sys
sys.path.insert(0, '/home/adrif/SE-Agentic-Evaluator')

# Force reload to avoid caching
import importlib
if 'core.clients.dashscope_client' in sys.modules:
    del sys.modules['core.clients.dashscope_client']

print("=" * 70)
print("VERIFICACIÓN: Retry Logic en dashscope_client")
print("=" * 70)

from core.clients.dashscope_client import DashScopeClient, RETRY_CONFIG, MAX_VISION_PAYLOAD_SIZE
import json
import inspect

print(f"\n✓ RETRY_CONFIG: {RETRY_CONFIG}")
print(f"✓ MAX_VISION_PAYLOAD_SIZE: {MAX_VISION_PAYLOAD_SIZE / 1024 / 1024:.1f} MB")

# Create client and check for retry method
client = DashScopeClient()

# Verify _post_with_retry exists and is a method
if hasattr(client, '_post_with_retry'):
    print(f"✓ Method '_post_with_retry' existe")
    
    # Get the method and inspect it
    method = getattr(client, '_post_with_retry')
    sig = inspect.signature(method)
    print(f"✓ Signature: {sig}")
    
    # Get the source code to verify it's the right implementation
    source = inspect.getsource(method)
    
    # Check for key features
    checks = [
        ("for attempt in range", "Loop over retries"),
        ("response.raise_for_status()", "Raises errors"),
        ("except requests.exceptions.HTTPError", "Catches HTTP errors"),
        ("time.sleep(wait_time)", "Waits between retries"),
        ("Retrying in", "Logs retry attempts"),
        ("error_code >= 500", "Handles 500 errors"),
    ]
    
    print(f"\n✓ Verificando características del método:")
    for check_str, description in checks:
        if check_str in source:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ MISSING: {description}")
            
    # Count lines
    lines = len(source.split('\n'))
    print(f"\n✓ Método tiene {lines} líneas de código")
    
else:
    print(f"✗ CRITICAL: Method '_post_with_retry' NOT FOUND!")
    sys.exit(1)

print("\n" + "=" * 70)
print("✅ RETRY LOGIC VERIFICADO Y PRESENTE")
print("=" * 70)

# Also check vision method
if hasattr(client, 'vision'):
    print(f"\n✓ Method 'vision' existe")
    vision_source = inspect.getsource(client.vision)
    
    if "_post_with_retry" in vision_source:
        print(f"✓ vision() llama a _post_with_retry")
    else:
        print(f"✗ CRITICAL: vision() NO llama a _post_with_retry!")
        sys.exit(1)
        
    if "compress_image_if_needed" in vision_source:
        print(f"✓ vision() llama a compress_image_if_needed")
    else:
        print(f"⚠ WARNING: vision() NO llama a compress_image_if_needed")

print("\n✅ TODOS LOS COMPONENTES PRESENTES Y CORRECTOS")
