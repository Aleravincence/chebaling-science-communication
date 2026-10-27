# Contributing

## Before changing the skill

Decide whether the change is a reusable editorial rule, a measured house-style token, a deterministic audit check, a script bug, or a project-specific fact that should stay outside the skill.

Keep local article facts and source files outside this repository.

## Branch and pull request

1. Create `feat/<topic>` or `fix/<topic>`.
2. Make the smallest change that solves the reusable problem.
3. Run the skill validator.
4. Test the audit script on at least one representative DOCX.
5. Include the command and result in the pull request.
6. For layout changes, include before/after page screenshots.
7. Update `CHANGELOG.md`.

## Style changes

A style change should state the measured before value, the measured after value, why the new value is more reusable, which reference file changed, and which figure or page demonstrates the result.

Do not turn one article's accidental formatting into a universal rule. Capture local exceptions as examples, not as mandatory instructions.

## Data and privacy

Never commit planning PDFs or Word files received privately, participant names or contact information, unpublished interview transcripts, the complete article deliverable unless the team explicitly decides to publish it, credentials, tokens, or local absolute paths.

Use fictional placeholders only when they are clearly labelled and contain no real personal data.

## Required checks

Run the skill validator and the article audit before opening a pull request. The mechanical checks do not prove scientific accuracy. A human reviewer must still compare every material claim with its source.
