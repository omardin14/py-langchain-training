"""Course and module content registry."""

import os

from learn.content.courses import COURSES
from learn.parser import parse_readme

# Resolve the project root (parent of learn/ package)
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get_course(course_id):
    """Get a course by ID. Returns None if not found."""
    for c in COURSES:
        if c["id"] == course_id:
            return c
    return None


def load_pages(module):
    """Load lesson pages from the module's README.md using markers.

    Returns a list of {"title": str, "content": str} dicts.
    Returns empty list if README has no lesson markers.
    """
    readme_path = os.path.join(_PROJECT_ROOT, module["directory"], "README.md")
    return parse_readme(readme_path)


def get_module(course, module_id):
    """Get a module by ID within a course. Returns None if not found."""
    for m in course["modules"]:
        if m["id"] == module_id:
            return m
    return None
