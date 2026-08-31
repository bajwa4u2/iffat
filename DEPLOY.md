# Deploying iffat.auraplatform.org

The Strategic Member site lives at `iffat/website/` in the codebase. In production it
must resolve at `https://iffat.auraplatform.org/` — the directory is mounted as the
subdomain root, so the codebase path never appears in public URLs.

The deployment shape is identical to the founder site (`personal/bajwa/DEPLOY.md`):
whichever host serves `company.auraplatform.org` today either takes this directory as
an additional subdomain on the same project (rewrite by Host header), or as a separate
project whose publish/output directory is **`iffat/website/`**. No build step — plain
HTML/CSS/JS.

## DNS record

At the DNS provider for `auraplatform.org`, add:

```
Type:   CNAME (or ALIAS / ANAME, depending on provider)
Name:   iffat
Value:  <host-target>            # same target pattern as bajwa/company
TTL:    300 (5 minutes) for cutover; raise to 3600 once stable
Proxy:  Enabled (Cloudflare orange-cloud) if using Cloudflare
```

TLS provisions automatically on the major hosts once the CNAME validates.

## Launch prerequisites (must exist before go-live)

1. **Aura Meetings meeting type.** The booking CTA on the page links to:

   ```
   https://auraplatform.org/i/aura-platform-llc/meet/introduction-discussion
   ```

   This meeting type exists in Aura Meetings (institution `aura-platform-llc`,
   slug `introduction-discussion`). Confirm it resolves before DNS cutover.

2. **Company home live.** The page links to the canonical company home at
   `https://company.auraplatform.org/`; product discovery is handled by the current
   company home and its product routes.

## Verification (after DNS propagates)

```
dig +short iffat.auraplatform.org
curl -I https://iffat.auraplatform.org/
curl -s -o /dev/null -w "%{http_code}  /\n" https://iffat.auraplatform.org/
curl -s https://iffat.auraplatform.org/robots.txt
curl -s https://iffat.auraplatform.org/sitemap.xml
curl -I https://iffat.auraplatform.org/assets/social/og-default.png
```

The root page should return `200`; `robots.txt` should reference the sitemap URL.

## Notes on the path strategy

Internal links are flat (`index.html`, `#role`, `#book`) and resolve relative to the
current page — they work whether the directory is mounted at `/` (production) or under
a subpath (local preview). All cross-site links (company, founder, sibling Strategic
Member, products) are absolute URLs.

The OG/social image is the verified estate card at
`assets/social/og-default.png`; the metadata identifies Iffat as the person
represented by this estate.

The source profile PDF (`iffat/iffat.pdf`) sits **outside** the web root by design.
Do not move it into `iffat/website/` — it is reference material, not published
content.
