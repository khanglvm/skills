# Commit and PR
Applies to: commit messages, pull and merge request descriptions, and squash-merge summaries.
Not for: release notes and changelogs (`release-notes`), review comments on a PR (`workplace`), design docs (`technical-docs`).

## Reader and purpose

A reviewer deciding whether the change is safe to merge, and later a maintainer running `git log` or `git blame` to learn why a line exists. Both want what changed, why, and what could break, without opening every file.

## Structure

- Commit subject: one line in the repository's convention (Conventional Commits, a ticket prefix, or plain imperative), about 50 to 72 characters, no full stop.
- Commit body, when the change needs one: why the change was made and anything the diff does not show. Wrap at the width the repository uses.
- PR description: what changed, why, how it was tested, and what could break or needs a reviewer's eye. Follow `.github/pull_request_template.md` when the repository has one.
- A reverted or replaced approach is mentioned only when the reviewer needs it to judge this one.

## Length and format

- Read `CONTRIBUTING.md` and the last few commits before the first one; match their prefix, case and tense.
- File names, functions, flags and commands in inline code.
- Testing names the commands that ran and their result; a check that did not run is listed as not run.
- Trailers (`Co-Authored-By:`, `Refs:`, `Fixes #N`) exactly as the repository or the brief requires, on their own lines at the end.

## Medium tells

- A subject that restates the diff mechanically ("Update file.py") or inflates it ("Revolutionize the auth flow").
- A body that walks through each file in order instead of saying why.
- A test section that claims coverage no command produced.
- A summary paragraph that repeats the bullet list above it ([upstream §2 One-line closers and dramatic fragments]).
- A labelled bullet for every change ([upstream §19 Bold as decoration]).

## Vietnamese notes

- Subjects and branch names stay ASCII and usually English; a commit body or PR description may be Vietnamese when the team writes that way (vi.md section 5).
- Keep the English dev terms: *commit, merge, rebase, fix, test, review* (VI-17). *cam kết các thay đổi* and *hợp nhất nhánh* are calques.
- Subject-free sentences are normal: *Sửa lỗi bộ lọc bị mất khi chuyển trang.*

## Review checklist

- Does the subject follow the repository's convention and say what the change does?
- Does the body or description say why, and what could break?
- Does every claim about testing match a command that actually ran?
- Are trailers and issue references in the required form?

## Sources

R2 samples (public GitHub PRs and engineering posts) and the repositories' own contributing guides; links in `references/sources.md`.
