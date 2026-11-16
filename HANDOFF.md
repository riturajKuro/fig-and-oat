# fig&oat: handoff to a new Claude Code account

Last updated: 15 Nov 2026. In the new account, start the first session in this folder and say:
"Read HANDOFF.md and continue the fig&oat store setup."

## Where things live
- **Google Drive is the shared home for all devices:** folder "fig&oat" in concierge@figandoat.com's Drive: https://drive.google.com/drive/folders/145biQtIgTXlThfGo7EGS5I2dX6yKPVhz. Save new docs, notes and assets there, and keep HANDOFF.md there up to date.
- Laptop copy: `Desktop\fig-and-oat`. It's needed to run the Shopify CLI scripts. When it changes, copy the change to Drive too.

## What the business is
- **Brand:** fig&oat (store name "Fig & Oat"). Shopify dropshipping, with AliExpress suppliers through DSers. US customers only.
- **Domain:** figandoat.com is owned but **not connected to Shopify yet**.
- **Email:** concierge@figandoat.com. This is also the Shopify login.
- **Store:** 1ws1tg-iy.myshopify.com. Still password protected ("Opening soon").
- **Owner style:** knows content and Meta ads, wants concise, no-BS answers.

## Store state (checked live 15 Nov 2026)
- **Live theme:** "fig&oat (draft)", gid://shopify/OnlineStoreTheme/194573140247 (MAIN).
  - It has the logo `figandoat-logo-header.png` and favicon `figandoat-favicon.png`.
  - Colors: background #FAF6EF, text #4A1F3D, accent #6B4A5E and #E6DCCB. Font: Jost.
  - The old "Horizon" theme (194475589911) is unpublished.
- **Policies:** Shipping and Refund (30-day guarantee, customer keeps the product) are saved in Shopify. Privacy and Terms are Shopify templates. Drafts are in `shop-policies-draft.md`.
- **Products:** all 4 are **ACTIVE**, have **no images**, and use placeholder compare-at prices (an FTC risk, so remove them or make them real):

| Handle | Variants (SKU, price) |
|---|---|
| smooth-stick (hero) | FO-STICK-1 $24 · FO-STICK-2M (2 sticks + mitt) $44 · FO-STICK-3MH (3 sticks + mitt + heel) $59 |
| smooth-skin-set | FO-SET-3 $39 |
| exfoliating-mitt | FO-MITT-1 $12 |
| heel-stick | FO-HEEL-1 $16 |

### Re-checked 15 Nov 2026 (new account)
- Live store matches the above: 4 ACTIVE products, same SKUs and prices, same themes.
- **New:** products show no sales-channel publications and no Online Store URL, so they're probably not published to the Online Store yet. Check before launch.
- All variant weights are 0 lb. Compare-at prices are still placeholders ($32/$60/$90/$52/$16/$22).
- Heel Stick SEO title says "Urea + Salicylic". Confirm salicylic acid from the sample's INCI list.
- DSers mapping status not checked yet (no DSers sign-in on the laptop).

## Suppliers (use the aliexpress.us links)
AliExpress US item IDs = .com ID + 2251799813685248.

| Role | Link | Notes |
|---|---|---|
| Hero stick | https://www.aliexpress.us/item/3256810386540392.html (Lakerain) | 5K+ sold, 4.9. Spec says 18g, so check the size. Lakerain branding is printed on the stick. |
| Hero backup | https://www.aliexpress.us/item/3256810598733159.html | 304 sold, 4.8 |
| Mitt | https://www.aliexpress.us/item/3256805951922355.html | 3K+ sold, 4.7 |
| Heel stick | https://www.aliexpress.us/item/3256809084496799.html (SUYARUN 60% urea) | 10K+ sold, 4.8 |

- **Dropped:** VividHub 1005012396228111, because its photos show The Inkey List's branding. Avoid any listing that names another brand.
- **Prices:** AliExpress shows new-shopper teaser prices ($0.33 to $1.09). Real costs and US shipping must come from DSers.
- **DSers status:** the 4 products are synced. Mapping is not done yet: use Standard Mapping for single items and Bundle Mapping for the bundles and the set.

## Meta setup (decided 16 Nov 2026, in progress)
**Done 16 Nov:**
- Business portfolio **"Fig&oat"**, ID 1024664694005334, owner Victor M. Calvo, business email concierge@figandoat.com. Meta wouldn't accept a lowercase name. The confirmation email to concierge@ still has to be clicked.
- Facebook Page **"Fig&oat"**, Page ID 1396805966855557 (profile URL facebook.com/profile.php?id=61596595771637). It's inside the portfolio, Victor has full access, category Health/beauty, bio "Smoother skin, simply. Body care for rough, bumpy skin. Free US shipping · 30-day guarantee.", and the f&o icon is the profile picture. No cover photo or website yet. Meta Commercial Terms were accepted with the owner's OK.
- **Instagram @fig_and_oat**, IG account ID 17841425570580763. @fig.and.oat and @figandoat were taken. The owner created it in the Instagram app with concierge@figandoat.com; Meta refused to create it from Business Suite. It's a Business account, category Health/beauty, display name "fig & oat". It's in the Fig&oat portfolio, connected to the Fig&oat Page (Instagram messages show in the Business Suite inbox), and has the f&o profile picture and the same bio as the Page.
- **Ad account "Fig&oat US"**, ID 1599111611971111 (act_1599111611971111). Owned by Fig&oat, USD, Eastern Time (America/New_York), created 16 Nov with the owner's OK to Meta Commercial Terms and Advertising policies. Victor has full access. **Payment method: a MasterCard, added by the owner on 16 Nov. Meta set a $50/day spending limit for the new account. Still missing: business name and address, and 2FA.** The Claude Meta Ads connector is signed in to the Rituraj profile, so it can't see this account until it's reconnected as Victor or Victor shares access.
- **Owner admin "kuro ito"** (the owner's Facebook account, invited at the owner's personal Gmail, accepted 16 Nov): full control of the portfolio, plus full access to the Page, @fig_and_oat and Fig&oat US. To use the Claude Meta Ads connector on Fig&oat US, reconnect it as kuro ito; it is currently signed in as Rituraj.

**Plan:**
- **Owner account:** the Facebook profile "Victor", signed in on Chrome on the owner's device "Solar ViC" (Claude in Chrome "Browser 2"). Victor creates and owns the business portfolio, the Page and the ad account. Don't use the Rituraj profile: it runs client work (Eduvaance).
- **Business portfolio:** "fig&oat", business email concierge@figandoat.com.
- **Facebook Page:** "fig&oat", inside that portfolio. Profile picture `fig-and-oat-logo/icon-instagram-1080.png`.
- **Ad account:** USD, time zone America/New_York (both permanent). The owner adds the payment method and turns on two-factor login.
- **Later:** verify figandoat.com in Business settings once it's connected to Shopify. Install the pixel and Conversions API with Shopify's Facebook & Instagram app.
- **Ad Library:** no setup needed. US competitor swipe file done 16 Nov: `research/ad-library-swipe-2026-11-16.md`, also in Drive as a Google Doc. Key finding: Equalize Labs has run a glycolic + salicylic body stick (same format as ours) since Jul 2026, aimed at seborrheic keratoses, so the KP / strawberry-legs angle for a stick is open.

## Sourcing and branding decisions (16 Nov 2026)
- **Packaging: neutral first.** Use listings with no brand printed on the product or box, and add the DSers order note "Dropshipping order: no invoice, no price tags, no promotional material, no logo inserts". Move best sellers to private label (logo sticker, box and insert via an agent) later. This means the **Lakerain hero stick (brand printed on the stick) has to be replaced with an unbranded stick listing**, or kept only as a backup.
- **Legal seller:** the owner is forming a **US LLC soon**. Once it exists, update the Shopify billing address, policies, Meta business info and (later) product labels with the LLC name and address.
- **DSers:** the owner signs in to DSers in Victor's Chrome (Browser 2). Claude then links AliExpress (the owner logs in to AliExpress), vets suppliers, maps products and reads real costs and shipping, sending screenshots before saving.
- **DSers status (checked 16 Nov, signed in as "concierge" in Victor's Chrome):** 3 of 4 products have an AliExpress supplier (Stick → Lakerain, Mitt, Heel). The Set is unmapped. The Stick's bundle variants have **no supplier variant selected and quantity 1**, so mapping is incomplete. Product costs before shipping: Stick $3.45–8.29, Mitt $2.42–2.49, Heel $2.55–4.49. **No AliExpress account is linked in DSers** (Settings → Application Management → AliExpress "Add Accounts"), so orders can't be placed yet. DSers default US shipping is "AliExpress standard" at **about 19 days and about $7.01**, which conflicts with the 7–12 day shipping policy and kills margin on the $12/$16 items. Prefer AliExpress Choice or US-warehouse listings.
- **AliExpress is linked to DSers** (16 Nov): buyer account us2587642184kywae, Default, Connected.
- **Unbranded stick candidate:** https://www.aliexpress.us/item/3256810600031896.html, "Shop910713194 Store". Generic "Glycolic Acid Exfoliating Body Stick" label with no brand name in the photos. **AliExpress Choice, free shipping, USPS, delivery about 7–12 days** (Nov 23–28 quoted on 16 Nov). $4.47 regular price ($1.09 new-shopper teaser), 134 sold, 4.2★ from only 5 reviews, and a new-looking store, so verify with a sample. In DSers search, most high-order sticks are Lakerain-branded, and "The Inkey List" listings are counterfeit-risk (avoid).
- **Mitt supplier checked (16 Nov):** 3256805951922355, New-Journey Store, **Choice, free shipping, ≤9 days, 4.7★ from 267 reviews, 3,000+ sold, unbranded**. Keep it.
- **Heel stick:** SUYARUN 3256809084496799 is Choice, free shipping, 4.8★ from 3,479 reviews, 10,000+ sold, and confirms 60% urea + 2% salicylic. But **SUYARUN is printed on it**, and every urea foot stick in the DSers search is branded (SUYARUN, JUINHOU…). This needs an owner decision.
- **DSers mapping limits:** the current DSers plan only offers Basic and Advanced mapping, **no Bundle Mapping**, so "2 sticks + mitt", "3 sticks + mitt + heel" and the Set can't auto-order several different items. The unbranded stick is saved in the Smooth Stick's DSers favorites; no mapping has been saved yet.
- **16 Nov changes (owner-approved):** bundles simplified because DSers has no Bundle Mapping. The Smooth Stick is now 1 / 2 / 3 sticks at $24 / $42 / $57 (SKUs FO-STICK-1/2/3). All compare-at prices are removed. The Smooth Skin Set is **DRAFT**. Mitt $12 and Heel $16 are unchanged and sold as add-ons.
- **DSers mapping saved (16 Nov):** Smooth Stick → unbranded stick 3256810600031896, variant "Exfoliating Stick", quantities 1/2/3, cost $4.47. Heel Stick → SUYARUN, variant "40g 1" (single stick; check against the sample). **Problem: the stick listing shows "Only 1 left"** (DSers stock 1), so it can't be the main supplier yet. Mitt mapped to **WHITE** (the owner wanted off-white/cream, and WHITE is the closest option).
- **Unbranded stick search (16 Nov):** on AliExpress (sorted by orders) and in DSers search, practically every glycolic body stick with real volume is **Lakerain** (often under generic titles). The rest are "The Inkey List" (counterfeit risk) or tiny listings. No in-stock, reputable unbranded stick was found. Realistic options: Lakerain for the test phase, or private label (agent or Alibaba OEM, MOQ about 500+).
- **Decision 16 Nov: Lakerain for testing.** DSers mapping saved: Smooth Stick 1 / 2 / 3 sticks → Lakerain 3256810386540392 packs "1 pc" / "2 pcs" / "3 pcs" (ships from China Mainland), quantity 1 each. Cost $3.45 (1 pc) to $8.29 (3 pcs), stock 108. **All 3 live products are now mapped** (Stick → Lakerain, Mitt → WHITE, Heel → SUYARUN "40g 1"). Move to private label once a product proves itself.
- **Rough gross margin before ads** (assuming free Choice shipping, Shopify Payments about 2.9% + $0.30): 1 stick $24 → ~$19.6; 3 sticks $57 → ~$46.7; Mitt $12 → ~$8.8; Heel $16 → ~$12.7. To confirm on the first real order.
- **Product photos added (16 Nov, owner-approved):** real supplier photos with the brand visible (Lakerain on the stick, SUYARUN on the heel stick), the stick's ingredient card, and clean white-mitt photos. **No before/after images** (unverified, FTC/Meta risk). Stick 4, Mitt 4, Heel 1, all READY. Every description now ends with "During our launch, products ship in the manufacturer's original packaging." Higgsfield-made visuals may replace these later (owner to confirm). Payload: `shopify-tools/gql/m_photos.graphql` + `v_photos.json`.
- **Published (16 Nov, owner-approved):** Stick, Mitt and Heel are published to **Online Store and Shop** (verified: isPublished true). The Set stays DRAFT and unpublished. `onlineStoreUrl` is still null, probably because the store password is on. The products aren't public until the owner removes the password.
- **DSers default US shipping is still "AliExpress standard" (~19 days, ~$7.01).** It was left unchanged on purpose: the "Selection" (Choice) method names include "For Special Goods" variants that cosmetics may need, and a wrong default could fail orders. Pick the Choice/Selection method per order in DSers (or set the default after the first test order shows which method applies).
- **Store audit:** `research/store-audit-2026-11-16.md` (also a Google Doc in Drive). Biggest blocker: products aren't published to any sales channel.

## Open to-dos
1. Map all 4 products in DSers. Then confirm real cost, US shipping time and margins.
2. Order samples. Check the stick size, label, INCI ingredient list and smell.
3. Add product photos.
4. Rename the theme to "fig&oat".
5. Add a business address to the policies and the store.
6. Connect figandoat.com in Shopify.
7. Set up Meta: pixel and Conversions API (via the Facebook & Instagram app in Shopify), the ad account and creatives.
8. Remove the store password only once everything above is done.

## Files in this folder
- `fig-and-oat-logo/`: every logo variant (SVG and PNG), the favicon, the Instagram icon and the Jost 500 font. The colors are fig #4A1F3D, oat #F3EADB, honey #B08A5B and leaf #7A8450.
- `shop-policies-draft.md`: the shipping and refund policy text.
- `kp-body-kit-validation.md`: the original demand research from 31 Oct.
- `shopify-tools/`: scripts and GraphQL used on the store.
  - `scripts/sx.sh` runs a .graphql file through Shopify CLI (laptop: CLI 5.0.1, logged in 15 Nov; in Git Bash add `/c/Users/DELL/AppData/Roaming/npm` to PATH first).
  - `scripts/sx-token.sh` does the same with an Admin API token in `SHOPIFY_TOKEN` (for cloud sessions, untested).
  - `scripts/products.py` builds the product JSON.
  - `gql/` holds the queries, product payloads and policy payloads.

## Launch plan doc
https://claude.ai/artifact/9ERo44AKpCBd7vjXhax6ui ("KP Body Kit: Launch Plan"). It is private to the **old** Claude account. Before switching, either:
- open it, then use **Share** and add the new account's email with edit access, or
- use the doc's **Export → Markdown** and save the file into this folder.

## Reconnect in the new account
Connectors belong to the Claude account, so none of them move over. Add each one in the new account's Connectors settings:
- **Shopify:** the claude.ai connector failed with "requires authentication" before. What worked was the **Shopify AI Toolkit plugin** plus **Shopify CLI**:
  - Shopify CLI 5.0.0 is installed in `%APPDATA%\npm`. A global update fails with EPERM because npm's prefix points at D:\npm-global. Install with `npm install -g --prefix "%APPDATA%\npm" @shopify/cli@latest`.
  - The CLI login is stored on this Windows user, not in the Claude account. It may still work, so test it with `bash shopify-tools/scripts/sx.sh shopify-tools/gql/state.graphql`.
  - If it doesn't work, log in again with `shopify store auth --store 1ws1tg-iy.myshopify.com --scopes read_products,write_products,read_themes,write_themes,read_content,write_content,read_files,write_files,read_legal_policies,write_legal_policies,read_publications,write_publications`.
- **Meta Ads:** connect it with the Facebook account that owns the fig&oat ad account.
- **Google Drive:** connected as concierge@figandoat.com (15 Nov 2026). **Gmail:** not connected yet. Connect it as concierge@figandoat.com.
- **Claude Docs:** turn it on to read and edit the launch doc once it's shared.

## Rules carried over
- Never enter passwords or payment details, and never buy anything. The owner does those.
- Show the exact command and get a yes before any Shopify login, install, change or publish.
- Publishing a theme and removing the store password are the owner's actions.
