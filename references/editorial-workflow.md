# Editorial Workflow

## 1. Lock the brief

Record:

- audience and channel;
- target length and reading time;
- required title and subtitle;
- required sections;
- DOCX/PDF deliverables;
- visual treatment and number of figures;
- source files the author explicitly permits;
- facts that cannot be changed.

Do not infer permission to use private reports publicly. The skill repository must stay free of source PDFs, participant data, and unpublished article files.

## 2. Build a claim ledger

Create a table before drafting:

| ID | Claim or value | Scope | Year | Unit | Source | Page/section | Status | Used in |
|---|---|---|---|---|---|---|---|---|
| C01 | 16110.7 | world biosphere reserve | after expansion | ha | Community plan | 1.2 | fact | opening/data section |
| C02 | 40 | first-batch project budget | 2026 | 万元 | Annual project | 3 | plan | research section |

Use `fact`, `plan`, `inference`, or `recommendation` in the status column. If the source itself has two values, record both and use an audit note instead of silently choosing one.

### Scope traps

Check these separately:

- national nature reserve vs expanded world biosphere reserve;
- surrounding township population vs population inside the reserve;
- species records vs population trends;
- planned indicators vs measured outcomes;
- 2023 survey sample vs full community population;
- national protected wildlife total vs first-class subset.

## 3. Resolve source conflicts

When two values in one source disagree:

1. Quote both.
2. Prefer the detailed, itemized statistic that can be reconstructed.
3. Add a note in the data-limitations appendix.
4. If a public agency must settle the number, state that it needs final confirmation.

Do not make the body look more certain than the source.

## 4. Explain the concept before the document

For a policy, plan, or project:

1. Explain the underlying concept in plain language.
2. Explain why the document exists.
3. Explain the implementation path.
4. Then list the document's tasks, budget, and outcomes.

Useful plain-language moves:

- “community sustainable development” → a five-year route map;
- “ecological product value realization” → an asset inventory for ecological goods and services;
- “human-wildlife conflict assessment” → a risk check-up covering ecology, loss, perception, compensation, and behaviour.

Do not present a plan as a completed outcome.

## 5. Choose the narrative

For a popular-science DOCX, use a sequence such as:

1. factual hook or clearly labelled type scenario;
2. concept definition;
3. local data with scope and source;
4. mechanism and social consequence;
5. governance or research path;
6. limitations and uncertainty;
7. closing callback.

A type scenario may be used to make a mechanism concrete, but label it as illustrative and remove names, dialogue, exact dates, and identifiable details.

## 6. Draft in the house voice

- Prefer concrete subjects and verbs.
- Keep paragraphs short enough for mobile reading.
- Use rhetorical questions sparingly.
- Explain technical terms at first use.
- Avoid repeated “不是……而是……” constructions and slogan-like triads.
- Do not use adjectives where a number, comparison, or mechanism can do the work.
- Do not claim that a source proves more than it does.
- Keep “protection success”, “livelihood pressure”, and “governance capacity” as separate variables.

## 7. Plan visuals with the text

Before making a figure, write its one-sentence takeaway. Then decide whether it needs a table, a chart, a map, a pathway diagram, or no visual at all.

Each visual needs:

- figure or table number;
- title;
- unit and scope;
- year;
- sample size or population when relevant;
- source marker;
- note when data are a plan, estimate, or illustrative pathway.

Check the figure against the body text and the nearest table. Do not allow the image and caption to tell different stories.

## 8. Build the DOCX

Use `references/house-style.md`. Keep content in editable text and tables rather than flattening the article into page images. Use images only for infographics and photographs.

Recommended section skeleton for this project family:

1. 导语
2. 一、什么是“人兽冲突”？
3. 二、车八岭：北纬24°的“物种宝库”
4. 三、山的外面，就是家
5. 四、冲突的根源：两组数字的碰撞
6. 五、2026年新方案：给冲突“建档”、做“体检”、开“药方”
7. 六、研究建设方案：用年度项目承接社区规划
8. 七、治冲突，也是找出路
9. 八、更大的图景
10. 附录A：数据口径与限制说明
11. 附录B：参考文献

Keep the order only if it serves the brief. Stability of section numbering matters more than copying this outline into unrelated articles.

## 9. Wire citations

Use Word bookmarks named `ref1` through `refN`. In-text `[n]` markers should be true internal hyperlinks. For grouped citations:

- link each explicit number in `[10,11,21]`;
- link range endpoints or the whole range consistently;
- ensure every reference has at least one incoming citation;
- ensure every internal anchor exists;
- put DOIs and URLs in the reference entry as external hyperlinks;
- never duplicate a citation marker or a DOI string during rebuilds.

## 10. Render and audit

1. Run `python scripts/audit_article.py article.docx --pdf article.pdf --expect-images N --expect-tables N --expect-pages N`.
2. Export the DOCX to PDF with Word COM on Windows if available.
3. Render every page to PNG.
4. Inspect the cover and all data pages at full size.
5. Create a contact sheet and inspect pagination, blank pages, orphaned headings, and image rhythm.
6. Re-run the audit after any final edit.

## 11. Version and collaborate

Use one repository for the skill, not one repository per article. Keep article deliverables in their own project folders.

Suggested Git workflow:

- `main`: validated shared version;
- `feat/<topic>`: new style or workflow addition;
- `fix/<topic>`: correction;
- pull request with audit output and screenshots of changed pages;
- update `CHANGELOG.md`;
- never commit private source files or generated PDFs unless the team intentionally decides to publish them.

Suggested changes to the skill should include:

- what changed;
- why the change is reusable;
- which reference or script was updated;
- test command and result;
- a before/after example if the visual style changed.
