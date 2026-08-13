# NousPolis External Review Kit

Public toolkit for principal-separated external review of NousPolis governance candidates.

## Purpose

This repository is intended to be forked by an external reviewer. The reviewer examines a frozen NousPolis candidate, records findings and disposition, and runs the included GitHub Actions workflow from their own fork.

The resulting Sigstore certificate identity is tied to the reviewer's GitHub repository and workflow run, allowing NousPolis to verify that the review artifact came from the precommitted external reviewer principal.

## Included

- `REVIEWER_GUIDE.md` — adversarial review method and disposition rules.
- `MAINTAINER_GUIDE.md` — candidate-freezing and handoff sequence.
- `target/TARGET_MANIFEST.template.json` — target snapshot template and required invariant list.
- `review/N1_CANDIDATE_REVIEW.template.json` — structured review template.
- `scripts/validate_review.py` — fail-closed target/review consistency checks.
- `.github/workflows/attest-review.yml` — reviewer-side Sigstore attestation workflow.

## Reviewer flow

1. Fork this repository to an independently controlled GitHub account or organization.
2. Confirm the published target manifest identifies the exact candidate you were asked to review.
3. Complete `review/N1_CANDIDATE_REVIEW.json` using the supplied template and guide.
4. Commit the completed review in your fork.
5. Run **Actions → Attest NousPolis Review → Run workflow** from your fork.
6. Return the generated `nouspolis-review-attestation` artifact unchanged.

A valid review may approve, approve with residual risk, defer, or reject the candidate. The attestation proves provenance of the review artifact; it does not force a favorable outcome or self-certify reviewer independence.
