# Reviewer Guide

Your task is to adversarially evaluate whether the identified NousPolis N1 candidate enforces the institutional safeguards it claims to enforce. You are not being asked to endorse NousPolis, its philosophy, or its political legitimacy.

## Review standard

Look for compliant-looking paths that defeat intended safeguards, including authority concentration, classification capture, precedence inversion, self-certification, configuration bypass, evaluation endogeneity, evidence gaming, maturity laundering, failure and recovery edge cases, and discrepancies between governing prose and executable enforcement.

## Required coverage

The target manifest contains the complete list of semantic invariants assigned to Review Authority. Your `invariants_reviewed` field must cover every one you actually evaluated.

## Findings

Use `CRITICAL`, `HIGH`, `MEDIUM`, and `LOW`. Each finding should include a stable ID, status, affected invariant IDs, evidence, and recommendation.

## Disposition

Allowed dispositions are `APPROVE_N1_CANDIDATE`, `APPROVE_WITH_RECORDED_RESIDUAL_RISK`, `DEFER_PENDING_REMEDIATION`, and `REJECT_N1_CANDIDATE`.

The N1 gate accepts only the first two, and an approval cannot contain an unresolved Critical finding. The workflow signs any valid disposition; it does not require a favorable outcome.

## Conflicts and separation

State your relationship to the founder/project, any compensation or material interest, infrastructure relationship, and the separation level you believe applies. NousPolis separately determines whether the claimed separation level satisfies its rules.

## AI assistance

You may use AI tools for code reading, attack generation, or summarization, but disclose material AI assistance in `methodology` and personally evaluate the evidence and conclusions.

## Chronology

Review the exact commit in `target/TARGET_MANIFEST.json`. If the target changes, a new or explicitly scoped re-review is required.
