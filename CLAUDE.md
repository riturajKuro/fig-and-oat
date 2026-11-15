# fig&oat: instructions for Claude sessions

Read `HANDOFF.md` first. It is the source of truth for store state, suppliers, to-dos and rules.

## Running in the cloud (claude.ai/code)
- There is no Shopify CLI login in the cloud. Run store queries with `bash shopify-tools/scripts/sx-token.sh <file.graphql> [vars.json] [--allow-mutations]`. It reads the Admin API token from the `SHOPIFY_TOKEN` environment secret.
- Never print, echo or commit the token.
- On the laptop, use `shopify-tools/scripts/sx.sh` (Shopify CLI) instead.

## Shared files
- Google Drive (concierge@figandoat.com), folder "fig&oat": https://drive.google.com/drive/folders/145biQtIgTXlThfGo7EGS5I2dX6yKPVhz
- Save new docs, notes and reports to that Drive folder. When HANDOFF.md changes, commit it here and update the Drive copy too.

## Rules
- Keep answers short and no-BS.
- Show the exact command and get a yes before any Shopify change, install or publish (anything run with `--allow-mutations`).
- Never enter passwords or payment details, and never buy anything.
- Publishing a theme and removing the store password are the owner's actions.
- DSers has no API. The owner maps products in DSers, and Claude guides from their screenshots.
