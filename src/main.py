"""
BreakGuard - Main Integration Pipeline
"""

from pathlib import Path

from diff_parser import DiffParser
from call_finder import CallFinder
from risk_scorer import calculate_risk
from reporter import Reporter


def main():

    # Sample repository used for testing
    repo_path = "tests/sample_repo"

    parser = DiffParser()
    finder = CallFinder(repo_path)
    reporter = Reporter()

    changed_functions = []
    changed_classes = []

    # Parse every Python file in sample repository
    for file in Path(repo_path).rglob("*.py"):

        tree = parser.parse_file(str(file))

        functions = parser.get_functions(tree)
        classes = parser.get_classes(tree)

        changed_functions.extend(
            [f["name"] for f in functions]
        )

        changed_classes.extend(classes)

    # Find affected files
    affected_files = finder.find_call_sites(changed_functions)

    # Placeholder values until GitHub integration
    untested_files = []
    breaking_changes = []

    # Calculate risk
    result = calculate_risk(
        changed_functions=changed_functions,
        affected_files=affected_files,
        untested_files=untested_files,
        breaking_changes=breaking_changes,
    )

    # Generate report
    markdown = reporter.generate(result)

    print("=" * 60)
    print(markdown)
    print("=" * 60)


if __name__ == "__main__":
    main()