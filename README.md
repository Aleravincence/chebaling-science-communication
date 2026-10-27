# Chebaling Science Communication Skill

A reusable Codex skill for producing sourced Chinese science-popularization DOCX articles with the Chebaling editorial and visual system.

The skill captures the workflow developed for the article “车八岭的人兽冲突：从成因，到多步治理，让绿水青山成为‘铁饭碗’”. It covers concept explanation, data-scope checks, figure and table QA, citation hyperlinks, page layout, typography, line spacing, Word-to-PDF proofing, and team version control.

## What is included

- `SKILL.md`: entrypoint and non-negotiable workflow.
- `references/house-style.md`: measured A4 layout, fonts, sizes, spacing, colours, captions, tables, infographics, and pagination.
- `references/editorial-workflow.md`: claim ledger, source-scope checks, section blueprint, drafting, citation wiring, and versioning.
- `references/qa-checklist.md`: data, chart, table, citation, layout, and delivery checks.
- `scripts/audit_article.py`: mechanical DOCX/PDF audit.
- `scripts/style_snapshot.py`: extract page and typography tokens from a DOCX.
- `scripts/render_proof.py`: render PDF pages and a contact sheet for layout review.

## Install

Clone the repository into your Codex skills directory:

```powershell
git clone <repository-url> "$env:USERPROFILE\.codex\skills\chebaling-science-communication"
```

Restart Codex after installation so the skill is discovered.

## Use

Invoke it explicitly when you want a repeatable result:

```text
Use $chebaling-science-communication to revise this conservation article with sourced data, consistent figures, and linked references.
```

Typical request:

```text
Use $chebaling-science-communication. Rewrite and lay out this DOCX for a WeChat-style science audience. Preserve all verified figures, label illustrative scenarios, keep figures/tables/body consistent, and produce a PDF proof.
```

## Validate an article

```powershell
python scripts/audit_article.py article.docx --pdf article.pdf --expect-images 5 --expect-figures 5 --expect-tables 2 --expect-pages 19
```

For a machine-readable report:

```powershell
python scripts/audit_article.py article.docx --json
```

Inspect the actual formatting of a master document:

```powershell
python scripts/style_snapshot.py article.docx --output style-snapshot.json
```

Render a PDF proof and contact sheet:

```powershell
python scripts/render_proof.py article.pdf --pages-dir proof-pages --contact proof-contact.png
```

## Team workflow

- `main` is the validated shared version.
- Use `feat/<topic>` for new rules or scripts.
- Use `fix/<topic>` for corrections.
- Open a pull request with the audit result and screenshots of changed pages.
- Update `CHANGELOG.md` for user-visible workflow or style changes.
- Do not commit private planning documents, source PDFs, participant data, or unpublished article files.

See `CONTRIBUTING.md` for the review checklist.

## Scope

This skill is intended for evidence-based conservation, ecology, heritage, and community-development communication. It is not a licence to invent local evidence or to present a plan as an outcome.

