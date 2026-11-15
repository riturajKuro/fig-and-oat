#!/usr/bin/env bash
# Cloud-friendly version of sx.sh: runs an Admin GraphQL file against the fig&oat store
# without Shopify CLI (no laptop, no browser login).
# Auth, either:
#   SHOPIFY_CLIENT_ID + SHOPIFY_CLIENT_SECRET  (Dev Dashboard app installed on the store;
#       a short-lived token is fetched with the client credentials grant), or
#   SHOPIFY_TOKEN  (a ready Admin API access token).
# Set these as secrets in the cloud environment. Never print or commit them.
# Usage: bash scripts/sx-token.sh query.graphql [variables.json] [--allow-mutations]
set -euo pipefail
STORE="${SHOPIFY_STORE:-1ws1tg-iy.myshopify.com}"
API="${SHOPIFY_API_VERSION:-2026-10}"
q="$1"; vars="{}"
[ -n "${2:-}" ] && [ "$2" != "--allow-mutations" ] && vars="$(cat "$2")"
if grep -qiE '^\s*mutation' "$q" && [[ " $* " != *" --allow-mutations "* ]]; then
  echo "Refusing: $q is a mutation. Re-run with --allow-mutations after approval." >&2; exit 1
fi

TOKEN="${SHOPIFY_TOKEN:-}"
if [ -z "$TOKEN" ]; then
  : "${SHOPIFY_CLIENT_ID:?Set SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET (or SHOPIFY_TOKEN)}"
  : "${SHOPIFY_CLIENT_SECRET:?Set SHOPIFY_CLIENT_SECRET}"
  resp="$(curl -sS -X POST "https://$STORE/admin/oauth/access_token" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=$SHOPIFY_CLIENT_ID" \
    --data-urlencode "client_secret=$SHOPIFY_CLIENT_SECRET")"
  TOKEN="$(printf '%s' "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("access_token",""))' 2>/dev/null || true)"
  if [ -z "$TOKEN" ]; then
    echo "Token request failed: $(printf '%s' "$resp" | head -c 300)" >&2; exit 1
  fi
fi

body="$(python3 -c 'import json,sys; print(json.dumps({"query": open(sys.argv[1]).read(), "variables": json.loads(sys.argv[2])}))' "$q" "$vars")"
curl -sS -X POST "https://$STORE/admin/api/$API/graphql.json" \
  -H "Content-Type: application/json" -H "X-Shopify-Access-Token: $TOKEN" \
  --data "$body" | python3 -m json.tool
