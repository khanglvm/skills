---
name: visual-fidelity-ui
description: Implement or audit responsive frontend UI against supplied screenshots, mockups, design panels, or an existing reference page when close visual matching matters. Use for screenshot-to-code, design-to-code, pixel-fidelity corrections, and visual-regression repair, especially when the work includes exact image crops, focal subjects, layered gradients, overlapping cards, annotation connectors, or small visual details. Do not use for open-ended greenfield design without a binding visual reference.
---

# Visual Fidelity UI

Treat the supplied design as a visual contract, not a moodboard. Preserve its product story, focal geometry, hierarchy, and small details while implementing real, responsive, semantic UI.

## Establish source authority

Before editing:

1. Open every supplied design, copy source, asset folder, and note source successfully.
2. Record which source controls copy, section order, imagery, and visual composition.
3. Inspect the original-resolution files, not only thumbnails or spreadsheet previews.
4. Map every design panel to its rendered section and authoritative copy.
5. Stop and report the exact blocker if a required source cannot be accessed or mapped.

Never invent, paraphrase, translate, shorten, or substitute authoritative content. Never silently use a visually similar asset when the specified asset exists.

## Build a section contract

Read [visual-contract.md](references/visual-contract.md) before implementation. For each section, record:

- primary subject and intended customer takeaway;
- exact asset, focal point, crop, and background anchor;
- heading, body, label, and footnote typography;
- layout, spacing, radii, borders, surfaces, gradients, and overlaps;
- small details such as icons, connector endpoints, dividers, and chips;
- responsive transformation and reduced-motion behavior;
- transition into the adjacent sections.

Section height may adapt responsively. The internal composition, semantic emphasis, product visibility, and source content remain binding.

## Inspect before coding

View each reference in two modes:

1. Full composition at native aspect ratio.
2. Readable detail crops for typography, controls, overlaps, connector endpoints, and product geometry.

For dense boards, divide the image into overlapping chunks. Do not approve details from a compressed contact sheet. Measure proportions and coordinates relative to the original image so the implementation can scale predictably.

## Implement the composition

- Build semantic HTML/CSS/JS or framework-native components; never ship the reference image as the webpage body.
- Preserve the project's existing font family, design tokens, header, footer, accessibility, and navigation unless the reference explicitly replaces them.
- Position media around the focal subject. Avoid generic `center center` crops when the subject is intentionally offset.
- Reserve media geometry before load. Do not animate width, aspect ratio, or background size from an incorrect initial value.
- Use gradients and overlays to support legibility without obscuring the product or meaningful people.
- Keep fixed-size visual elements, such as reference chips and status icons, independent from fluid headline sizing.
- Do not invent decorative ordinal labels such as `01 / 03`, `01—03`, section numbers, step counters, or slide indices to make a page feel editorial. Include them only when an authoritative source requires them or they communicate real sequence, position, progress, or navigation state.
- Implement overlaps with explicit stacking order. Hover and entrance motion must not reverse the reference layering.
- Use fluid type and spacing only inside bounded ranges that preserve the reference's line breaks and hierarchy.

Read [complex-effects.md](references/complex-effects.md) when the reference uses connectors, background continuity, layered cards, masks, blends, or complex crops.

## Verify in a browser

Read [verification.md](references/verification.md) before declaring completion. Use `agent-browser` by default when available.

At minimum:

1. Capture the exact reference viewport or aspect ratio.
2. Capture a common desktop viewport and multiple mobile widths.
3. Traverse the page first so lazy media is loaded.
4. Capture the full page and every section separately.
5. Compare full compositions and detail crops side by side.
6. Test first load and first scroll for geometry shifts or background flicker.
7. Fix a bounded batch of mismatches, recapture, and repeat.

Judge screenshots, not DOM metrics alone. A correct element box can still show the wrong crop, contrast, focal point, or connector endpoint.

## Hard failure conditions

Do not mark the work complete when any of these remain:

- required source content or media was guessed;
- the product or primary person is hidden, cropped irrationally, or covered by a fade;
- a connector terminates in empty space or points to the wrong mechanism;
- a wide viewport exposes an uncovered background edge;
- text weight, wrapping, contrast, or chip sizing materially drifts from the reference;
- decorative indexing or counters were added without source authority or functional meaning;
- overlapping cards have the wrong z-order, opacity, or merge behavior;
- media changes size or crop on first scroll;
- only a thumbnail, DOM snapshot, or single viewport was reviewed;
- a section was skipped because it was not mentioned in feedback.

## Completion evidence

Report:

- sources opened and mapped;
- viewports tested;
- full-page and section capture locations;
- notable responsive adaptations;
- any remaining visual deviation, with an honest reason.
