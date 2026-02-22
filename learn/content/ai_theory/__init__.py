"""AI Theory & Foundations course - module registry."""

from learn.content.ai_theory.module_01 import MODULE as MODULE_01
from learn.content.ai_theory.module_02 import MODULE as MODULE_02
from learn.content.ai_theory.module_03 import MODULE as MODULE_03
from learn.content.ai_theory.module_04 import MODULE as MODULE_04
from learn.content.ai_theory.module_05 import MODULE as MODULE_05
from learn.content.ai_theory.module_06 import MODULE as MODULE_06
from learn.content.ai_theory.module_07 import MODULE as MODULE_07
from learn.content.ai_theory.module_08 import MODULE as MODULE_08
from learn.content.ai_theory.module_09 import MODULE as MODULE_09
from learn.content.ai_theory.module_10 import MODULE as MODULE_10
from learn.content.ai_theory.module_11 import MODULE as MODULE_11
from learn.content.ai_theory.module_12 import MODULE as MODULE_12
from learn.content.ai_theory.module_13 import MODULE as MODULE_13
from learn.content.ai_theory.module_14 import MODULE as MODULE_14

_COURSE_DIR = "courses/ai-theory"

# All modules in order, with directory paths prefixed for the new layout.
AI_THEORY_MODULES = [
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
]

# Prefix each module's directory with the course path.
for _m in AI_THEORY_MODULES:
    _orig = _m["directory"]
    if not _orig.startswith(_COURSE_DIR):
        _m["directory"] = f"{_COURSE_DIR}/{_orig}"
