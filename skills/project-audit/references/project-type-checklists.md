# Project type checklists

## 1. Project type detection

| Signals | Type |
|---|---|
| Source directories or implementation entry points with a relevant manifest | Code |
| Several business-oriented sections such as audience, product, marketing, analytics, strategy or operations | Product/Business |
| Primarily documentation and reference material | Docs |
| Substantial implementation and business or documentation workflows | Mixed |

Check documented purpose and actual entry points. A package manifest can support utility scripts in a documentation or product project. Count numbered or otherwise prefixed folder names when they fit their documented role. If signals are weak, note the ambiguity and review the documented workflow and file hygiene.

## 2. Code project checklist

| Zone | Check |
|---|---|
| Source | Implementation has a clear entry point and layout |
| Verification | Test or verification instructions match the current workflow |
| Configuration | Project-level configuration is distinguishable from private local settings |
| Build and deployment | Documented commands and references agree with actual files |
| Documentation | Setup and operation instructions are discoverable |
| Dependencies | Declared dependencies and lockfile policy match the documented workflow |

## 3. Product or business checklist

| Zone | Check |
|---|---|
| Audience | Audience records referenced by the project are accessible |
| Product | Description, roadmap and decisions can be found |
| Marketing | Channels and content have a documented home if applicable |
| Analytics | Reports and metrics can be found when the workflow calls for them |
| Operations | Active process instructions have owners or clear entry points where needed |

## 4. Documentation checklist

| Zone | Check |
|---|---|
| Navigation | Readers can find the index and relevant sections |
| Completeness | Required guidance is usable and promised files exist |
| Freshness | Claims and links agree with current sources |
| Cross-references | Important internal links lead to the intended file |

## 5. Severity modifiers table

Judge severity by verified impact and apply the relevant checklists to each part of a mixed project.

| Finding | How to calibrate |
|---|---|
| Broken instruction link | Critical if it prevents an essential workflow. Warning or Low if a working path exists, depending on the impact. |
| Missing entry point | Critical only if users demonstrably cannot access essential material. Warning when it creates material friction. |
| Tracked binaries or generated assets | Consider actual size, stated repository policy, and whether the file is an expected deliverable. |
| Evident secret disclosure | Critical when supported by evidence. Use filenames only to identify possible risks for safe verification. |
| Empty folder or overlapping guidance | Assess whether it misleads users or actually causes drift. |
| Missing ignore coverage | Base severity on observed files and demonstrated risk. |
