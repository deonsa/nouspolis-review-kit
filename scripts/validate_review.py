#!/usr/bin/env python3
import hashlib
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest_path = root / 'target' / 'TARGET_MANIFEST.json'
review_path = root / 'review' / 'N1_CANDIDATE_REVIEW.json'

manifest = json.loads(manifest_path.read_text())
review = json.loads(review_path.read_text())

commit = manifest.get('target_commit', '')
if manifest.get('status') != 'FROZEN_FOR_REVIEW':
    raise SystemExit('target manifest is not frozen')
if not re.fullmatch(r'[0-9a-f]{40}', commit):
    raise SystemExit('invalid target commit')
if review.get('target_commit') != commit:
    raise SystemExit('review targets a different commit')
manifest_hash = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
if review.get('target_manifest_sha256') != manifest_hash:
    raise SystemExit('review target manifest hash mismatch')
required = set(manifest.get('review_required_invariants', []))
reviewed = set(review.get('invariants_reviewed', []))
if not required or not required.issubset(reviewed):
    raise SystemExit('required invariant coverage is incomplete')
allowed = {'APPROVE_N1_CANDIDATE','APPROVE_WITH_RECORDED_RESIDUAL_RISK','DEFER_PENDING_REMEDIATION','REJECT_N1_CANDIDATE'}
if review.get('disposition') not in allowed:
    raise SystemExit('unsupported disposition')
if review.get('disposition') in {'APPROVE_N1_CANDIDATE','APPROVE_WITH_RECORDED_RESIDUAL_RISK'}:
    if review.get('unresolved_critical_findings'):
        raise SystemExit('approval contains unresolved Critical findings')
print('review validation passed')
