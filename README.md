# BreakGuard

## Blast Radius & Breaking Change Detection for Pull Requests

BreakGuard is a GitHub Action that analyzes Pull Requests to detect potential breaking changes before they are merged.

### Features
- Detect changed Python functions/classes
- Find dependent call sites
- Calculate blast radius
- Check test coverage
- Generate a risk report
- Comment directly on GitHub Pull Requests

## Tech Stack
- Python
- Tree-sitter
- GitHub Actions
- Docker
- PyGithub
- Pytest