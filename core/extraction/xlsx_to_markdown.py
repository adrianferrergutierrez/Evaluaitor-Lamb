"""
core/extraction/xlsx_to_markdown.py
====================================
Tool: convert an Excel (.xlsx) rubric table to Markdown format.

Reads the first sheet of an Excel file, detects the header row 
(containing level scores like "Insuficiente (0)"), and converts 
the table into a Markdown table compatible with rubric_importer.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)


def xlsx_to_markdown(input: str, output: str) -> Dict[str, Any]:
    """Convert an Excel rubric to Markdown.

    Parameters
    ----------
    input:
        Path to the .xlsx file.
    output:
        Path to write the generated Markdown file.

    Returns
    -------
    dict
        Keys: ``markdown_path`` (path to generated file).
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas is required. Install with: pip install pandas openpyxl")

    input_path = Path(input)
    output_path = Path(output)

    df = pd.read_excel(str(input_path), header=None)

    # Find header row: look for a row containing level scores like "(0)", "(10)"
    header_idx = None
    for i, row in df.iterrows():
        row_str = " ".join(str(v) for v in row if pd.notna(v))
        if re.search(r"\(\d+\)", row_str):
            header_idx = i
            break

    if header_idx is None:
        # Fallback: assume first row is header
        header_idx = 0

    # Extract table from header onwards
    table_df = df.iloc[header_idx:]
    table_df.columns = table_df.iloc[0]
    table_df = table_df[1:]

    # Clean up NaN values
    table_df = table_df.fillna("")

    # Convert to Markdown
    md_content = table_df.to_markdown(index=False)

    output_path.write_text(md_content, encoding="utf-8")
    logger.info("Converted %s to Markdown at %s", input, output)
    return {"markdown_path": str(output_path)}
