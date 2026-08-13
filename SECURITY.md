# Security and Privacy

This review kit is designed to operate without repository secrets.

Do not add private credentials, private signing material, passwords, sensitive personal data, or confidential third-party material.

The attestation workflow uses GitHub Actions OIDC and Sigstore keyless signing with minimal workflow permissions. Reviewers should inspect `.github/workflows/attest-review.yml` before enabling Actions in a fork.

Target snapshots should contain only material intentionally approved for public external review. Hashes in `target/TARGET_MANIFEST.json` bind each published target file to the reviewed candidate. If a target hash fails validation, stop and request a corrected target bundle.
