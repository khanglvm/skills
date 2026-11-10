# Workplace
Applies to: Jira and issue comments, Outline comments, team chat, code-review comments, handoffs, status updates and internal notes.
Not for: PR descriptions and commit messages (`commit-pr`), external email (`email`), reports and analyses (`report`).

## Reader and purpose

A colleague who must act: test, decide, unblock or pick up the work. They read the first line and skim the rest. Before a ticket comment, check the team's current channels and the ticket history for context, and use the people-in-charge the team has recorded. This card sets the wording; it grants no permission to post.

## Structure

- Lead with the result and the next action, then the owner and the link. One request per message when the reader must act.
- Add a technical detail only when the recipient needs it to act or diagnose, or asks for it. Keep material blockers and uncertainty, and keep untested and blocked behaviour explicit.
- A clarification names the concrete missing decision or reproduction data.
- A handback is comment, status and verified owner together; a question alone is incomplete.
- A section about handing work over describes what was checked and what is handed over, not an abstract conclusion.

## Length and format

- Routine hashes, build numbers and URLs, verification methods and counts, compression details and checksum lists stay in supporting records. Link the useful attachment or field contract instead of repeating it.
- An API method and endpoint go in a code or noformat block with brace placeholders intact. An image gets a caption saying what it shows, not a raw attachment number.
- After tagging a person, continue the message without repeating their name.
- When the team's protocol marks agent-written comments (for example a fixed first line), follow it exactly, with a real newline after the marker, never a literal `\n`.
- Chat: one action per line; tag the person and say what to attach.

## Medium tells

- Preamble and closing offers: "Just wanted to flag", "Quick update", "Let me know if you need anything" ([upstream §22 Chatbot residue]).
- Re-explaining the thread to someone who wrote it ([upstream §26 Re-explaining what the reader knows]).
- Roles named in the agent's words instead of the team's. Use the team's own titles (QA, QC, BE Dev, PM).
- Review comments that address the author instead of the change.

## Vietnamese notes

- Ticket and wiki comments: subject-free prose (*Đã fix lỗi ..., Cần QA kiểm tra lại ...*), no *nhé* or *nghe*, no emoji beyond a protocol marker. Never infer an honorific (VI-41); missing saved context establishes none.
- For an unknown recipient write *người nhận bàn giao* (or *người nhận handover*); never *người kiểm tra*, and do not default to *người tiếp nhận*.
- Describe QA work as *kết quả kiểm thử* or the concrete checks, screenshots and logs. Here *bằng chứng* reads as accusatory.
- Chat: *nhé* and *nghe* are fine (*nghe* is southern, so match the thread). *Đã* or *rồi* carries the status: *Đã deploy lên staging rồi nhé.* English dev terms with Vietnamese grammar, no gloss (vi.md section 5).
- Code review addresses the change: *Chỗ này nên tách thành hàm riêng.* *Có thể dùng map thay cho vòng lặp ở đây không?*

✗ Tôi đã hoàn thành việc sửa lỗi cho chức năng lọc đơn hàng. Anh vui lòng kiểm tra lại giúp em ạ.

✓ Đã fix lỗi bộ lọc đơn hàng bị mất khi chuyển trang. QA kiểm tra lại theo các bước trong mục Test steps; ảnh "Bộ lọc sau khi chuyển trang" là kết quả kiểm thử trên staging.

## Review checklist

- Does the message start with the result, and does it follow the team's comment protocol?
- Would the recipient need anything that is missing, or is anything there that they do not need?
- Is every role named as the team says it, with no inferred honorific?
- If this is a handback, are the status and owner set in the same step?

## Sources

R2 workplace samples (public issue threads, engineering blogs) and trussary/vietnamese-language-skill for the review sentences; links in `references/sources.md`.
