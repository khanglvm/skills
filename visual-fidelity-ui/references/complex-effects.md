# Complex visual effects

## Semantic annotation connectors

Do not approximate connector lines with independent CSS borders. Model them as geometry.

1. Identify each label's semantic target in the source image.
2. Measure the target coordinate on the native image.
3. Convert it to the rendered image coordinate after `object-fit` or background cropping.
4. Draw one responsive SVG overlay with `viewBox` coordinates matching the section.
5. Use `polyline` or `path` for multi-segment routes and `stroke-dasharray` for dashed lines.
6. Put terminal dots at the physical target and optional label-side dot at the text edge.
7. Keep label layout independent from the connector path.

For `object-fit: cover`, compute the visible transform:

```text
scale = max(containerWidth / imageWidth, containerHeight / imageHeight)
renderedWidth = imageWidth * scale
renderedHeight = imageHeight * scale
offsetX = (containerWidth - renderedWidth) * objectPositionX
offsetY = (containerHeight - renderedHeight) * objectPositionY
screenX = sourceX * scale + offsetX
screenY = sourceY * scale + offsetY
```

Recalculate on resize. A line is wrong if it lands on a decorative elbow, transparent housing, or empty background instead of the named component.

## Background continuity

When an image occupies only part of a wide section:

- sample the source edge color and use it as the section fallback;
- anchor the product side explicitly with `background-position` or a positioned `<img>`;
- extend a short, directional gradient from the image edge into the solid area;
- keep the pure text zone outside the partially transparent blend;
- verify ultra-wide screens for exposed edges.

Prefer a positioned `<img>` with `object-fit: cover` when precise subject anchoring matters. Use `object-position` or `transform-origin` derived from the source focal point.

## Layered comparison cards

- Give each card an explicit width, background, opacity, and z-index from the reference.
- If the leading card visually covers the trailing card, keep it opaque and above the trailing card in all states.
- Apply muted overlays to negative/comparison cards without muting the positive card.
- Place check/cross icons inside a safe inset; do not rely on overflow clipping.
- Hover may add small translation or contrast, but must not change stacking order.

## Gradient text and chips

- Treat chip dimensions as independent tokens; do not derive them from headline `clamp()` values.
- Use a single rounded element with border and background gradient. Avoid pseudo-elements that create visible end caps unless the reference contains them.
- For gradient text, use `background-clip: text` with a solid-color fallback.
- Match gradient direction, stop positions, and contrast at both ends; do not use a generic left-to-right highlight.

## Stable media geometry

- Set intrinsic `width` and `height` or `aspect-ratio` before media loads.
- Keep initial and animated states at the same width, height, crop, and background size.
- Animate opacity, clip-path, mask position, or transform instead of layout dimensions.
- Preload hero media and the next likely above-the-fold asset.
- Test before and after the first scroll to catch delayed intrinsic-size or font changes.
