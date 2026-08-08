# BreakGuard Agents and Skills

## Custom Agent

### BreakGuard Analysis Agent

Location:

`agents/breakguard-analysis-agent.md`

The BreakGuard Analysis Agent analyzes pull requests for potential breaking changes and blast-radius risk.

It coordinates the analysis workflow:

Pull Request
→ Diff Parser
→ Call Finder
→ Risk Scorer
→ Reporter

The agent identifies changed functionality, affected dependencies, test coverage, breaking changes, and overall risk.

## Custom Skill

### PR Risk Analysis Skill

Location:

`skills/pr-risk-analysis/SKILL.md`

The PR Risk Analysis Skill provides a repeatable procedure for analyzing a pull request.

It covers:

- Diff analysis
- Changed function detection
- Dependency analysis
- Test coverage analysis
- Breaking change detection
- Risk scoring
- Risk reporting

## Relationship

The custom agent uses the PR Risk Analysis Skill as its structured procedure for evaluating pull requests.

Together they provide the agent behavior and reusable analysis procedure required by BreakGuard.