# Vietnamese layer

Load for any Vietnamese text; the upstream workflow still runs in full. The writer's own rules (project docs, Knowledge preferences) win. A reviewer's wording is direction, not approved copy; never turn one correction into a word ban.

This is the drafting core. `languages/vi-catalogue.md` holds every tell's forms, examples and *Keep* exceptions, for review, rewrites and linter findings.

## 1. Write from meaning

Word for word is the surest way to translate wrong (Cao Xuân Hạo). Whenever the source or your reasoning is in English, keep the meaning and say it as a Vietnamese writer would.

1. With the source closed, write one plain line per paragraph: who does what, to what, and why this reader cares.
2. Pick the medium's row in the register matrix (section 4).
3. Write actor, active verb, concrete object; time or place first in news-like text ("Chiều 1/11, ..."). Carry logic inside the sentence with *sau khi, khiến, nên, vì, để, nhưng, trong khi, nghĩa là*. In technical text the system or step can be the subject; Vietnamese may drop a subject English needs.
4. Reopen the source. Every number, name, date, condition and hedge (*có thể, chưa, chỉ, vẫn, đã, mới*) survives; nothing new appears. Editions may differ in structure and examples, never in facts, ownership or uncertainty.

Done when every paragraph traces to a line from step 1 and no sentence keeps English shape (VI-10, VI-12, VI-15; no adjective before its noun or clause order copied from the source).

## 2. When to act: clusters

One tell is weak evidence. Score each paragraph: strong 3, medium 2, weak 1. Strengths live only in `patterns/vi-tells.json` (manual entries too). For a tell it does not rate, judge: strong when it bends meaning, register or a claim, weak for a lone connector or glue word, medium otherwise.

Act on a strong tell at once, a medium one when a second tell shares the paragraph or it repeats, a weak one only inside a cluster. Rewrite a paragraph scoring 3 or more; when two tells hit one sentence, rewrite it once from its meaning. Return natural input nearly unchanged and say so. When a fix would change meaning, register or a claim, comment to the author instead.

## 3. Tell families

- **Framing (VI-01 to VI-06):** open on the content and end on the last fact, with no context opener, announcement, template closer, *không phải X mà là Y*, self-announced importance or slogan fragment.
- **Translationese (VI-10 to VI-17):** native order (*do X làm, được X làm*), the bare verb instead of *tiến hành, việc, sự*, *một, các, những* only to count, no *một cách*, the plain meaning of a metaphor or calque, native email formulas, English dev terms in dev text.
- **Inflation (VI-20 to VI-24):** facts instead of praise or significance riders, one word instead of a synonym pair, a named source for every number or ranking, details only this recipient fits.
- **Glue and rhythm (VI-30 to VI-34):** logic inside the sentence, one target per pronoun, one thought per sentence joined with real connectives, varied openers, prose instead of listicle shape.
- **Register (VI-40 to VI-43):** one address set, honorifics only when known, neutral Vietnamese without faked casualness or chatbot wrappers.
- **Mechanics (VI-50 to VI-56):** section 5, the dash rule in section 3a, and *Không X được* for UI errors.

## 3a. Upstream patterns in Vietnamese

Patterns no tell heading names (others: end of the catalogue):

- §10 and §21 do not apply: Vietnamese press and localised software use “ ” (follow the target file).
- §11: Vietnamese drops subjects natively, so flag only a hidden actor the reader needs.
- §8: no clause dash. The spaced hyphen marks a role after a name, a quote's attribution and photo credits in news-style copy or where the writer's sample uses it; elsewhere use a comma, colon or parentheses. Compounds (*kinh tế - xã hội*), the Tiêu ngữ and ranges keep their hyphen.

## 4. Register matrix

Pick a row before writing; one address set per document, a channel override (Zalo notice) excepted. Unless a row says otherwise: no pronouns, no particles.

- Jira / Outline comment: subject-free; the team's saved protocol.
- Team chat: tag, then no name; writer *mình* or none; *nhé, nghe* ok; one action per line.
- PR, code review: address the change; writer *mình* or none ("Chỗ này nên tách hàm riêng.").
- RFC, design doc, runbook, postmortem: system as subject; runbook steps as bare imperatives.
- README, tutorial, help article: *bạn*; project voice; gloss a term once.
- UI strings, errors: *bạn*, sparingly.
- Release notes: none or *bạn*.
- Personal blog article: *bạn* sparingly, writer *mình*; particles in column voice only.
- Landing (SaaS, studio, consumer): *bạn*, writer *chúng tôi*.
- Landing (bank, insurance, real estate), status page: *quý khách*, writer *chúng tôi*; plain words on status pages.
- B2B email, known relation: *anh/chị* and *ạ* only when known, writer as the relation sets; otherwise neutral, no pronoun.
- Official document (NĐ 30/2020): *Kính gửi:* + body, the agency writes; every thể thức element kept.
- News-style report: full name with (age, place) once, then honorific + given name; writer *phóng viên*; *tôi* is for columns.

## 5. Mechanics

**Numbers.** Thousands take a period, decimals a comma: 1.526; 5,25 cm; 3,6 triệu đồng/tháng. Prose uses scale words (2,5 tỷ đồng), tables full digits; never mix them in one column. VND has no decimals: *100.000 ₫* or *đồng*. Counts and measures take digits (4 người, 7 km, 185 m²), though narrative may spell a small number. One unit spacing per document (*24 giờ*, *1.000 đ/phút*).

**Dates and times.** dd/mm/yyyy, one form per document (29/04/2026 or 29/4/2026); drop a clear year (19/7); part of day first (*Sáng 5/8*); *tháng 1/2026*; 24-hour time (14:30). In prose, *Ngày 15/10/2021, ...*, not *Vào ngày ..., một ...*. Official documents: *Hà Nội, ngày 05 tháng 3 năm 2020*, with a leading zero for days below 10 and months 1 and 2.

**Punctuation.** No space before . , ; : ? or !, one after; no comma before *và/hoặc* in a list. Brackets carry age and place (*31 tuổi, quê Hậu Giang*). Ellipsis sparingly; *?!* only in chat. Quotes may flag a borrowed or figurative word; semicolons separate parallel items in prose.

**Capitals.** Sentence case for titles, headings, buttons and menus. Institutions capitalise each content word (*Bộ Tài nguyên và Môi trường*). A role: capitalised in official copy (*Thủ tướng Chính phủ*), lowercase after a name in everyday copy; one choice per document. Products keep their casing. ALL CAPS only for NĐ 30 elements (Quốc hiệu, document type, *MẬT, KHẨN*) or a brand guide requiring it.

**Spelling and encoding.** Emit NFC. One tone-mark style per document (*hòa/hoà, thủy/thuỷ*), following the project's files, else the old style (*hòa, thủy, hủy*); the same for *kỳ/kì*. Slugs, identifiers, branch names and commit subjects stay ASCII.

**English terms.** One term per concept within a document.

- English in dev prose, chat, PR and Jira: commit, push, merge, pull request, MR, branch, build, deploy, release, rollback, hotfix, pipeline, job, image, registry, repo, staging, production, bug, fix, test (*chạy test*), review, task, ticket, sprint, backlog, Definition of Done, endpoint, timeout, log, API, ID, code (*sửa code*, not *sửa mã*), agent, harness, CLI, PRD, QA, QC, BE Dev, PM, engineer, developer.
- Vietnamese in UI and consumer copy: tệp or tập tin (file), thẻ (tab), Cài đặt, Tải xuống, Tải lên, sao lưu, đồng bộ, khôi phục, Đăng nhập, Đăng xuất, mật khẩu, tài khoản, lỗi (a bug as users see it), Tìm kiếm, Thử lại, Hủy.
- Both live, by formality: server / máy chủ (non-engineers), database / cơ sở dữ liệu (specs), cache / bộ nhớ đệm (published docs), deploy / triển khai (gloss, corporate text), test / kiểm thử (*kết quả kiểm thử* in QA reports), source code / mã nguồn (formal company story only).

A tutorial or article glosses an English term once ("CI/CD, tức tích hợp và triển khai liên tục"), then uses it bare; chat, Jira and handoffs never gloss. Name a document by what it is (PRD, *tài liệu kỹ thuật*); *trang* means a literal page.

## 6. Leave these alone

Every *Keep* in the catalogue holds. Also leave:

- A single medium or weak tell, above all one next to a concrete fact.
- Text published before 30/11/2022.
- Hán-Việt and nominalised legal, medical and administrative terms (*khởi tố, phê duyệt, chủ trì, kê biên tài sản*); NĐ 30 thể thức: Quốc hiệu, Tiêu ngữ, *Căn cứ ...;*, *Kính gửi:*, *Nơi nhận:*, *TM., KT., TL.*, *Trân trọng.*
- Quotes, approved slogans, titles, proper and brand names, and text discussing a phrase rather than using it.

## 7. Vietnamese review checklist

Run after the upstream check step; done only when every item passes.

1. Section 1 step 4 holds, and the fidelity pass (`overrides/khang.md`) left no unsupported claim.
2. Every pronoun and relation word (*nó, điều này, liên hệ*) has one target; no three short sentences carry one thought; each sentence follows from the last.
3. No strong tell, no paragraph at 3 or more, no rewrite survivor (a new *Điều này*, *không phải ... mà là*, dash, triad, bold label, particle).
4. One matrix row throughout, no inferred honorific; mechanics pass (numbers, dates, sentence case, NFC, tone marks, one term per concept).
5. Read each sentence aloud: would a Vietnamese colleague say it so?
6. **Skeleton pass.** Reread each paragraph for sentence frames alone. Back-translate each sentence word for word; if it lands on a stock English frame (worth X-ing, built into, expects), rewrite it from its meaning. A paragraph with no listed phrase can still be English underneath.
7. Lint the before and after text; compare their numbers, URLs and code.

## 8. Linter

`scripts/vi-tells.py` masks code, URLs, paths and quotes; its recall is low by design, so reading stays the main check.
