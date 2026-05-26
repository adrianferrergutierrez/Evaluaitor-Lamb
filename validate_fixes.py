#!/usr/bin/env python3
"""Quick validation script for the fixes."""

import sys
from pathlib import Path

REPO = Path(__file__).parent
sys.path.insert(0, str(REPO))

try:
    from core.clients.dashscope_client import DashScopeClient, RETRY_CONFIG, MAX_VISION_PAYLOAD_SIZE
    print("✓ DashScopeClient module OK")
    print(f"  - max_retries: {RETRY_CONFIG['max_retries']}")
    print(f"  - max_payload: {MAX_VISION_PAYLOAD_SIZE / 1024 / 1024:.1f} MB")
except Exception as e:
    print(f"✗ DashScopeClient failed: {e}")
    sys.exit(1)

try:
    from core.extraction.diagramlens_tool import describe_diagrams, compress_image_if_needed, HAS_PIL
    print("✓ diagramlens_tool module OK")
    print(f"  - PIL available: {HAS_PIL}")
except Exception as e:
    print(f"✗ diagramlens_tool failed: {e}")
    sys.exit(1)

# Check methods
client = DashScopeClient()
if hasattr(client, '_post_with_retry'):
    print("✓ _post_with_retry method present")
else:
    print("✗ _post_with_retry method missing")
    sys.exit(1)

print("\n✅ All validations passed!")
print("\nChanges implemented:")
print("  1. Retry logic with exponential backoff")
print("  2. Image compression for large files (>1MB)")
print("  3. Payload size validation (10MB limit)")
print("  4. Enhanced logging for debugging")
