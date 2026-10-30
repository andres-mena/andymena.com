# Andres Mena — personal website

Personal website source for andymena.com, maintained in `andres-mena/andymena.com`. Hosting, domain configuration, and course materials are pending.

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
- `site/LICENSE`: license retained from the reference template.
- `CONTENT_NOTES.md`: local editorial notes, excluded from Git.
- `DNS_SETUP.md`: Name.com access and domain setup instructions.

## Design reference

The source reference is `juancyamin/juancyamin.github.io`, inspected on 2026-10-30. Its academic navigation, serif headings, restrained backgrounds, two-column sections, and teaching hierarchy inform this static adaptation. The Jekyll theme/build system and Juan's personal content are not included. The original MIT license is retained.

The primary blue is `#233393`, with `#3043b4` as a secondary blue; both appear in LAPDE's homepage styles. The supplied landscape is combined with a decorative illustration of an observed and counterfactual trajectory. The illustration represents no empirical result.

## Publication later

When repository access is ready, add a GitHub Pages deployment workflow that uploads **only `site/`**. Configure the custom domain and domain verification before changing DNS. Do not publish the workspace root.
