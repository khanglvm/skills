# Browser and image verification

## Capture matrix

Use a unique `agent-browser` session. Capture at:

- the reference's exact native aspect ratio when practical;
- desktop: `1440x900` or the project's primary desktop target;
- mobile: `390x844`, `360x844`, and `430x844` when supported;
- an additional wide viewport when the design uses edge-anchored media.

Close the exact session when finished.

## Required pass

1. Load the page and wait for fonts and critical media.
2. Scroll through the whole page once to trigger lazy assets.
3. Return to the top and capture the full page.
4. Capture each section at readable resolution.
5. Capture detail crops for text, cards, gradients, connector endpoints, and focal products.
6. Compare the implementation beside the reference at the same aspect ratio.
7. Record mismatches by section and severity.
8. Fix the highest-impact bounded batch.
9. Repeat captures until no material mismatch remains.

## Detail inspection

Use an image viewer at original resolution. If a panel is dense, generate overlapping crops with ImageMagick when available:

```bash
magick reference.png -crop 50%x55% +repage /tmp/reference-chunk-%02d.png
```

For a targeted crop:

```bash
magick reference.png -crop WIDTHxHEIGHT+X+Y +repage /tmp/reference-detail.png
```

Inspect the reference and capture as full compositions and as matching detail crops. Contact sheets help navigate, but they are not acceptance evidence.

## First-scroll stability

Record the bounding rectangle of major media before scrolling, scroll one viewport, return, and record again. Width and height should remain stable. Also compare screenshots for:

- background-size or focal-point jumps;
- late font swaps that change line breaks;
- image decode that changes aspect ratio;
- scroll animation initial states that reveal a square or partial image before expansion.

## Severity order

Fix in this order:

1. Wrong source content or asset.
2. Missing or hidden primary product/person.
3. Wrong focal crop, geometry, or connector target.
4. Wrong hierarchy, line wrapping, or contrast.
5. Wrong surface, gradient, border, overlap, or icon.
6. Motion and transition polish.

## Evidence-based completion

Completion requires screenshots from every section, not only the sections named in user feedback. If a mismatch remains, identify the section, viewport, visible difference, and reason instead of calling it acceptable.
