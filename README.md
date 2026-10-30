# Andres Mena — personal website

Personal website source for andymena.com, maintained in `andres-mena/andymena.com`. The GitHub Pages workflow is prepared; Pages activation, custom domain configuration, HTTPS, and course materials are pending.

## Preview

Open `site/index.html` in a browser. The website has no build step, external fonts, tracking, or required JavaScript.

Only `site/` is intended for deployment. The purchase confirmation email, source photos, and LinkedIn source file are not website content.

## Structure

- `site/index.html`: biography, research, teaching, software, media.
- `site/cv.html`: public, printable CV.
- `site/assets/Andres_Mena_CV.pdf`: public CV generated from the HTML document.
- `site/assets/style.css`: layout and palette.
- `site/assets/portrait.jpg`: optimized portrait.
- `site/assets/data-landscape.jpg`: supplied landscape photograph.
- `site/assets/podcast-clip.mp4`: interview excerpt, with local poster and optional automatic English captions.
- `site/LICENSE`: MIT license and copyright notice.
- `CONTENT_NOTES.md`: local editorial notes, excluded from Git.
- `DNS_SETUP.md`: Name.com access and domain setup instructions.

## Design

The primary blue is `#233393`, with `#3043b4` as a secondary blue; both appear in LAPDE's homepage styles. The supplied landscape is combined with a decorative illustration of an observed and counterfactual trajectory. The illustration represents no empirical result.

## Publication

In repository Settings → Pages, select **GitHub Actions** as the publishing source. The workflow in `.github/workflows/pages.yml` uploads **only `site/`** on each push to `main`, and can also be run manually from the Actions tab.

Set the custom domain to `andymena.com` in Pages settings, complete domain verification and DNS configuration, and enable **Enforce HTTPS** after the certificate becomes available. Do not publish the workspace root.
