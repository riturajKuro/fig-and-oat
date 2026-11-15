#!/usr/bin/env bash
# Run an Admin GraphQL file against the fig&oat store via Shopify CLI.
# Usage: bash scripts/sx.sh query.graphql [variables.json] [--allow-mutations]
args=(store execute --store 1ws1tg-iy.myshopify.com --json --query-file "$1")
[ -n "$2" ] && [ "$2" != "--allow-mutations" ] && args+=(--variable-file "$2")
[[ " $* " == *" --allow-mutations "* ]] && args+=(--allow-mutations)
shopify "${args[@]}" 2>&1 | grep -v -e '^{"type":"progress"' -e '^<claude-code-hint'
