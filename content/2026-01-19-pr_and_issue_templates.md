Title: TIL: Pull Request and Issue Templates
Date: 2026-01-19
Category: Today I Learned
Status: published

I wanted Code for Philly Balancer's PRs to be more easily testable and improve how contributors file new issues so I wrote a pull request and issue template this is inspired by Simon Willison's talk ["Massively increase your productivity on personal projects with comprehensive documentation and automated tests"](https://simonwillison.net/2022/Nov/26/productivity/)

## Pull Request Template:

```
## Description
<!-- Provide a clear and concise description of the changes in this PR -->


## Related Issue
<!-- If this PR relates to an issue, link it here -->


## Manual Tests
<!-- Help reviewers understand your changes work: paste terminal commands/output or attach a screen capture video -->


## Automated Tests
<!-- Help prove your changes work and prevent regressions: describe tests added or explain why tests aren't applicable -->


## Documentation
<!-- Help others understand your changes: list any documentation you've updated or note if updates aren't needed -->


## Reviewers
<!-- Tag the person or team who should review this PR -->


## Notes
<!-- Any additional context, concerns, or discussion points for reviewers -->
```

## Issue Template:

```
---
name: Issue template
about: Help push the project forward
title: ''
labels: ''
assignees: ''

---

## Title
<!-- Title: [Type]: Short description of the problem or goal  -->

## Background
<!-- Why does this change need to happen? -->

## Existing Behavior
<!-- What code or docs are changing? Link or paste as needed -->

## Acceptance Criteria
- [] <!-- What does done look like? -->

## Approach
<!-- How are you tackling this? Update as you go -->

## References
<!-- Anything useful — docs, links, decisions -->

## Risks and Rollback
<!-- Anything that could go wrong, or leave blank if low risk -->

## Screenshots / Recordings
<!-- Before/after visuals or console output if helpful -->
```