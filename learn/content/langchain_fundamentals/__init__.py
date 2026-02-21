"""LangChain Fundamentals course - module registry."""

from learn.content.langchain_fundamentals.module_01 import MODULE as MODULE_01
from learn.content.langchain_fundamentals.module_02 import MODULE as MODULE_02
from learn.content.langchain_fundamentals.module_03 import MODULE as MODULE_03
from learn.content.langchain_fundamentals.module_04 import MODULE as MODULE_04
from learn.content.langchain_fundamentals.module_05 import MODULE as MODULE_05
from learn.content.langchain_fundamentals.module_06 import MODULE as MODULE_06
from learn.content.langchain_fundamentals.module_07 import MODULE as MODULE_07
from learn.content.langchain_fundamentals.module_08 import MODULE as MODULE_08
from learn.content.langchain_fundamentals.module_09 import MODULE as MODULE_09
from learn.content.langchain_fundamentals.module_10 import MODULE as MODULE_10
from learn.content.langchain_fundamentals.module_11 import MODULE as MODULE_11
from learn.content.langchain_fundamentals.module_12 import MODULE as MODULE_12
from learn.content.langchain_fundamentals.module_13 import MODULE as MODULE_13
from learn.content.langchain_fundamentals.module_14 import MODULE as MODULE_14
from learn.content.langchain_fundamentals.module_15 import MODULE as MODULE_15
from learn.content.langchain_fundamentals.module_16 import MODULE as MODULE_16
from learn.content.langchain_fundamentals.module_17 import MODULE as MODULE_17
from learn.content.langchain_fundamentals.module_18 import MODULE as MODULE_18
from learn.content.langchain_fundamentals.module_19 import MODULE as MODULE_19

_COURSE_DIR = "courses/langchain-fundamentals"

# All modules in order, with directory paths prefixed for the new layout.
LANGCHAIN_MODULES = [
    MODULE_01,
    MODULE_02,
    MODULE_03,
    MODULE_04,
    MODULE_05,
    MODULE_06,
    MODULE_07,
    MODULE_08,
    MODULE_09,
    MODULE_10,
    MODULE_11,
    MODULE_12,
    MODULE_13,
    MODULE_14,
    MODULE_15,
    MODULE_16,
    MODULE_17,
    MODULE_18,
    MODULE_19,
]

# Prefix each module's directory with the course path so the rest of the app
# resolves files correctly without touching individual module_XX.py files.
for _m in LANGCHAIN_MODULES:
    _orig = _m["directory"]
    if not _orig.startswith(_COURSE_DIR):
        _m["directory"] = f"{_COURSE_DIR}/{_orig}"
    # Also prefix setup.module_dir if present
    if "setup" in _m and "module_dir" in _m["setup"]:
        _setup_dir = _m["setup"]["module_dir"]
        if not _setup_dir.startswith(_COURSE_DIR):
            _m["setup"]["module_dir"] = f"{_COURSE_DIR}/{_setup_dir}"
