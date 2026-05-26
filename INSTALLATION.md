# 📦 Installation & Deployment Guide

## Dependencies

### Required
- Python 3.11+
- `requests` (already in requirements.txt)

### Optional (Recommended)
- `Pillow` - For automatic image compression

## Installation Steps

### 1. Update Dependencies

```bash
# Install Pillow for image compression (optional but recommended)
pip install Pillow>=10.0.0

# Verify installation
python3 -c "from PIL import Image; print('✓ Pillow installed')"
```

### 2. Verify Core Modules

```bash
cd SE-Agentic-Evaluator

# Test imports
python3 -c "
from core.clients.dashscope_client import DashScopeClient, RETRY_CONFIG
from core.extraction.diagramlens_tool import describe_diagrams
print('✓ All modules imported successfully')
"
```

### 3. Environment Setup

Ensure the following environment variables are set:

```bash
# Required
export DASHSCOPE_API_KEY="sk-..." 

# Optional (defaults to singapore)
export DASHSCOPE_REGION="singapore"  # singapore, us, or china
export DASHSCOPE_MODEL="qwen3.5-plus"
```

## Validation

### Run Test Suite

```bash
# Test all fixes
python3 tests/test_describe_diagrams_fix.py

# Expected output:
# ✓ All tests completed successfully!
```

### Quick Manual Test

```bash
python3 << 'EOF'
import logging
logging.basicConfig(level=logging.INFO)

from core.extraction.diagramlens_tool import describe_diagrams, HAS_PIL
from pathlib import Path

print(f"PIL available: {HAS_PIL}")

# Test with actual document if available
test_doc = Path("tests/test-1-hito-2/output/phase0_extract/contents.md")
if test_doc.exists():
    result = describe_diagrams(str(test_doc), model="qwen-vl-plus")
    print(f"Result: {result}")
else:
    print("No test document found")
EOF
```

## Deployment Checklist

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Pillow installed (optional but recommended)
- [ ] DASHSCOPE_API_KEY set in environment
- [ ] Test suite passes
- [ ] Manual test with sample document successful

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'PIL'`

**Solution**: Install Pillow
```bash
pip install Pillow>=10.0.0
```

**Note**: The application will work without Pillow, but large images won't be automatically compressed.

### Error: `DASHSCOPE_API_KEY` not set

**Solution**: Set environment variable
```bash
export DASHSCOPE_API_KEY="your-api-key-here"

# Verify
echo $DASHSCOPE_API_KEY
```

### Error: `400 Bad Request` still occurring

**Debugging Steps**:
1. Enable debug logging:
   ```python
   import logging
   logging.getLogger("core.clients.dashscope_client").setLevel(logging.DEBUG)
   logging.getLogger("core.extraction.diagramlens_tool").setLevel(logging.DEBUG)
   ```

2. Check payload sizes in logs - should see compression messages

3. Verify API connection:
   ```python
   from core.clients.dashscope_client import DashScopeClient
   client = DashScopeClient()
   print(client.check_connection())
   ```

4. Check API status and rate limits

## Performance Notes

### Compression Overhead
- Small images (<1 MB): No compression, immediate processing
- Large images (>1 MB): ~1-2s compression time
- Typical batch (26 images): +30-60s total (but eliminates 400 errors)

### Retry Backoff Timing
- Attempt 1: Immediate
- Attempt 2: Wait 1s
- Attempt 3: Wait 2s  
- Attempt 4: Wait 4s

## Configuration Fine-Tuning

### Increase Compression Aggressiveness

```python
# In core/extraction/diagramlens_tool.py
MAX_IMAGE_SIZE = 512 * 1024  # 512 KB (default: 1 MB)
JPEG_QUALITY = 75  # Lower quality = smaller size (default: 85)
```

### Increase Retry Attempts

```python
# In core/clients/dashscope_client.py
RETRY_CONFIG = {
    "max_retries": 5,  # More retries
    "base_delay": 2.0,  # Longer initial delay
    "max_delay": 120.0,  # Longer max delay
    "backoff_factor": 2.0,
}
```

## Monitoring

### Log Format

All vision API calls will log:
- Payload size (KB)
- Image file size (MB)
- Compression details
- Retry attempts (if any)
- Success/failure status

Example:
```
Image img_1.jpg is 2.10 MB. Compressing to 1200px max width...
Compression complete: 2.10 MB → 0.08 MB (96.2% reduction)
Payload size: 95.50 KB
DashScope vision 'qwen-vl-plus': 250 input tokens, 180 output tokens
```

## Rollback

If you need to revert these changes:

```bash
git checkout core/clients/dashscope_client.py
git checkout core/extraction/diagramlens_tool.py
```

The original versions will have no retry logic or compression, but will function without breaking changes.
