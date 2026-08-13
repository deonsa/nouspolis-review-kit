# Maintainer Guide

Prepare an N1 candidate for principal-separated external review in this order:

1. Identify a willing reviewer and the GitHub account or organization that will control their fork.
2. Determine the expected reviewer workflow identity for that fork.
3. Add that exact identity to NousPolis `config/review_authority.json` through the governed change process. Do not use a wildcard or founder-controlled identity.
4. Freeze the resulting exact NousPolis candidate commit. Further candidate changes invalidate the target.
5. Populate `target/files/` with the smallest sufficient public snapshot of that exact candidate, preserving repository-relative paths.
6. Create `target/TARGET_MANIFEST.json` with `status: FROZEN_FOR_REVIEW`, the exact commit, generation time, file hashes, and unchanged required invariant list.
7. Run `python scripts/validate_review.py --target-only`.
8. Run the NousPolis external witness workflow against the same exact target commit.
9. Ask the reviewer to fork this public kit, perform the review, and generate the review attestation from their fork.
10. Verify the returned review and attestation against the precommitted reviewer identity before importing it into NousPolis.
11. Re-run the complete N1 maturity report. A passing review does not itself authorize an automatic maturity transition.

Do not control the reviewer's GitHub account, fork, workflow run, or final judgment. Do not ask a reviewer merely to countersign a review prepared by NousPolis.
