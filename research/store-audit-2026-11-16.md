# fig&oat Shopify store audit (16 Nov 2026)

Read-only check through the Admin API (Shopify CLI on the laptop) plus a look at the live storefront. Nothing was changed.
This access can't read shipping rates, payments, markets/taxes or navigation menus, so those are listed as "check in admin".

## What's there
| Area | Status |
|---|---|
| Store | "Fig & Oat", 1ws1tg-iy.myshopify.com, **Basic plan**, USD, America/New_York, pounds |
| Store email | concierge@figandoat.com (sender and customer contact) |
| Storefront | Password page "Opening soon" with fig&oat logo and newsletter signup ✅ |
| Theme | "fig&oat (draft)" live, with logo, favicon, colors and Jost font. Horizon unpublished. |
| Products | 4, all ACTIVE: smooth-stick (3 bundles), smooth-skin-set, exfoliating-mitt, heel-stick. Titles, descriptions and SEO done. |
| Policies | Shipping and Refund (custom), Privacy and Terms (Shopify templates) |
| Pages | Contact, Your Privacy Choices |
| Sales channels | Online Store, Point of Sale, Shop |
| Apps | DSers, Shopify CLI connector, Messaging, fig&oat ops (cloud access) |
| Files | logos and favicon uploaded |

## What's missing or wrong (blocks launch)
| # | Issue | Fix | Who |
|---|---|---|---|
| 1 | **Products aren't published to any sales channel.** No Online Store URL, so nobody could buy even after the password is removed. | Publish all 4 to Online Store (and Shop). | Claude, with your OK |
| 2 | **No product photos** (0 images on all 4) | Supplier images (cleaned, no foreign branding) for now; own photos and UGC after samples | Claude + you |
| 3 | **DSers not mapped**, so orders can't auto-route to suppliers | Map in DSers (Standard for singles, Bundle for sets) | You sign in; Claude does it |
| 4 | **Real costs and US shipping times unknown**, so margins are unverified | Read them from DSers after mapping | Claude |
| 5 | **Placeholder compare-at prices** ($32/$60/$90/$52/$16/$22): FTC risk | Remove them, or use real bundle savings only | Claude, with your OK |
| 6 | **Variant weights all 0 lb** | Set real weights from the supplier (or keep free-shipping-only rates) | Claude |
| 7 | **No business address**: billing address has only ZIP 33143 (Miami), and policies have none | Decide the legal entity and address (see questions) | You |
| 8 | **Domain figandoat.com not connected** | Connect in Settings → Domains (DNS at your registrar) | You + Claude |
| 9 | **Navigation menu and collections:** only the default "Home page" collection | Create "Shop all" and "Bundles" collections; check header/footer menus | Claude |
| 10 | **Shipping rates, payments (Shopify Payments / PayPal), taxes**: can't be read with current access | Check in admin: free US shipping rate, payouts set up, sales tax registrations | You (payments); Claude can guide |
| 11 | **Meta pixel and Conversions API** not installed | Install "Facebook & Instagram" app → connect to Fig&oat portfolio, dataset and catalog | You approve; Claude guides |
| 12 | **Theme name** still "fig&oat (draft)" | Rename to "fig&oat" | Claude, with your OK |

## Order to do it in
1. Pick suppliers and **map in DSers**, so real cost and shipping time are known (blocks pricing and guarantee decisions).
2. Fix prices (compare-at), weights, photos and descriptions with the real supplier details.
3. Publish products, then add collections and menus.
4. Business address and entity, then put it into the policies.
5. Payments, shipping rate and taxes check.
6. Domain.
7. Facebook & Instagram app (pixel, CAPI, catalog).
8. Order samples, film creatives.
9. Remove the password (your action) and run a paused campaign for approval.
