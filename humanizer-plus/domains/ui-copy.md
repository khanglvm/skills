# UI copy
Applies to: buttons, labels, menus, messages, errors, empty states, onboarding steps, tooltips and i18n strings.
Not for: landing and marketing pages (`landing`), help-centre articles (`technical-docs`), release notes (`release-notes`).

## Reader and purpose

Someone in the middle of a task who reads two words and moves on. Every string either names an action or tells them what happened and what to do next. Follow the product's existing glossary, tone and tone-mark style before this card.

## Structure

- Labels and buttons: verb first, no pronoun ("Try again", "Save", "Not now").
- An error says what failed, then the next step when one is known. Name the cause only when the code knows it.
- Never blame the user: say what is wrong with the input, not what they did.
- Empty state: what is missing, then the action.
- When a service fails, say what still works and keep the rest usable rather than blocking the screen.
- Help text and tooltips are prose: full sentences, a subject where the actor matters, the condition before the action it governs, the fix right after the error it explains.

## Length and format

- Sentence case in both languages (VI-51).
- Prefer the short everyday word. One term per concept across the product.
- i18n: keep placeholders identical to the source string; keys stay ASCII; values are NFC; one tone-mark style per product.
- Leave room in fixed-width controls: Vietnamese strings often run longer than English.
- Uppercase CSS transforms can drop stacked diacritics in fonts without full Vietnamese coverage; check the font before using them.
- Numbers and dates follow vi.md section 5 (`Intl.NumberFormat('vi-VN')`, dd/mm/yyyy).

## Medium tells

- UI strings may drop the subject and use fragments; the chopped-fragment rule (VI-32) applies only to help-text paragraphs.
- English: no "Oops", no exclamation marks in errors, no "Something went wrong" without a next step.
- Internal terms leaking into the product (empty state, end user, onboarding flow, unknown error code, invalid request).

## Vietnamese notes

- Buttons: *Thử lại, Quay lại, Lưu, Tìm hiểu thêm, Để sau*; *Chọn tất cả*, never *Chọn Tất Cả*.
- Short words: *hủy* (not *hủy bỏ*), *nhập* (not *nhập vào*), *ẩn* (not *giấu*), *tìm hiểu* (not *học*).
- Settled strings: *Đang tải…, Đang lưu…, Đã lưu, Cài đặt, Đăng nhập, Đăng xuất, Quên mật khẩu, Tải xuống, Tải lên, Sao chép liên kết, Cho phép, Có gì mới*.
- Calques to replace: *Học thêm* → *Tìm hiểu thêm*; *Đăng nhập vào* → *Đăng nhập*; *Làm tươi trang* → *Tải lại trang*; *Nộp* → *Gửi*; *Định giá* → *Bảng giá* (VI-14 to VI-16).
- Errors: *Không lưu được hình ảnh. Thử lại sau ít phút.* Use *Không ... được*, not *... thất bại* (VI-53). Generic fallback: *Đã có lỗi xảy ra. Vui lòng thử lại.*
- No blame: *Thông tin chưa đúng, vui lòng kiểm tra lại*, not *Bạn đã nhập sai*.
- Replace calqued fillers (*Có vẻ như ..., Có điều gì đó không ổn, Rất tiếc!*) with the fact (VI-15).
- Keep out of the product: *trạng thái rỗng, người dùng cuối, luồng onboarding, mã lỗi không xác định, yêu cầu không hợp lệ*.
- *Vui lòng* appears once, at the action. *Bạn* sparingly. *Quý khách* never appears in a developer tool or a CLI (VI-40).
- Empty state: *Chưa có dự án nào. Tạo dự án đầu tiên.*
- Vietnamese has one plural category. ICU messages use `other` only (`{count, plural, other {# dự án}}`) or plain `"{count} dự án"`; a `one` branch copied from English is a bug.
- Lint string files with `--doctype ui`.

## Review checklist

- Does every button start with a verb, and every error give a next step?
- Is any internal or English-only term visible to the user?
- Does the string fit its control at the longest translation?
- Is the plural block `other`-only and every placeholder intact?

## Sources

Microsoft Vietnamese Localization Style Guide, Mozilla Firefox Vietnamese strings, trussary/vietnamese-language-skill; links in `references/sources.md`.
