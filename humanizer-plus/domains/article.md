# Article
Applies to: blog posts, essays, features, case studies, opinion pieces and news-style write-ups.
Not for: research write-ups and analyses (`report`), tutorials and guides (`technical-docs`), social posts (`social`).

## Reader and purpose

A stranger who arrives from a search or a link and owes the writer nothing. They stay when they can picture the problem before the first tool, term or acronym. When the repository has its own article guide, read all of it first; this card fills only what it leaves out.

## Structure

- Open with a situation the reader can picture, and say whose problem it is.
- For something the writer made, use this order: the problem as a concrete situation; the idea and why; what the thing is, with an everyday comparison before the technical name; each part tied back to the opening situation in the order the reader would meet it; the writer's role, the current state, and what they would tell someone trying the same.
- Headings name a moment the reader recognises ("When the agent gets the request", "Khi QA nhận ticket"). A heading that states advice or an abstract idea gives the reader nothing to hold.
- End on the last concrete fact, a quote or the open question (VI-03, [upstream §13 Inflated significance]).
- Two language editions are each written natively for their readers. Structure, headings, paragraph order and examples may differ; facts, links, images, ownership and uncertainty must match.

## Length and format

- A stranger with no context should understand from the title what problem the piece is about. Everyday problem first; tool names can come in the excerpt or body.
- No full stop at the end of a title, at most one colon, sentence case (VI-51).
- The excerpt or sapo is one sentence of about 20 to 35 words that carries the main fact and adds to the title instead of repeating it.
- Keep each `title`/`seoTitle` and `excerpt`/`seoDescription` pair consistent and inside the project's length limits.
- Keep every fact, link, image and `<details>` block. Frontmatter keys, slugs, image paths and URLs stay unchanged unless the project guide says otherwise.

## Medium tells

- Connected sentences: join related ideas with real connectives, keep a short sentence for a question or a real turn, and bridge every new fact to the one before (VI-32).
- Read each sentence as a first-time reader: every pronoun and relation word has one target (VI-31).
- Introduce a term once in everyday words, then use it bare. A vague noun becomes what it does for the task.
- Ownership: a tool the writer created is introduced as their creation ("I built", "I made"; "maintain" only for upkeep). Show their part through what they do: the workflow they set, the changes they control and review, how they check an agent's work. Keep authorship qualifiers (much, most) accurate.
- A hypothetical reads as hypothetical. No invented incidents, numbers, people, results or feelings.
- Workplace implementation details stay private; describe client companies by sector, never by name.

## Vietnamese notes

- Draft the Vietnamese edition with the write-from-meaning step (vi.md section 1), never by translating the English sentences.
- Titles stay short and carry only the core contrast. Qualifiers such as *đã được xác minh* move to the sapo or first paragraph.
- *mình* for a personal blog; otherwise use the vi.md register row. Describe a feature in plain words rather than a calqued command name. A tool the writer created: *Mình tạo ra X để ...*, never *Mình duy trì X*.
- Column voice may use *tôi/mình*, particles (*cơ, chứ, nhỉ*) and a dry aside when the writer's sample does. Explanation stays neutral (VI-42).
- News-style pieces: time marker first (*Chiều 1/11, ...*), a person introduced once with full name and (age, place), the spaced hyphen for apposition (vi.md section 3a).

## Review checklist

- Can a first-time reader picture the situation before the first tool or term?
- Do the headings name moments in the story, and does each part tie back to the opening?
- Would a visitor with no context understand the title and excerpt?
- Is the writer introduced as the creator of their tools, with their role shown through actions?
- Does each language read as if it had been written in that language?
- Did the project's own checks run (locale check, build), where it has them?

## Sources

R1 journalism notes (titles, sapo, endings) and the writer's own article guide; links in `references/sources.md`.
