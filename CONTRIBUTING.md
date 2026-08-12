# Contributing to tinytext

> **Note:** this repository is a test bed for an automation project and is not
> accepting outside contributions. This file is a fixture — it exists so the
> automation has realistic rules to detect. The rules below are real rules, but
> there is no real project behind them.

Thanks for your interest! This is a small project and we try to keep the
process light, but a few rules keep things tidy.

## Before you start work

**Comment on the issue first and wait to be assigned.** We do not accept pull
requests for issues that have not been claimed. This avoids two people
duplicating effort on the same fix. A comment like "I'd like to work on this"
is enough — a maintainer will assign you, usually within a day.

If an issue has been assigned to someone else, please pick a different one.

## Pull requests

- One issue per pull request. Keep the diff as small as possible.
- Every bug fix needs a test that fails before the fix and passes after it.
- Run `pytest` locally before pushing; CI runs the same suite.
- Follow the pull request template.
- Reference the issue in the description, e.g. `Fixes #12`.

## Sign your commits (DCO)

Every commit must carry a `Signed-off-by` line certifying the Developer
Certificate of Origin. Add it automatically with `git commit -s`. Pull requests
containing unsigned commits will not be merged.

## AI-assisted contributions

AI tools are allowed. If you used one to write any part of the change, please
say so in the pull request description. We do not require anything more than a
one-line disclosure, but undisclosed AI-generated pull requests will be closed.

## Code style

Standard library only. Keep functions small and documented with a docstring
containing a doctest-style example.
