# QA Checklist

## Brief and structure

- [ ] Audience, channel, title, target length, and deliverables are explicit.
- [ ] The title appears consistently on the cover, metadata, running header, and opening/closing text where applicable.
- [ ] Concepts are explained before document titles or project tasks are introduced.
- [ ] The article separates facts, plans, inferences, and recommendations.
- [ ] No invented person, dialogue, quote, date, or specific incident appears.
- [ ] A type scenario, if used, is labelled as illustrative and not tied to a real household.

## Data and source scope

- [ ] Every material number has a source marker.
- [ ] Every number has a year, unit, and geographic or population scope.
- [ ] Nature-reserve and biosphere-reserve areas are not mixed.
- [ ] Township population and in-reserve population are not mixed.
- [ ] Sample size is stated and not generalized to the full population.
- [ ] Planned indicators are not written as completed results.
- [ ] Conflicting source values are disclosed in a data note.
- [ ] “Protection recovery” is not assumed to prove a population trend unless measured.

## Text, figures, and tables

- [ ] Figure captions run in sequence: 图1, 图2, ….
- [ ] Table captions run in sequence: 表1, 表2, ….
- [ ] Every figure caption states source, year, and scope.
- [ ] Every table caption or note states source and time period.
- [ ] Values in figures match the body and related tables.
- [ ] Units and rounding are consistent across text, figure, and table.
- [ ] Figure titles do not contradict the caption.
- [ ] Table rows are not stranded alone across pages.
- [ ] Captions are not clipped, overlapped, or reduced below legibility.
- [ ] Infographic text remains readable at the final inserted width.

## Citations and links

- [ ] Reference bookmarks exist as `ref1` … `refN`.
- [ ] Every in-text `[n]` marker points to an existing bookmark.
- [ ] Every reference has at least one incoming citation.
- [ ] Grouped citations link each explicit number.
- [ ] No citation marker is duplicated, for example `[5-9][5-9]`.
- [ ] No DOI or URL string is duplicated.
- [ ] DOI and URL entries are true external hyperlinks.
- [ ] Reference entries contain enough metadata to resolve the source.
- [ ] No source is cited for a claim it does not support.

## Layout and typography

- [ ] Cover uses the prescribed 40 pt title, 12 pt standfirst, and 12 pt metadata.
- [ ] Body uses 12 pt 微软雅黑, 1.3 line spacing, 4 pt after, 0.74 cm first-line indent.
- [ ] Level-1 headings use 15 pt 黑体 bold teal.
- [ ] Level-2 headings use 14 pt 微软雅黑 bold dark ink.
- [ ] Captions and notes use 10 pt grey text.
- [ ] Tables use 8.5 pt body text and the pale green header.
- [ ] Hyperlinks use `#0563C1` with underline.
- [ ] Running header and page number use 9 pt grey.
- [ ] No blank pages, orphaned headings, clipped text, or overlapping objects remain.

## Final proof and package

- [ ] DOCX opens without repair prompts.
- [ ] PDF proof is exported from the final DOCX.
- [ ] Every PDF page is inspected at full size.
- [ ] A contact sheet is inspected for pagination and rhythm.
- [ ] `audit_article.py` returns `PASS`.
- [ ] Expected image, table, and page counts match the delivered document.
- [ ] Build scripts and version notes are retained.
- [ ] Private source files and participant data are excluded from the Git commit.
- [ ] A pull request describes the change and includes audit output.
