"""
Stage 1: Diff Parser

This module parses Python source files using Tree-sitter.
For Milestone 1, it only loads a Python file and builds its AST.
"""

from pathlib import Path
from tree_sitter import Language, Parser
import tree_sitter_python


class DiffParser:
    """Parses Python source files using Tree-sitter."""

    def __init__(self):
        self.parser = Parser()
        self.parser.language = Language(tree_sitter_python.language())

    def parse_file(self, file_path: str):
        """
        Parse a Python source file and return its AST.

        Args:
            file_path: Path to a Python file.

        Returns:
            Tree-sitter syntax tree.
        """
        source = Path(file_path).read_text(encoding="utf-8")
        tree = self.parser.parse(source.encode("utf-8"))
        return tree


if __name__ == "__main__":
    parser = DiffParser()

    # Change this path to any Python file for testing
    tree = parser.parse_file("sample.py")

    print("✅ Python file parsed successfully!")
    print(tree.root_node)