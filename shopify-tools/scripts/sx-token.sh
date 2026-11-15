#!/usr/bin/env bash
# Cloud-friendly version of sx.sh: runs an Admin GraphQL file against the fig&oat store
# with an Admin API access token instead of Shopify CLI (no laptop, no browser login).
# Needs env var SHOPIFY_TOKEN (custom app Admin API token, set as a secret in the cloud environment).
# Usage: bash scripts/sx-token.sh query.graphql [variables.json] [--allow-mutations]
set -euo pipefail
STORE="${SHOPIFY_STORE:-1ws1tg-iy.myshopify.com}"
API="${SHOPIFY_API_VERSION:-2026-10}"
: "${SHOPIFY_TOKEN:?Set SHOPIFY_TOKEN (Admin API access token) first}"
q="$1"; vars="{}"
[ -n "${2:-}" ] && [ "$2" != "--allow-mutations" ] && vars="$(cat "$2")"
if grep -qiE '^\s*mutation' "$q" && [[ " $* " != *" --allow-mutations "* ]]; then
  echo "Refusing: $q is a mutation. Re-run with --allow-mutations after approval." >&2; exit 1
fi
body="$(python3 -c 'import json,sys; print(json.dumps({"query": open(sys.argv[1]).read(), "variables": json.loads(sys.argv[2])}))' "$q" "$vars")"
curl -sS -X POST "https://$STORE/admin/api/$API/graphql.json" \
  -H "Content-Type: application/json" -H "X-Shopify-Access-Token: $SHOPIFY_TOKEN" \
  --data "$body" | python3 -m json.tool
