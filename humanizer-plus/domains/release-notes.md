# Release notes
Applies to: release notes, changelogs, "what's new" entries and internal release summaries.
Not for: commit messages and PR descriptions (`commit-pr`), product announcements written as articles (`article`).

## Reader and purpose

Decide the reader first. User-facing notes describe what changed for the user; an internal release summary lists every ticket for the team. The project's existing changelog format wins over this card.

## Structure

- Version and date at the top (dd/mm/yyyy in Vietnamese, the project's own format in English).
- Group by kind: Added / Changed / Fixed.
- Each bullet starts with a bare verb and names the feature. Hold one tense form per changelog.
- For changed behaviour, label the old and the new (Before / Now). Release notes are where [upstream §25 Writing about the document instead of its subject] allows the previous version.
- Say who is affected and under what condition. Keep scope words exact (only, by default, at most, at least).
- Internal release: before promoting a release to an environment, gather every ticket's changes, including unmerged feature branches, prereleases and work found in past threads, and list anything not yet merged. Ticket keys belong here. Name environments the way each product's team does.

## Length and format

- One line per change; link the full internal record instead of expanding it.
- No emoji per bullet, no bold label on every line (VI-34).
- Out of user notes: commit hashes, build numbers, internal ticket keys, verification methods and counts, and the names of the people who did the work.

## Medium tells

- Vendor-as-subject preamble in internal notes and "We're excited to announce" in English ([upstream §13 Inflated significance]). A B2B customer notice may open with its customary greeting.
- "Improved performance and user experience" with no object. Write what got faster or simpler, from the ticket; if the ticket says nothing more, write the plain change and ask.
- "Minor bug fixes" is honest only when nothing more is known.

## Vietnamese notes

- Groups: *Thêm / Cải thiện / Sửa lỗi*. Bullets: *Thêm tùy chọn "Liên hệ báo phí sau" trong phần thiết lập phí vận chuyển.* Bare verb by default; *Đã thêm / Đã sửa* where the project already writes it that way.
- Old and new: *Trước đây: ...* / *Cập nhật: ...*. Conditions: *chỉ áp dụng cho tài khoản ...*, *từ phiên bản ...*; scope words *chỉ, mặc định, tối đa, ít nhất*.
- Drop *Hệ thống bổ sung ..., Chúng tôi vui mừng thông báo ...* in internal notes. Replace *cải thiện hiệu suất và trải nghiệm người dùng* with the concrete change (VI-20). *Sửa một số lỗi nhỏ* only when nothing more is known.
- Dev terms follow the vi.md terms table: English in internal notes (*fix, deploy, endpoint*), Vietnamese nouns in consumer notes (*lỗi, tệp*).

✗ Chúng tôi rất vui mừng giới thiệu bản cập nhật mới với nhiều cải tiến vượt trội, giúp nâng cao trải nghiệm người dùng một cách toàn diện.

✓
```
Phiên bản 2.4 · 12/11/2026
Thêm
- Xuất danh sách đơn hàng ra tệp CSV.
Sửa lỗi
- Bộ lọc ngày không còn bị mất khi chuyển trang.
```

English: "2.4 · 12 Nov 2026. Added: export the order list to CSV. Fixed: the date filter no longer resets when you change page."

## Review checklist

- Can a user tell from each bullet what changed for them, and under what condition?
- Is the tense form the same in every bullet?
- Did any hash, build number or internal name leak into user notes?
- For an internal release, is every ticket listed and every unmerged change flagged?

## Sources

R2 release-note samples (Base.vn, Haravan) and trussary/vietnamese-language-skill; links in `references/sources.md`.
