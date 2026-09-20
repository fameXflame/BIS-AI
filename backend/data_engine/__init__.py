"""
Data Engine package for BIS AI.

Provides standard database access, search lookups, and domain filtering.
"""

from .standards_db import (
    BIS_STANDARDS_DATABASE,
    get_all_standards,
    get_standard_by_code,
    get_standards_by_division,
)

__all__ = [
    "BIS_STANDARDS_DATABASE",
    "get_all_standards",
    "get_standard_by_code",
    "get_standards_by_division",
]
