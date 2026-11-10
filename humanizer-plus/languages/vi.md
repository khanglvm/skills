# Vietnamese layer

Load this file for any Vietnamese text: drafting, rewriting, translating from English, or reviewing. The upstream humanizer workflow still runs in full (mark the tells, draft, check, final). This file adds the write-from-meaning step, the Vietnamese tells (VI-xx), register, mechanics and the exceptions. Cards in `domains/` add per-medium rules and cite these IDs. `patterns/vi-tells.json` holds the regex-detectable subset, and `scripts/vi-tells.py` lints with it (section 8).

The writer's own rules (project docs, Knowledge preferences) win over anything here. Treat a reviewer's offered wording as direction, not approved copy, and never turn one correction into a word ban.

## 1. Write from meaning

Cao Xuân Hạo's rule for translators: word-for-word is the surest way to translate wrong. Drop the source wording, keep the meaning, then say it the way a Vietnamese writer would. Use this step whenever the input is English notes, an English draft, or your own English reasoning.

1. With the source closed, write one plain line per paragraph: who does what, to what, and why this reader cares.
2. Pick the medium and its row in the register matrix (section 4) before the first sentence.
3. Write each sentence as actor, active verb, concrete object. Put time or place first in news-like text ("Chiều 1/11, ..."). Carry the logic inside the sentence with *sau khi, khiến, nên, vì, để, nhưng, trong khi, nghĩa là*. The system or the step can be the subject in technical text, and Vietnamese may drop the subject where English cannot.
4. Reopen the source. Every number, name, date, condition and hedge (*có thể, chưa, chỉ, vẫn, đã, mới*) must survive; nothing new appears. Each edition may differ in structure, headings and examples, as long as facts, ownership and uncertainty match.

Done when every paragraph traces to a line from step 1 and no sentence keeps English shape: no `được ... bởi`, no default *một* before a noun, no adjective before its noun, no clause order copied from the source.

Human Vietnamese prose links ideas inside long sentences, not with glue at the start of each one. In 17,000 words of pre-2022 news the median sentence ran about 28 words, only 6% ran 10 words or fewer, and an explicit adversative opened a sentence about once per 1,000 words.

## 2. When to act: clusters, not sightings

A single tell is weak evidence; Vietnamese editors and every Vietnamese tool reviewed agree on this. Score each paragraph: strong tells weigh 3, medium 2, weak 1.

- **Strong (act on one sighting):** VI-02, VI-03, VI-14, VI-16, VI-17, the set phrases of VI-15 (*khi nói đến, đó là lý do tại sao*), an invented fact under VI-23, VI-41 to VI-43, and the mechanics errors VI-50 to VI-53.
- **Medium:** most other tells; act when a second tell shares the paragraph or the same tell repeats.
- **Weak** (VI-12, VI-13, VI-33, single connectors and glue words): act only inside a cluster.

`patterns/vi-tells.json` carries the weight of each linted form.

Rewrite a paragraph that scores 3 or more. A sentence with one medium or weak tell next to a concrete fact (a number, name, date) stays as it is. When two tells hit one sentence, rewrite the sentence once from its meaning rather than patching phrase by phrase. If the input already reads naturally, return it nearly unchanged and say so. When a fix would change meaning, register or a claim, leave a comment for the author instead of rewriting.

Calibration from the same human corpus: *Điều này* opened a sentence twice, *Ngoài ra/Bên cạnh đó* four times, *không chỉ ... mà còn* once; *Hơn nữa, Tóm lại, đóng vai trò quan trọng, một cách + adj* and `được ... bởi` never appeared.

## 3. Tell catalogue

Format: tell, typical forms, `✗` AI version → `✓` natural version, then when to keep it. Families use fixed ID ranges so new tells slot in without renumbering. Several are the Vietnamese face of an upstream pattern; the upstream § is noted, and section 3a maps every upstream pattern.

### Framing (VI-01 to VI-09)

**VI-01 Macro-context opener.** *Trong bối cảnh ... không ngừng phát triển, Trong kỷ nguyên số, Trong thế giới ngày nay, Từ xưa đến nay.*
✗ Trong bối cảnh công nghệ phát triển không ngừng, doanh nghiệp cần đổi mới quy trình. → ✓ Doanh nghiệp cần đổi mới quy trình.
Keep when the clause names a specific change the next sentence uses.

**VI-02 Announcing opener (§4).** *Trong bài viết này, chúng ta sẽ cùng tìm hiểu; Hãy cùng khám phá; Dưới đây là một số; Bạn đã bao giờ tự hỏi ...?*
✗ Trong bài viết này, chúng ta sẽ cùng tìm hiểu cách cache giảm tải cho database. → ✓ Cache giữ lại dữ liệu đã đọc, nên database nhận ít truy vấn hơn.
Keep in a syllabus, proposal or long spec that must state its scope.

**VI-03 Template closer and moral (§2, §13).** *Tóm lại; Nhìn chung; Có thể thấy rằng; Hy vọng bài viết hữu ích; Vì vậy, mỗi chúng ta cần ...; hứa hẹn một tương lai tươi sáng*; a last sentence about what will continue *trong tương lai gần*.
✗ Tóm lại, có thể thấy đây là giải pháp đáng cân nhắc. Hy vọng bài viết hữu ích với bạn. → ✓ End on the last fact, a quote, or the real next step.
Keep a summary the reader asked for, or an opinion piece that ends on a demand.

**VI-04 Contrast frame (§1).** *không phải X mà là Y*, the split form *Không phải X. Mà là Y.*, repeated *không chỉ ... mà còn*, *thay vì ..., hãy ...*
✗ Giỏi AI không phải là thuộc vài câu lệnh. Mà là biết đưa đúng bối cảnh. → ✓ Giỏi AI là biết đưa cho nó đúng bối cảnh.
✗ Công cụ không chỉ mở tệp 2 GB trong 4 giây mà còn có phím tắt. → ✓ Công cụ mở tệp 2 GB trong 4 giây và có phím tắt.
Keep one when the negative half corrects a belief the reader holds. After fixing one, check the paragraph for a second copy.

**VI-05 Self-announced importance (§3, §9).** *Điều quan trọng là; Điều thú vị là; Cái hay ở đây là; Cần lưu ý rằng; Về bản chất; Suy cho cùng; X là chìa khóa của Y.*
✗ Điều thú vị là công cụ này chạy hoàn toàn offline. → ✓ Công cụ này chạy hoàn toàn offline.
Keep *Lưu ý:* before a real warning in a procedure.

**VI-06 Social-post arc and slogan fragments.** *Sau một thời gian làm X, tôi nhận ra ...; Nói thẳng.; Một chuẩn. Mọi AI. Mọi API.*; a headline made of two nominal slogans.
✗ Nói thẳng. Một chuẩn giao tiếp. Bất kỳ AI nào. Bất kỳ API nào. → ✓ Chuẩn giao tiếp này dùng chung cho mọi AI và mọi API.
Keep a genuine anecdote with its date or number.

### Translationese (VI-10 to VI-19)

**VI-10 Passive calque `được ... bởi`.** Native order puts the agent right after *được* or uses *do*.
✗ Sản phẩm được phát triển bởi đội kỹ sư và được tin dùng bởi hàng nghìn khách hàng. → ✓ Sản phẩm do đội kỹ sư phát triển và được hàng nghìn khách hàng tin dùng.
Keep a passive with an unknown or unimportant agent. *Được* marks benefit, *bị* marks harm.

**VI-11 Nominalisation and light verbs.** *việc/sự + verb, tiến hành, thực hiện việc, thông qua việc, đưa ra sự hỗ trợ, công tác*; sentence after sentence opening with *Việc*.
✗ Nhóm tiến hành việc gửi bản nháp để thực hiện việc lấy ý kiến. → ✓ Nhóm gửi bản nháp để lấy ý kiến.
Keep *việc + verb* as a subject naming a defined act ("Việc tính phí cần được xác nhận"), legal procedure names, and real nouns (*sự cố, sự kiện*).

**VI-12 Article and plural calque.** *một* for every *a/an*, *các/những* for every English plural.
✗ Đây là một giải pháp giúp bạn đạt được những kết quả tốt trong các công việc hằng ngày. → ✓ Giải pháp này giúp bạn làm việc hằng ngày tốt hơn.
Keep *một* when it counts one, *các/những* when plurality matters.

**VI-13 `một cách` + adjective.**
✗ Hệ thống xử lý yêu cầu một cách nhanh chóng và hiệu quả. → ✓ Hệ thống xử lý yêu cầu nhanh và hiệu quả.

**VI-14 Literal English metaphor.** *mở khóa tiềm năng* (unlock), *điều hướng sự phức tạp* (navigate complexity), *cánh cửa* for gate, *tác động có ý nghĩa, ở cấp độ cốt lõi, đi sâu vào, tận dụng sức mạnh của, thay đổi cuộc chơi*; Western imagery such as *người hùng thầm lặng*. Name the plain meaning.
✗ Công cụ mở khóa tiềm năng tìm xu hướng trong dữ liệu bán hàng. → ✓ Công cụ giúp tìm xu hướng trong dữ liệu bán hàng.
✗ hai cánh cửa (for "two gates", meaning two audiences) → ✓ hai đối tượng
Keep an approved slogan, and *liền mạch* or *tận dụng* where the break or the reused resource is named.

**VI-15 Phrase calques.** *khi nói đến* → *về*; *điều này có nghĩa là* → *tức là*; *đó là lý do tại sao* → *vì vậy*; repeated *một trong những ... nhất*; *và/hoặc*; chains of *của ... của ... của*; *đối với việc*; UI fillers *Có vẻ như ..., Có điều gì đó không ổn*.
✗ Khi nói đến hiệu năng, đây là một trong những thư viện nhanh nhất. Điều này có nghĩa là bạn ít phải tối ưu. → ✓ Về hiệu năng, thư viện này thuộc nhóm nhanh nhất, nên bạn ít phải tối ưu.
Keep *và/hoặc* in a contract that already uses it.

**VI-16 Email and support calques.** *Tôi hy vọng email này tìm thấy bạn khỏe; Đừng ngần ngại liên hệ; Cảm ơn bạn đã dành thời gian; vui lòng* before every sentence; *Học thêm* for "Learn more".
✗ Đừng ngần ngại liên hệ nếu bạn có bất kỳ câu hỏi nào. → ✓ Nếu cần thêm thông tin, bạn cứ phản hồi email này.
Keep native support formulas: *xin lỗi vì sự bất tiện, rất tiếc vì trải nghiệm chưa tốt*.

**VI-17 Developer-term calques.** *cam kết các thay đổi* (commit), *triển khai đến sản xuất, hợp nhất nhánh, yêu cầu kéo, sửa mã*. See the terms table in section 5.
✗ Sau khi hợp nhất nhánh, nhóm sẽ triển khai bản vá lên môi trường sản xuất. → ✓ Sau khi merge, nhóm sẽ deploy bản fix lên production.

### Inflation (VI-20 to VI-29)

**VI-20 Hollow evaluative words.** The Vietnamese counterpart of upstream §12; count them in groups. *giải pháp toàn diện, vượt trội, đột phá, đẳng cấp, nâng tầm, bứt phá, tối ưu hóa (figurative), kỷ nguyên số, hệ sinh thái, hành trình (figurative), bức tranh toàn cảnh, chìa khóa thành công, giá trị cốt lõi, mang lại nhiều lợi ích, đa dạng và phong phú, không thể phủ nhận, nổi bật với, bày tỏ sự ủng hộ*; official-style intensifiers *vô cùng, hết sức, sâu sắc, mạnh mẽ, quyết liệt* stacked on *đẩy mạnh, tăng cường, nâng cao*.
✗ Nền tảng mang lại giải pháp toàn diện, giúp doanh nghiệp tối ưu hóa quy trình bán hàng trong kỷ nguyên số. → ✓ Nền tảng giúp doanh nghiệp quản lý quy trình bán hàng. Anything more specific needs a fact from the brief; ask for it.
Keep technical uses (*tối ưu hóa hàm mục tiêu*) and a literal *hành trình*.

**VI-21 Significance riders (§13, §15).** *đóng vai trò quan trọng/then chốt trong việc; ..., góp phần ...; ..., qua đó khẳng định ...; đánh dấu bước ngoặt; mang tính lịch sử.*
✗ Đơn vị đã tổ chức 12 lớp tập huấn, góp phần nâng cao năng lực cán bộ và khẳng định vị thế trong chuyển đổi số. → ✓ Đơn vị đã tổ chức 12 lớp tập huấn cho cán bộ.
Keep a role the text actually analyses.

**VI-22 Doubled synonyms and stacked sets (§6).** *triển khai thực hiện, tổ chức thực hiện, đảm bảo duy trì, nhanh chóng, kịp thời, hiệu quả*; three Tết wishes in a row.
✗ Nhóm đã triển khai thực hiện kế hoạch một cách nhanh chóng, kịp thời và hiệu quả. → ✓ Nhóm đã thực hiện kế hoạch đúng hạn.
Keep fixed administrative pairs (*kiểm tra, giám sát*) and one traditional wish.

**VI-23 Borrowed authority, invented numbers, unproven superlatives (§17).** *Các chuyên gia cho rằng; Nhiều nghiên cứu chỉ ra; tăng 45%* with no source; *số 1, tốt nhất, hàng đầu, duy nhất* in advertising, which Luật Quảng cáo 16/2012, Điều 8 khoản 11 allows only with documented proof.
✗ Nhiều nghiên cứu chỉ ra phương pháp này tăng năng suất 45%. → ✓ Name the study the source gives, or cut the claim. Never invent a source or a replacement number.

**VI-24 Swappable content and set-piece prose.** Tri ân, Tết or launch copy that fits any recipient (*Một năm nhiều thử thách và cơ hội ...; Mỗi đơn hàng là một kỷ niệm*); ornamental verbs *nuôi dưỡng, bồi đắp, vun đắp, thắp sáng, lan tỏa*. Swap the name in your head: if the text still fits, it lacks facts.
Fix with details the writer supplied; ask when there are none. Never invent memories, prices or customers.

### Glue and rhythm (VI-30 to VI-39)

**VI-30 Sentence-initial connectors.** *Hơn nữa, Bên cạnh đó, Ngoài ra, Thêm vào đó, Đồng thời, Không những thế*; a mid-sentence *, đồng thời* as all-purpose glue; chains of *đồng thời ... qua đó ... từ đó*.
✗ Hơn nữa, cách này tiết kiệm chi phí. Bên cạnh đó, nó còn chạy nhanh hơn. → ✓ Cách này vừa rẻ hơn vừa chạy nhanh hơn.
Keep *Nhưng* or *Tuy nhiên* where the content really turns, and one *Trong khi đó* per piece.

**VI-31 Unanchored glue words.** *Điều này, Việc này, Chính vì vậy, Đây là lý do*, and *nó* with two possible targets. Every pronoun and relation word needs one clear target.
✗ Nhóm đổi lịch giao hàng và cách tính phí. Điều này áp dụng từ thứ Hai. → ✓ Lịch giao hàng và cách tính phí mới áp dụng từ thứ Hai. If the source does not say which one applies, ask.

**VI-32 Chopped fragments.** The correction the maintainer makes most often in agent drafts. One thought cut into short sentences or comma-chained bits. Join them with real connectives (*vì, nên, nhưng, để, khiến, sau khi, trong khi, nghĩa là, và ... cũng vậy*) or relation words (*hướng đến, cho, dành cho*).
✗ Một đồng nghiệp mới cần được giới thiệu đôi chút trước khi hiểu tên một trang có ý nghĩa gì. Agent cũng cần phần giới thiệu ấy. → ✓ Một đồng nghiệp mới cần được giới thiệu đôi chút trước khi hiểu tên một trang có ý nghĩa gì, và agent cũng vậy.
A conjunction between unrelated statements fixes nothing: the ideas must form a story. UI strings, lists, quotes and code keep their own form.

**VI-33 Uniform rhythm and repeated openers (§7).**
✗ Công ty thành lập năm 2010. Công ty có trụ sở tại Hà Nội. Công ty chuyên làm phần mềm. → ✓ Công ty thành lập năm 2010, đặt trụ sở tại Hà Nội và chuyên làm phần mềm.
Keep required repeated blocks (*Căn cứ ...;*, *Nơi nhận:*) and deliberate repetition in narrative.

**VI-34 Listicle shape (§19, §20).** *Dưới đây là một số lợi ích:* followed by two-word noun bullets, a bold label on every line, emoji section icons.
✗ Dưới đây là một số lợi ích: Tiết kiệm thời gian / Tăng hiệu quả / Dễ sử dụng → ✓ Prose with the specifics the source gives, or a list of parallel facts.
Keep steps, checklists and reference lists.

### Register (VI-40 to VI-49)

**VI-40 Mixed or wrong address.** *quý khách* in the hero and *bạn* in the FAQ; *chúng ta* on a company page where *chúng tôi* is meant; *Quý khách* in a CLI error; *tôi* and *mình* alternating for one writer. Pick one row of the matrix and hold it.

**VI-41 Inferred honorifics.** *anh, chị, em, ạ* chosen from a name, tag, avatar or role. Missing context establishes nothing.
✗ Anh check giúp em bản fix này ạ. → ✓ Nhờ kiểm tra giúp bản fix này. (or name the role: QA kiểm tra giúp ...)

**VI-42 Faked casualness.** Particles, teencode (*ko, dc, r*), slang, typos, emoji or anecdotes inserted to sound human. Use plain, neutral Vietnamese; keep particles, dialect and slang only where the input or the medium already has them (chat may use *nhé, nghe*).

**VI-43 Chatbot residue (§22, §23).** *Chắc chắn rồi!; Câu hỏi rất hay!; Dưới đây là phiên bản đã chỉnh sửa; Nếu bạn cần, mình có thể ...; Là một mô hình ngôn ngữ ...; Tính đến thời điểm cập nhật kiến thức ...* Remove the wrapper, keep the content.

### Mechanics tells (VI-50 to VI-59)

Objective errors. Section 5 has the rules.

- **VI-50** English number format: *1,000,000; 3.6 triệu.*
- **VI-51** Title Case or ALL CAPS in headings and buttons: *Chọn Tất Cả, Tầm Quan Trọng Của Việc Học.*
- **VI-52** Em or en dash used to join clauses.
- **VI-53** *X thất bại* or *X không thành công* in UI errors: write *Không X được*.
- **VI-54** English-shaped long date in prose: *vào ngày 15 tháng 10 năm 2021.*
- **VI-55** A space before , ; : ? or !, or a comma before *và/hoặc* in a list.
- **VI-56** Decomposed (NFD) characters, or both tone-mark styles in one document.

## 3a. Upstream patterns in Vietnamese

| Upstream | In Vietnamese |
|---|---|
| [upstream §1 Not X but Y] | VI-04 |
| [upstream §2 One-line closers and dramatic fragments] | VI-03, VI-06 |
| [upstream §3 Sayings that sound deep] | VI-05 |
| [upstream §4 Staged run-up before the point] | VI-02 |
| [upstream §5 Arguing with no one] | applies as written |
| [upstream §6 Forced triads] | VI-22 |
| [upstream §7 Repeated sentence openings] | VI-33 |
| [upstream §8 Dashes as the universal connector] | VI-52, with the hyphen note below |
| [upstream §9 Stacked qualifiers] | VI-05 |
| [upstream §10 Hyphenated pairs everywhere] | does not apply |
| [upstream §11 Passive voice and missing subjects] | VI-10; Vietnamese drops subjects natively, so flag only a hidden actor the reader needs |
| [upstream §12 Overused AI words] | VI-20 and VI-14 replace the English list |
| [upstream §13 Inflated significance] | VI-21, VI-03 |
| [upstream §14 Vague connection or association] | applies as written |
| [upstream §15 Shallow -ing phrases] | VI-21 (rider clauses with *góp phần, qua đó*) |
| [upstream §16 Sales language] | VI-20, VI-23 |
| [upstream §17 Borrowed authority] | VI-23 |
| [upstream §18 Avoiding is, are, and has] | VI-11 |
| [upstream §19 Bold as decoration] | VI-34 |
| [upstream §20 Decorative headings] | VI-34, VI-51 |
| [upstream §21 Curly quotation marks] | does not apply: Vietnamese press and localised software use “ ”; follow the target file |
| [upstream §22 Chatbot residue] | VI-43, VI-16 |
| [upstream §23 Knowledge-limit disclaimers and guesses] | VI-43 |
| [upstream §24 A heading repeated in the first sentence] | applies as written |
| [upstream §25 Writing about the document instead of its subject] | applies as written; VI-02 for the announcing form |
| [upstream §26 Re-explaining what the reader knows] | applies as written |

Hyphen note for §8: no em or en dash as a clause connector. A spaced hyphen is the Vietnamese press convention for a role after a name, attribution after a quote and photo credits; use it in news-style copy or when the writer's sample does. Elsewhere use a comma, colon or parentheses. Compounds (*kinh tế - xã hội*), the Tiêu ngữ and ranges keep their hyphen.

## 4. Register and address by medium

Choose the row before writing. One address set per document; a channel override (a Zalo service notice) is the only exception.

| Medium | Reader | Writer | Particles | Notes |
|---|---|---|---|---|
| Jira / Outline comment | none | none | none | Subject-free, 🤖 first line; `domains/workplace.md` |
| Team chat | tag, then no name | *mình* or none | *nhé, nghe* ok | One action per line |
| PR, code review | the change | *mình* or none | none | "Chỗ này nên tách hàm riêng." |
| RFC, design doc, runbook, postmortem | none | none | none | System as subject; runbook steps are bare imperatives |
| README, tutorial, help article | *bạn* | project voice | none | Gloss a term once |
| UI strings, errors | *bạn*, sparingly | none | none | `domains/ui-copy.md` |
| Release notes | none or *bạn* | none | none | `domains/release-notes.md` |
| Personal blog articles | *bạn*, sparingly | *mình* | column voice only | `domains/article.md` |
| Landing: SaaS, studio, consumer | *bạn* | *chúng tôi* | none | `domains/landing.md` |
| Landing: bank, insurance, real estate; status page | *quý khách* | *chúng tôi* | none | Plain words on status pages |
| B2B email, known relation | *anh/chị* only when known | as the relation sets | *ạ* only when known | Otherwise neutral, no pronoun |
| Official document (NĐ 30/2020) | *Kính gửi:* + body | the agency | none | Keep every thể thức element |
| News-style report | full name with (age, place) once, then honorific + given name | *phóng viên* | none | *tôi* belongs to columns |

- *Chúng tôi* is the company; *chúng ta* only when the reader is really included.
- Never infer age, gender or an honorific from a name, tag or role (VI-41).
- Keep a regional voice (*mô, răng, nghen, hông*) that the input already has; never add one.

## 5. Mechanics

**Numbers.** Thousands take a period, decimals a comma: 1.526; 5,25 cm; 3,6 triệu đồng/tháng. Prose uses the scale words (2,5 tỷ đồng); tables use full digits; never mix the two in one column. VND has no decimals; put ₫ after the number with a space, or write *đồng*. Counts and measures take digits (4 người, 7 km, 185 m²); a spelled-out small number is fine in narrative. Hold one unit spacing per document (*24 giờ*, *1.000 đ/phút*).

**Dates and times.** dd/mm/yyyy, one form per document (29/04/2026 or 29/4/2026); drop the year when it is clear (19/7); the part of day goes before the date (*Sáng 5/8*); months as *tháng 1/2026*; 24-hour time (14:30). Official documents use *Hà Nội, ngày 05 tháng 3 năm 2020*, with a leading zero for days below 10 and for months 1 and 2.

**Punctuation.** No space before . , : ; ? !, one space after. No comma before *và/hoặc* in a list. Brackets carry age and place (*31 tuổi, quê Hậu Giang*). Use an ellipsis sparingly and *?!* only in chat. Quotation marks may flag a borrowed or figurative word. Semicolons separate parallel list items in prose.

**Capitals.** Sentence case for titles, headings, buttons and menu items. Institutions capitalise each content word (*Bộ Tài nguyên và Môi trường*). Role plus name: official copy capitalises it (*Thủ tướng Chính phủ*); everyday copy lowercases a role placed after the name; pick one per document. Product names keep their own casing. ALL CAPS only for NĐ 30 elements (Quốc hiệu, document type, *MẬT, KHẨN*) or a brand guide that requires it.

**Spelling and encoding.** Emit NFC. Hold one tone-mark style per document (*hòa/hoà, thủy/thuỷ*) and follow the project's existing files. With no files to follow, use the old style (*hòa, thủy, hủy*). Hold *kỳ/kì* the same way. Slugs, identifiers, branch names and commit subjects stay ASCII.

**English terms: keep or Vietnamise.** Hold one term per concept within a document.

| Keep in English in dev prose, chat, PR, Jira | Vietnamise in UI and consumer copy | Both live: pick by formality |
|---|---|---|
| commit, push, merge, pull request, MR, branch | tệp or tập tin (file), thẻ (tab) | server / máy chủ (non-engineers) |
| build, deploy, release, rollback, hotfix | Cài đặt, Tải xuống, Tải lên | database / cơ sở dữ liệu (specs) |
| bug, fix, test (*chạy test, test lại*), review | sao lưu, đồng bộ, khôi phục | cache / bộ nhớ đệm (published docs) |
| task, ticket, sprint, backlog, Definition of Done | Đăng nhập, Đăng xuất, mật khẩu, tài khoản | deploy / triển khai (gloss, corporate text) |
| pipeline, job, image, registry, repo | lỗi (a bug as users see it) | test / kiểm thử (*kết quả kiểm thử* in QA reports) |
| staging, production, endpoint, timeout, log, API, ID | Tìm kiếm, Thử lại, Hủy | source code / mã nguồn (formal company story only) |
| code (*sửa code*, not *sửa mã*), agent, harness, CLI, PRD | | |
| QA, QC, BE Dev, PM, engineer, developer | | |

In a tutorial or article, gloss an English term once in everyday words ("CI/CD, tức tích hợp và triển khai liên tục"), then use it bare. Never gloss in chat, Jira or a handoff. Name a document by what it is (PRD, *tài liệu kỹ thuật*); *trang* means a literal page.

## 6. Leave these alone

- A single medium or weak tell, above all one sitting next to a concrete fact.
- Text published before 30/11/2022.
- Hán-Việt and nominalised legal, medical and administrative terms (*khởi tố, phê duyệt, chủ trì, kê biên tài sản*), and NĐ 30 thể thức: Quốc hiệu, Tiêu ngữ, *Căn cứ ...;*, *Kính gửi:*, *Nơi nhận:*, *TM., KT., TL.*, *Trân trọng.*
- A passive whose agent is unknown or beside the point; *do X thiết kế*; *được X tin dùng*.
- Subject-free sentences in UI, chat, Jira, runbooks and release notes.
- Stable English dev terms in dev prose, and product or brand names.
- One *không chỉ ... mà còn* that carries the argument; *Nhưng* or *Tuy nhiên* where the content turns; one *Cụ thể,* or *Trong khi đó*.
- Native politeness: *xin lỗi vì sự bất tiện, Trân trọng*, one traditional wish.
- Quotes, approved slogans, titles, proper names, and text that discusses a phrase rather than uses it.
- Dialect, particles and slang already present in the input.
- Ordinary uses of words that also appear in VI-14 or VI-20 (*tận dụng* an existing resource, *hành trình* as a trip, *dấu ấn* in a natural collocation).
- Curly quotes, and the spaced hyphen in news-style apposition, compounds and ranges.

A human-sounding fix never adds typos, slang, particles, emoji or invented detail.

## 7. Vietnamese review checklist

Run after the upstream check step. The draft is done only when every item passes.

1. Every number, unit, name, date, condition and hedge from the source is present; nothing was added.
2. Every pronoun and relation word (*nó, điều này, liên hệ*) has one clear target.
3. In prose, no run of three or more short sentences carries a single thought, and each sentence follows from the one before.
4. Every strong tell from section 2 is gone.
5. No paragraph scores 3 or more (section 2).
6. Survivors of the rewrite are gone: a new *Điều này*, a new *không phải ... mà là*, a dash, a triad, a bold label, an inserted particle.
7. Address matches one matrix row throughout, with no inferred honorific.
8. Mechanics pass: number and date format, sentence case, NFC, one tone-mark style, one term per concept.
9. Read each sentence aloud: would a Vietnamese colleague say it this way?
10. Run the linter (section 8) on the before and after text and compare numbers, URLs and code between them. Its flags are prompts to reread, not orders to delete. Do not claim a check you did not run.

## 8. Linter

```
python3 <skill-dir>/scripts/vi-tells.py [--json] [--doctype prose|ui|handoff|marketing] [--include-quotes] FILE... | -
```

It normalises to NFC, masks frontmatter, code, URLs, paths, HTML tags, blockquotes and quoted speech, then prints `path:line:col id strength "match" why`. A paragraph that scores 3 or more (section 2) is a cluster and is listed first. Exit 0 means no findings, 1 findings, 2 a usage or catalogue error. `--doctype` turns on the scope-specific patterns (`ui` for strings, `handoff` for Jira and Outline comments, `marketing` for landing copy); `prose` is the default.

On 14 human news articles published before 2022 (about 17,000 words, 536 paragraphs) it reports no cluster. Recall on agent-written text is low by design, so reading this file stays the main check.
