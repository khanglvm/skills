# Vietnamese tell catalogue

Every tell in `languages/vi.md` section 3, in full. Read it for review mode, when rewriting existing text, or to resolve a linter finding. Entry: forms, `✗` AI → `✓` natural, when to keep. Every *Keep* here is a leave-alone rule. A heading's § is the upstream pattern it localises (the rest are at the end). Each linted form's strength lives in `patterns/vi-tells.json`.

### Framing (VI-01 to VI-09)

**VI-01 Macro-context opener.** *Trong bối cảnh ... không ngừng phát triển, Trong kỷ nguyên số, Trong thế giới ngày nay, Từ xưa đến nay.*
✗ Trong bối cảnh công nghệ phát triển không ngừng, doanh nghiệp cần đổi mới quy trình. → ✓ Doanh nghiệp cần đổi mới quy trình.
Keep when it names a specific change the next sentence uses.

**VI-02 Announcing opener (§4).** *Trong bài viết này, chúng ta sẽ cùng tìm hiểu; Hãy cùng khám phá; Dưới đây là một số; Bạn đã bao giờ tự hỏi ...?*
✗ Trong bài viết này, chúng ta sẽ cùng tìm hiểu cách cache giảm tải cho database. → ✓ Cache giữ lại dữ liệu đã đọc, nên database nhận ít truy vấn hơn.
Keep in a syllabus, proposal or long spec that must state its scope.

**VI-03 Template closer and moral (§2, §13).** *Tóm lại; Nhìn chung; Có thể thấy rằng; Hy vọng bài viết hữu ích; Vì vậy, mỗi chúng ta cần ...; hứa hẹn một tương lai tươi sáng*; a last line about *trong tương lai gần*.
✗ Tóm lại, có thể thấy đây là giải pháp đáng cân nhắc. Hy vọng bài viết hữu ích với bạn. → ✓ End on the last fact, a quote, or the real next step.
Keep a summary the reader asked for, or an opinion piece ending on a demand.

**VI-04 Contrast frame (§1).** *không phải X mà là Y*, split *Không phải X. Mà là Y.*, repeated *không chỉ ... mà còn*, *thay vì ..., hãy ...*
✗ Giỏi AI không phải là thuộc vài câu lệnh. Mà là biết đưa đúng bối cảnh. → ✓ Giỏi AI là biết đưa cho nó đúng bối cảnh.
✗ Công cụ không chỉ mở tệp 2 GB trong 4 giây mà còn có phím tắt. → ✓ Công cụ mở tệp 2 GB trong 4 giây và có phím tắt.
Keep one whose negative half corrects a belief the reader holds, or one *không chỉ ... mà còn* carrying the argument. After a fix, look for a second.

**VI-05 Self-announced importance (§3, §9).** *Điều quan trọng là; Điều thú vị là; Cái hay ở đây là; Cần lưu ý rằng; Về bản chất; Suy cho cùng; X là chìa khóa của Y.*
✗ Điều thú vị là công cụ này chạy hoàn toàn offline. → ✓ Công cụ này chạy hoàn toàn offline.
Keep *Lưu ý:* before a real warning in a procedure.

**VI-06 Social-post arc and slogan fragments (§2).** *Sau một thời gian làm X, tôi nhận ra ...; Nói thẳng.; Một chuẩn. Mọi AI. Mọi API.*; a headline of two nominal slogans.
✗ Nói thẳng. Một chuẩn giao tiếp. Bất kỳ AI nào. Bất kỳ API nào. → ✓ Chuẩn giao tiếp này dùng chung cho mọi AI và mọi API.
Keep a genuine anecdote with its date or number.

### Translationese (VI-10 to VI-19)

**VI-10 Passive calque `được ... bởi` (§11).** Native order puts the agent right after *được* or uses *do*.
✗ Sản phẩm được phát triển bởi đội kỹ sư và được tin dùng bởi hàng nghìn khách hàng. → ✓ Sản phẩm do đội kỹ sư phát triển và được hàng nghìn khách hàng tin dùng.
Keep a passive with an unknown or irrelevant agent. *Được* marks benefit, *bị* harm.

**VI-11 Nominalisation and light verbs (§18).** *việc/sự + verb, tiến hành, thực hiện việc, thông qua việc, đưa ra sự hỗ trợ, công tác*; *Việc* opening sentence after sentence.
✗ Nhóm tiến hành việc gửi bản nháp để thực hiện việc lấy ý kiến. → ✓ Nhóm gửi bản nháp để lấy ý kiến.
Keep *việc + verb* naming a defined act ("Việc tính phí cần được xác nhận"), legal procedure names, real nouns (*sự cố, sự kiện*).

**VI-12 Article and plural calque.** *một* for every *a/an*, *các/những* for every plural.
✗ Đây là một giải pháp giúp bạn đạt được những kết quả tốt trong các công việc hằng ngày. → ✓ Giải pháp này giúp bạn làm việc hằng ngày tốt hơn.
Keep *một* when it counts one, *các/những* when plurality matters.

**VI-13 `một cách` + adjective.**
✗ Hệ thống xử lý yêu cầu một cách nhanh chóng và hiệu quả. → ✓ Hệ thống xử lý yêu cầu nhanh và hiệu quả.

**VI-14 Literal English metaphor (§12).** *mở khóa tiềm năng* (unlock), *điều hướng sự phức tạp*, *cánh cửa* for gate, *tác động có ý nghĩa, ở cấp độ cốt lõi, đi sâu vào, tận dụng sức mạnh của, thay đổi cuộc chơi*; Western imagery (*người hùng thầm lặng*). Say the plain meaning.
✗ Công cụ mở khóa tiềm năng tìm xu hướng trong dữ liệu bán hàng. → ✓ Công cụ giúp tìm xu hướng trong dữ liệu bán hàng.
✗ hai cánh cửa (for "two gates", meaning two audiences) → ✓ hai đối tượng
Keep an approved slogan; *liền mạch* or *tận dụng* when the break or reused resource is named.

**VI-15 Phrase calques and English skeletons.** Set phrases: *khi nói đến* → *về*; *điều này có nghĩa là* → *tức là*; *đó là lý do tại sao* → *vì vậy*; repeated *một trong những ... nhất*; *và/hoặc*; *của ... của ... của*; *đối với việc*; UI fillers *Có vẻ như ..., Có điều gì đó không ổn*.
✗ Khi nói đến hiệu năng, đây là một trong những thư viện nhanh nhất. Điều này có nghĩa là bạn ít phải tối ưu. → ✓ Về hiệu năng, thư viện này thuộc nhóm nhanh nhất, nên bạn ít phải tối ưu.
An **English skeleton** puts Vietnamese words on an English frame. Back-translate word for word; if it lands on a stock English frame, rewrite from the meaning. Frames: worth X-ing (*giới hạn nên biết, là điều đáng có*), built into (*nằm sẵn trong*), belongs to (*thuộc về* a place), expects (*dự kiến* for an input), say what it should (*nói đúng những gì nó cần nói*), does not stand still (*không vì thế mà đứng yên*).
✗ Công cụ có một giới hạn nên biết: mỗi lần chỉ đọc 50 trang. → ✓ Có điều công cụ chỉ đọc được 50 trang mỗi lần.
✗ API dự kiến nhận một chuỗi JSON. → ✓ API nhận đầu vào là chuỗi JSON.
✗ Tài liệu có còn nói đúng những gì nó cần nói không? → ✓ Nội dung tài liệu còn đúng không?
Keep *và/hoặc* in a contract using it; *thuộc về* for ownership (*bản quyền thuộc về tác giả*); *dự kiến* for a plan (*dự kiến phát hành 5/12*); *đáng* + verb on a concrete noun (*phim đáng xem*).

**VI-16 Email and support calques (§22).** *Tôi hy vọng email này tìm thấy bạn khỏe; Đừng ngần ngại liên hệ; Cảm ơn bạn đã dành thời gian; vui lòng* on every sentence; *Học thêm* ("Learn more").
✗ Đừng ngần ngại liên hệ nếu bạn có bất kỳ câu hỏi nào. → ✓ Nếu cần thêm thông tin, bạn cứ phản hồi email này.
Keep native formulas: *xin lỗi vì sự bất tiện, rất tiếc vì trải nghiệm chưa tốt, Trân trọng*, one traditional wish.

**VI-17 Developer-term calques.** *cam kết các thay đổi* (commit), *triển khai đến sản xuất, hợp nhất nhánh, yêu cầu kéo, sửa mã*; terms in vi.md section 5.
✗ Sau khi hợp nhất nhánh, nhóm sẽ triển khai bản vá lên môi trường sản xuất. → ✓ Sau khi merge, nhóm sẽ deploy bản fix lên production.

### Inflation (VI-20 to VI-29)

**VI-20 Hollow evaluative words (§12, §16).** *giải pháp toàn diện, vượt trội, đột phá, đẳng cấp, nâng tầm, bứt phá, tối ưu hóa (figurative), kỷ nguyên số, hệ sinh thái, hành trình (figurative), bức tranh toàn cảnh, chìa khóa thành công, giá trị cốt lõi, mang lại nhiều lợi ích, đa dạng và phong phú, không thể phủ nhận, nổi bật với, bày tỏ sự ủng hộ*; official intensifiers *vô cùng, hết sức, sâu sắc, mạnh mẽ, quyết liệt* stacked on *đẩy mạnh, tăng cường, nâng cao*.
✗ Nền tảng mang lại giải pháp toàn diện, giúp doanh nghiệp tối ưu hóa quy trình bán hàng trong kỷ nguyên số. → ✓ Nền tảng giúp doanh nghiệp quản lý quy trình bán hàng. More needs a fact from the brief; ask.
Keep technical uses (*tối ưu hóa hàm mục tiêu*), a literal *hành trình*, *dấu ấn* in a natural collocation.

**VI-21 Significance riders (§13, §15).** *đóng vai trò quan trọng/then chốt trong việc; ..., góp phần ...; ..., qua đó khẳng định ...; đánh dấu bước ngoặt; mang tính lịch sử.*
✗ Đơn vị đã tổ chức 12 lớp tập huấn, góp phần nâng cao năng lực cán bộ và khẳng định vị thế trong chuyển đổi số. → ✓ Đơn vị đã tổ chức 12 lớp tập huấn cho cán bộ.
Keep a role the text actually analyses.

**VI-22 Doubled synonyms and stacked sets (§6).** *triển khai thực hiện, tổ chức thực hiện, đảm bảo duy trì, nhanh chóng, kịp thời, hiệu quả*; three Tết wishes in a row.
✗ Nhóm đã triển khai thực hiện kế hoạch một cách nhanh chóng, kịp thời và hiệu quả. → ✓ Nhóm đã thực hiện kế hoạch đúng hạn.
Keep fixed administrative pairs (*kiểm tra, giám sát*) and one traditional wish.

**VI-23 Borrowed authority, invented numbers, unproven claims (§16, §17).** *Các chuyên gia cho rằng; Nhiều nghiên cứu chỉ ra; tăng 45%* with no source; *số 1, tốt nhất, hàng đầu, duy nhất* in ads, which Luật Quảng cáo 16/2012, Điều 8 khoản 11 allows only with documented proof; quantifiers and rankings the source lacks (*chủ yếu, thường, mọi, vài, đáng nhớ nhất, chắc chắn*; fidelity pass in `overrides/khang.md`).
✗ Nhiều nghiên cứu chỉ ra phương pháp này tăng năng suất 45%. → ✓ Name the study the source gives, or cut the claim. Never invent a source or a replacement number.

**VI-24 Swappable content and set-piece prose.** Tri ân, Tết or launch copy that fits any recipient (*Một năm nhiều thử thách và cơ hội ...; Mỗi đơn hàng là một kỷ niệm*); ornamental *nuôi dưỡng, bồi đắp, vun đắp, thắp sáng, lan tỏa*. If it still fits with another name swapped in, it lacks facts.
Fix with the writer's details or ask; never invent memories, prices or customers.

### Glue and rhythm (VI-30 to VI-39)

**VI-30 Sentence-initial connectors.** *Hơn nữa, Bên cạnh đó, Ngoài ra, Thêm vào đó, Đồng thời, Không những thế*; mid-sentence *, đồng thời* as glue; chains of *đồng thời ... qua đó ... từ đó*.
✗ Hơn nữa, cách này tiết kiệm chi phí. Bên cạnh đó, nó còn chạy nhanh hơn. → ✓ Cách này vừa rẻ hơn vừa chạy nhanh hơn.
Keep *Nhưng* or *Tuy nhiên* where the content turns, and one *Cụ thể,* or *Trong khi đó* per piece. Human news prose links ideas inside long sentences rather than with glue at each start (counts: `references/sources.md`, R1).

**VI-31 Unanchored glue words.** *Điều này, Việc này, Chính vì vậy, Đây là lý do*, and *nó* with two possible targets. Each pronoun and relation word needs one clear target.
✗ Nhóm đổi lịch giao hàng và cách tính phí. Điều này áp dụng từ thứ Hai. → ✓ Lịch giao hàng và cách tính phí mới áp dụng từ thứ Hai. If the source does not say which applies, ask.

**VI-32 Chopped fragments.** One thought cut into short sentences or comma-chained bits. Join with real connectives (*vì, nên, nhưng, để, khiến, sau khi, trong khi, nghĩa là, và ... cũng vậy*) or relation words (*hướng đến, cho, dành cho*).
✗ Một đồng nghiệp mới cần được giới thiệu đôi chút trước khi hiểu tên một trang có ý nghĩa gì. Agent cũng cần phần giới thiệu ấy. → ✓ Một đồng nghiệp mới cần được giới thiệu đôi chút trước khi hiểu tên một trang có ý nghĩa gì, và agent cũng vậy.
A conjunction between unrelated statements fixes nothing; the ideas must form a story. UI strings, lists, quotes and code keep their form.

**VI-33 Uniform rhythm and repeated openers (§7).**
✗ Công ty thành lập năm 2010. Công ty có trụ sở tại Hà Nội. Công ty chuyên làm phần mềm. → ✓ Công ty thành lập năm 2010, đặt trụ sở tại Hà Nội và chuyên làm phần mềm.
Keep required repeated blocks (*Căn cứ ...;*, *Nơi nhận:*) and deliberate narrative repetition.

**VI-34 Listicle shape (§19, §20).** *Dưới đây là một số lợi ích:* then two-word noun bullets, a bold label per line, emoji section icons.
✗ Dưới đây là một số lợi ích: Tiết kiệm thời gian / Tăng hiệu quả / Dễ sử dụng → ✓ Prose with the source's specifics, or a list of parallel facts.
Keep steps, checklists and reference lists.

### Register (VI-40 to VI-49)

**VI-40 Mixed or wrong address.** *quý khách* in the hero, *bạn* in the FAQ; *chúng ta* for a company that means *chúng tôi* (the reader is not included); *Quý khách* in a CLI error; *tôi* and *mình* alternating for one writer. Hold one row of the register matrix (vi.md section 4).

**VI-41 Inferred honorifics.** *anh, chị, em, ạ*, age or gender inferred from a name, tag, avatar or role. Missing context establishes nothing.
✗ Anh check giúp em bản fix này ạ. → ✓ Nhờ kiểm tra giúp bản fix này. (or the role: QA kiểm tra giúp ...)

**VI-42 Faked casualness.** Particles, teencode (*ko, dc, r*), slang, typos, emoji or anecdotes added to sound human. Write plain, neutral Vietnamese: particles and slang only where the input or medium has them (chat: *nhé, nghe*), a regional voice (*mô, răng, nghen, hông*) only from the input, and never typos, emoji or invented detail.

**VI-43 Chatbot residue (§22, §23).** *Chắc chắn rồi!; Câu hỏi rất hay!; Dưới đây là phiên bản đã chỉnh sửa; Nếu bạn cần, mình có thể ...; Là một mô hình ngôn ngữ ...; Tính đến thời điểm cập nhật kiến thức ...* Remove the wrapper, keep the content.

### Mechanics tells (VI-50 to VI-59)

Objective errors; rules in vi.md section 5.

- **VI-50** English number format: *1,000,000; 3.6 triệu.*
- **VI-51** Title Case or ALL CAPS in headings and buttons (§20): *Chọn Tất Cả, Tầm Quan Trọng Của Việc Học.*
- **VI-52** Em or en dash joining clauses (§8).
- **VI-53** *X thất bại* or *X không thành công* in UI errors: write *Không X được*.
- **VI-54** English *On [date], a [event]* frame: *Vào ngày 15 tháng 10 năm 2021, một vụ cháy ...* The long date itself is native (*diễn ra vào ngày 15 tháng 10 năm 2021*); write *Ngày 15/10/2021, ...* or open on the event.
- **VI-55** A space before . , ; : ? or ! (one after), or a comma before *và/hoặc* in a list.
- **VI-56** Decomposed (NFD) characters, or both tone-mark styles in one document.

## Upstream patterns without a tell heading

- §5, §14, §24, §25 and §26 apply as written; VI-02 covers the announcing form of §25.
- §12: VI-14 and VI-20 replace its word list.
- §8, §10, §11 and §21: vi.md section 3a.
