# Attribution

The Vietnamese layer (`languages/vi.md`), the medium cards (`domains/`) and the linter patterns (`patterns/vi-tells.json`) combine ideas from five MIT-licensed repositories, public style guides, practitioner articles and a small corpus of human news text. Most material is re-expressed. Where a short example sentence or a phrase list was kept close to its source, the source is named below and its MIT notice is reproduced at the end.

## Upstream

**blader/humanizer** (vendored unmodified as `upstream/humanizer.md`, with its notice in `upstream/LICENSE`). Copyright (c) 2025 Siqi Chen. MIT. The workflow, voice rules and pattern numbers (§1 to §26) that the layers extend and cite.

## Repositories mined

**cthpAiden/humanizer-vi.** Copyright (c) 2026 Phuc Chau. MIT.
- Kept close to the source: the VI-12 pair (*Đây là một giải pháp ...* → *Giải pháp này giúp bạn làm việc hằng ngày tốt hơn*), the VI-33 pair (*Công ty thành lập năm 2010 ...*), the bad side of VI-10.
- Re-expressed: tell families for macro openers, glue words, *một cách* + adjective, email and support calques, set-piece verbs, the "do not confuse with" notes, the rule against invented decoration.

**longhang2004/vietnamese-humanizer.** Copyright (c) 2026 Vietnamese Writing Skills contributors. MIT.
- Kept close to the source: the VI-11 pair (*Nhóm tiến hành việc gửi bản nháp ...*), the VI-14 pair (*mở khóa tiềm năng tìm xu hướng ...*), the VI-31 bad example (*Nhóm đổi lịch giao hàng và cách tính phí ...*), the shortened VI-04 example (*mở tệp 2 GB trong 4 giây*).
- Re-expressed: stable pattern IDs with families, density aggregation and minimum counts, the no-change outcome, the four intervention levels (keep, rewrite, comment, author decides), regex ideas for `đóng vai trò ... trong việc`, `được ... bởi`, `thông qua việc`, `thực hiện việc`, and the false-positive notes for *tận dụng* and *liền mạch*.

**cuongducle/viet-humanize.** Copyright (c) 2026 cuongducle. MIT.
- Re-expressed only: the conservative stance (natural is not the same as casual), the before/after verify step for numbers, URLs and code, "flags are prompts, not orders", and "do not claim a check you did not run". Its AI and human corpus files were used read-only to test the linter; none of that text is included.

**trussary/vietnamese-language-skill.** Copyright (c) 2026 vietnamese-language-skill contributors. MIT.
- Kept close to the source: settled UI strings and CTA calque pairs (*Học thêm → Tìm hiểu thêm*, *Lấy báo giá → Nhận báo giá*), the two code-review example sentences in `domains/workplace.md`, the internal-term list in `domains/ui-copy.md`.
- Re-expressed: the register matrix by medium, one register per document, *chúng tôi* versus *chúng ta*, the impersonal register for specs and runbooks, the keep/Vietnamise term split by formality, ICU `other`-only plurals, NFC and tone-mark consistency, the Hán-Việt prestige axis, the Luật Quảng cáo superlative check.

**haunguyendev/humanizer-vi.** Copyright (c) 2025 Siqi Chen; Copyright (c) 2026 haunguyendev. MIT.
- Kept close to the source: the shape of the VI-21 example (*12 lớp tập huấn, góp phần ...*).
- Re-expressed: the Nghị định 30 do-not-flag list (thể thức, *Căn cứ*, *Nơi nhận*, signature marks), doubled synonyms (*triển khai thực hiện*), chained *của* and *và/hoặc*, and the over-edit guard: rewrite a sentence only with two tells, keep a sentence with one tell and a concrete fact.

## Style guides and official texts

- Microsoft Vietnamese Localization Style Guide: https://download.microsoft.com/download/b/f/e/bfecb1b4-21ab-48fd-a48c-c2471b026f8f/vie-vnm-StyleGuide.pdf (sentence case, *Không ... được* errors, short everyday words, number format, no comma before *và/hoặc*, subject-dropping UI fragments).
- Mozilla Firefox Vietnamese strings: https://github.com/mozilla-l10n/firefox-l10n (button forms; calqued error fillers noted as cautions).
- Nghị định 30/2020/NĐ-CP, Điều 8 and Phụ lục I, VI: https://luatvietnam.vn/hanh-chinh/nghi-dinh-30-2020-nd-cp-ve-cong-tac-van-thu-moi-nhat-181212-d1.html (capitals, dates in official documents).
- Quyết định 240/QĐ (1984), Bộ Giáo dục: https://thuvienphapluat.vn/van-ban/Giao-duc/Quyet-dinh-240-QD-nam-1984-chinh-ta-thuat-ngu-tieng-Viet-sach-giao-khoa-bao-van-ban-nganh-giao-duc-216818.aspx (foreign proper names).
- Luật Quảng cáo 16/2012/QH13, Điều 8 khoản 11 (regulated superlatives), as summarised in the trussary repository.

## Practitioner and research sources

- Cao Xuân Hạo, "Suy nghĩ về dịch thuật": https://www.caoxuan.com/article.php?Fl=archives%2Fcxhao_translation_doc (the write-from-meaning step).
- Brands Vietnam, "Dấu hiệu nhận biết nội dung được viết bởi AI" (2025-09-23): https://help.brandsvietnam.com/vi/article/dau-hieu-nhan-biet-noi-dung-duoc-viet-boi-ai-3zy07d
- Phạm Mỹ, "Mùi AI", Báo Văn Nghệ (2026-02-23): https://baovannghe.vn/mui-ai-26802.html (English-centred logic, imported imagery, set-piece greetings).
- Tân Phát Digital checker: https://tanphatdigital.com/vi/tools/kiem-tra-van-ban-ai (density over presence, false-positive test on news).
- Upcontent: https://upcontent.vn/kiem-tra-van-ban-ai/ (name-swap test).
- Finhay: https://www.finhay.com.vn/meo-dung-chatgpt-khong-bi-van-mau-robotic (hollow word list).
- Facebook group post, Nghiện AI: https://www.facebook.com/groups/aiartworksvn/posts/4450406765172173 (split contrast, staccato fragments, confession arc; the two short VI-04 and VI-06 examples paraphrase it).
- Workplace and product samples from the R2 report: Tiki Engineering, Viblo, Cybozu Vietnam, easywebhub GitHub issues, MoMo, Base.vn and Haravan release notes (links in `references/sources.md`).

## Human news corpus

Fourteen articles published before November 2022 (VnExpress, Znews, VietNamNet, Tuổi Trẻ, Thanh Niên, Lao Động, Nhân Dân), listed in `references/sources.md`. They were used for counts and linter calibration only and are not part of this repository. The skill quotes no more than a few words from any of them.

## Maintainer's own material

Rules and examples from the maintainer's own writing guides and corrections, including the VI-32 example pair, which is his own rewrite direction. His personal preferences are not stored here; the router loads them from Knowledge at run time.

## MIT permission notice

Applies to each copyright line above:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
