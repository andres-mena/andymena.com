# Andres Mena — personal website

Personal website published at andymena.com, maintained in `andres-mena/andymena.com`. Course materials can be added as they become available.

## Preview

Open `site/index.html` in a browser. The website has no build step, external fonts, tracking, or required JavaScript. Optional animations use a locally hosted copy of Motion 14.9.0.

Only `site/` is intended for deployment. The purchase confirmation email, source photos, and LinkedIn source file are not website content.

## Structure

- `site/index.html`: biography, research, teaching, software, media.
- `site/cv.html`: redirect for the previous CV page address.
- `site/assets/Andres_Mena_CV.pdf`: original PDF supplied by the owner (`CV_Mena_2027.pdf`); opened directly by the CV navigation link.
- `site/assets/style.css`: layout and palette.
- `site/assets/animations.js`: intro, scroll, stagger, and illustration hover animations; respects reduced motion and print preferences.
- `site/assets/vendor/motion-14.9.0.js`: pinned Motion browser library, with its MIT license alongside it.
- `site/assets/portrait.jpg`: optimized portrait.
- `site/assets/data-landscape.jpg`: supplied landscape photograph.
- `site/assets/podcast-clip.mp4`: interview excerpt, with local poster and optional automatic English captions.
- `site/LICENSE`: MIT license and copyright notice.
- `CONTENT_NOTES.md`: local editorial notes, excluded from Git.
- `DNS_SETUP.md`: Name.com access and domain setup instructions.

## Design

The primary blue is `#233393`, with `#3043b4` as a secondary blue; both appear in LAPDE's homepage styles. The supplied landscape backs a four-stage vector illustration: population with unknown effects, treatment and control, heterogeneous effects, and targeting decisions. The illustration represents no empirical result. `site/assets/policy-learning.svg` is a standalone version of the diagram.

## Publication

In repository Settings → Pages, select **GitHub Actions** as the publishing source. The workflow in `.github/workflows/pages.yml` uploads **only `site/`** on each push to `main`, and can also be run manually from the Actions tab.

Set the custom domain to `andymena.com` in Pages settings, complete domain verification and DNS configuration, and enable **Enforce HTTPS** after the certificate becomes available. Do not publish the workspace root.
