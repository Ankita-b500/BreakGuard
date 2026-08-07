"""
Stage 2
Call Finder

This module finds where changed functions are used
inside the repository.
"""

from pathlib import Path
import ast


class CallFinder:
    """Find function call sites across Python files."""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)

    def find_call_sites(self, changed_functions):
        """
        Search all Python files for calls to changed functions.

        Args:
            changed_functions (list[str]):
                List of modified function names.

        Returns:
            list[str]:
                Files containing calls to modified functions.
        """

        affected_files = []

        for py_file in self.repo_path.rglob("*.py"):

            # Ignore virtual environment
            if "venv" in py_file.parts:
                continue

            try:
                source = py_file.read_text(encoding="utf-8")
                tree = ast.parse(source)

                for node in ast.walk(tree):

                    if isinstance(node, ast.Call):

                        # Direct function call
                        if isinstance(node.func, ast.Name):
                            if node.func.id in changed_functions:
                                affected_files.append(str(py_file))
                                break

                        # Object method call
                        elif isinstance(node.func, ast.Attribute):
                            if node.func.attr in changed_functions:
                                affected_files.append(str(py_file))
                                break

            except Exception:
                # Ignore files with parsing errors
                continue

        return sorted(set(affected_files))