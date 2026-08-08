# PR Risk Analysis Skill

## Purpose

Provide a repeatable procedure for analyzing a GitHub Pull Request for breaking changes and blast-radius risk.

## Inputs

- Pull request diff
- Changed files
- Changed functions and classes
- Repository dependency information
- Test files

## Procedure

1. Parse the pull request diff.
2. Identify changed functions, classes, and APIs.
3. Find code that calls or depends on the changed functionality.
4. Determine which affected areas have tests.
5. Identify potential breaking API changes.
6. Calculate the risk score.
7. Determine the risk level.
8. Generate a concise risk report.

## Risk Factors

The analysis considers:

- Number of changed functions
- Number of affected files
- Number of untested affected files
- Number of breaking changes

## Risk Levels

- LOW: score below 40
- MEDIUM: score from 40 to 79
- HIGH: score 80 or above

## Output Format

The report should contain:

- Risk Level
- Risk Score
- Blast Radius
- Tested Calls
- Untested Calls
- Summary

## Principle

Passing CI tests does not automatically mean that a change is low risk. The purpose of this skill is to expose dependency and blast-radius risks that ordinary tests may not reveal.