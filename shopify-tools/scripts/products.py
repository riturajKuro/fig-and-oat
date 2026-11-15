import json, sys

OUT = sys.argv[1]

FAQ_SHIP = ("<h3>Shipping</h3><p>Free US shipping. Orders ship in 1–3 business days and arrive in "
            "7–12 business days, with tracking.</p>")
GUARANTEE = ("<h3>30-day smooth-skin guarantee</h3><p>Use it for 30 days. If you don't love how your "
             "skin feels, email us for a full refund. Keep the product.</p>")

products = [
    {
        "handle": "smooth-stick",
        "title": "The Smooth Stick — Glycolic Exfoliating Body Stick",
        "productType": "Body exfoliant",
        "tags": ["hero", "body", "exfoliant", "strawberry legs", "rough bumpy skin"],
        "seo": {"title": "The Smooth Stick | Glycolic Body Stick for Rough, Bumpy Skin | fig&oat",
                "description": "Swipe on, leave on. A glycolic acid body stick that smooths rough, bumpy skin "
                               "on legs, arms and the back of the neck. Free US shipping, 30-day guarantee."},
        "descriptionHtml": (
            "<p><strong>Rough, bumpy skin on your legs or arms? Swipe on. Leave on. Feel the difference.</strong></p>"
            "<p>The Smooth Stick is a no-mess glycolic acid body exfoliant in a twist-up stick. It gently loosens "
            "the dead skin that makes skin look dotted and feel rough, so legs, arms and the back of the neck "
            "look and feel visibly smoother.</p>"
            "<h3>Why you'll like it</h3><ul>"
            "<li>Visibly smoother, softer skin with regular use</li>"
            "<li>Helps the look of “strawberry legs” and rough, bumpy patches</li>"
            "<li>No scrubbing, no sticky hands, no mess: swipe and go</li>"
            "<li>Travel-friendly solid stick</li></ul>"
            "<h3>How to use</h3><ol>"
            "<li>On clean, dry skin, swipe 2–3 times over rough areas.</li>"
            "<li>Leave on. Follow with moisturizer if you like.</li>"
            "<li>Start every other evening, then build to daily.</li>"
            "<li>Use sunscreen on treated areas during the day.</li></ol>"
            "<h3>Good to know</h3><p>Not for broken, irritated or freshly shaved skin. A light tingle is normal; "
            "stop if irritation occurs. Patch test first. For external use only.</p>"
            + FAQ_SHIP + GUARANTEE),
        "option": "Bundle",
        "variants": [
            ("1 stick", "24.00", "32.00", "FO-STICK-1"),
            ("2 sticks + free mitt", "44.00", "60.00", "FO-STICK-2M"),
            ("3 sticks + mitt + heel stick (best value)", "59.00", "90.00", "FO-STICK-3MH"),
        ],
    },
    {
        "handle": "smooth-skin-set",
        "title": "The Smooth Skin Set — Stick, Mitt & Heel Stick",
        "productType": "Body care set",
        "tags": ["set", "bundle", "body", "strawberry legs", "rough bumpy skin"],
        "seo": {"title": "The Smooth Skin Set | 3-Step Routine for Rough, Bumpy Skin | fig&oat",
                "description": "Exfoliate, smooth and soften: The Smooth Stick, Korean exfoliating mitt and "
                               "heel stick in one routine. Free US shipping, 30-day guarantee."},
        "descriptionHtml": (
            "<p><strong>The whole routine for smoother legs, arms and heels.</strong></p>"
            "<h3>What's inside</h3><ol>"
            "<li><strong>The Exfoliating Mitt</strong>: buffs away dead skin in the shower, 1–2 times a week.</li>"
            "<li><strong>The Smooth Stick</strong>: glycolic acid swipe-on for rough, bumpy skin.</li>"
            "<li><strong>The Heel Stick</strong>: urea + salicylic acid balm for rough heels and elbows.</li></ol>"
            "<h3>Your routine</h3><ul>"
            "<li>Shower: mitt on damp skin, light pressure, 1–2 times a week.</li>"
            "<li>Evening: Smooth Stick on legs and arms.</li>"
            "<li>Night: Heel Stick on heels and elbows only.</li></ul>"
            "<p>Not for broken or irritated skin. Patch test first. Use sunscreen on treated areas.</p>"
            + FAQ_SHIP + GUARANTEE),
        "option": "Set",
        "variants": [("Stick + mitt + heel stick", "39.00", "52.00", "FO-SET-3")],
    },
    {
        "handle": "exfoliating-mitt",
        "title": "The Exfoliating Mitt — Korean Viscose Body Mitt",
        "productType": "Body tool",
        "tags": ["tool", "mitt", "exfoliant", "body"],
        "seo": {"title": "The Exfoliating Mitt | Korean Viscose Body Scrub Mitt | fig&oat",
                "description": "A Korean-style viscose mitt that buffs away dead skin in the shower. "
                               "Reusable. Free US shipping."},
        "descriptionHtml": (
            "<p><strong>Watch the dead skin roll away.</strong></p>"
            "<p>A Korean-style viscose exfoliating mitt for a deep, satisfying body buff in the shower. "
            "Pairs with The Smooth Stick for visibly smoother skin.</p>"
            "<h3>How to use</h3><ol>"
            "<li>Soak in warm water for 10 minutes so skin softens.</li>"
            "<li>Wet the mitt and rub in long strokes with light pressure.</li>"
            "<li>Rinse, then moisturize. Use 1–2 times a week.</li>"
            "<li>Rinse the mitt and hang to dry. Replace every 2–3 months.</li></ol>"
            "<p>Skip broken, sunburned or freshly shaved skin.</p>" + FAQ_SHIP),
        "option": "Pack",
        "variants": [("1 mitt", "12.00", "16.00", "FO-MITT-1")],
    },
    {
        "handle": "heel-stick",
        "title": "The Heel Stick — Urea Balm for Rough Heels & Elbows",
        "productType": "Foot care",
        "tags": ["heels", "urea", "foot care", "elbows"],
        "seo": {"title": "The Heel Stick | Urea + Salicylic Balm for Rough Heels | fig&oat",
                "description": "A swipe-on urea and salicylic acid balm that softens rough, dry heels and elbows. "
                               "Free US shipping, 30-day guarantee."},
        "descriptionHtml": (
            "<p><strong>Soft heels, no greasy hands.</strong></p>"
            "<p>A twist-up balm with urea and salicylic acid that softens thick, rough, dry skin on heels and "
            "elbows. Swipe on at night and wake up to smoother, softer skin.</p>"
            "<h3>How to use</h3><ol>"
            "<li>Swipe onto clean, dry heels or elbows at night.</li>"
            "<li>Wear socks for best results.</li>"
            "<li>Use nightly until smooth, then 2–3 times a week.</li></ol>"
            "<p>For heels and elbows only. Not for face, legs or broken skin.</p>" + FAQ_SHIP + GUARANTEE),
        "option": "Pack",
        "variants": [("1 stick", "16.00", "22.00", "FO-HEEL-1")],
    },
]

for p in products:
    v = {"input": {
        "handle": p["handle"], "title": p["title"], "descriptionHtml": p["descriptionHtml"],
        "vendor": "fig&oat", "productType": p["productType"], "tags": p["tags"], "status": "DRAFT",
        "seo": p["seo"],
        "productOptions": [{"name": p["option"], "values": [{"name": n} for n, *_ in p["variants"]]}],
        "variants": [{
            "optionValues": [{"optionName": p["option"], "name": n}],
            "price": price, "compareAtPrice": cmp, "sku": sku,
            "inventoryPolicy": "CONTINUE", "taxable": True,
            "inventoryItem": {"tracked": False, "requiresShipping": True, "sku": sku},
        } for n, price, cmp, sku in p["variants"]],
    }}
    v["input"]["variants"] = [{k: val for k, val in x.items() if k != "sku"} for x in v["input"]["variants"]]
    json.dump(v, open(f"{OUT}/prod_{p['handle']}.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(p["handle"], len(p["variants"]))
