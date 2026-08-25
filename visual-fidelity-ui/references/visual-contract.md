# Visual contract

Create a contract for every reference panel before implementation. This prevents a large image from being reduced to a vague impression.

## Section record

Use this structure:

```text
Section:
Reference file and native size:
Authoritative copy source:
Primary customer takeaway:
Primary subject:
Subject bounding area (x/y/w/h as %):
Background anchor and fallback color:
Content bounding area (x/y/w/h as %):
Heading size/weight/line count/color:
Body size/weight/line count/color:
Chip/icon/button geometry:
Cards, borders, radii, gradients, and z-order:
Small details and semantic targets:
Desktop-to-mobile transformation:
Entry/exit transition:
Acceptance screenshots:
```

Percent coordinates are relative to the native reference canvas, not a thumbnail.

## Binding versus adaptable

Binding:

- source copy and locale;
- section order and customer message;
- subject identity, product color, and meaningful variant;
- focal geometry and product visibility;
- typography hierarchy and intended line grouping;
- surface palette, gradients, borders, radii, and stacking;
- connector meaning and endpoint;
- icon meaning and state.

Adaptable:

- section height when needed for responsive content;
- exact whitespace at unsupported aspect ratios;
- animation implementation, provided it preserves the reference state;
- mobile stacking, provided hierarchy and meaning remain intact.

## Content-source gate

When a spreadsheet, CMS, document, or annotation file controls copy:

- map exact rows or fields to exact sections;
- preserve punctuation, units, qualifiers, and footnotes;
- verify both locales independently;
- treat missing or conflicting cells as blockers;
- search the rendered page for every mapped source line after implementation.

Do not generate marketing claims to fill gaps.

## Visual review questions

Ask for every section:

1. What should the customer notice first?
2. Is that subject visible immediately without scrolling or waiting?
3. Does the crop show the mechanism or benefit named by the copy?
4. Does the fade protect text without hiding the product?
5. Do the text scale, weight, and line breaks express the same hierarchy?
6. Do cards, icons, and comparisons preserve their intended positive/negative emphasis?
7. Does the next section feel intentionally connected rather than hard-split?
