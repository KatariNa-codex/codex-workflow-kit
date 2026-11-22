# Audit checklists

## Instructions

- Review in-scope instructions and the sections referenced by the documented workflow. Record any read limits.
- Follow local paths relative to the referring document or explicitly documented base. Inspect file metadata before opening a linked document. Check paths and local links and compare directory descriptions to actual layout. Verify external links only if authorized and relevant to the request.
- Check for conflicting applicable rules, unfinished sections that impede work, and guidance contradicted by current evidence. Dates alone do not establish staleness. A child override within its scope may be intentional.
- Compare duplicated rules with project memory where available. Flag conflicting versions or substantial drift. Redact apparent secret values encountered incidentally.

## Project memory discovery

1. Check project-documented memory and in-scope local `MEMORY.md` or `memory/`. For optional memory-kit, use the active profile selected by the host. Use `CODEX_HOME` when it identifies that profile, otherwise the known active home, commonly `~/.codex` for a default profile. Do not fall back to the default when an alternate active profile is known. If the active profile cannot be confirmed, skip profile-backed memory lookup.
2. Read the active profile's `memory-kit.json` only for `projects_dir` and, if needed to disambiguate project boundaries, `root`. Parse locally and keep other fields out of output. An absent, unreadable, or unusable configuration means this lookup is unavailable. Never inspect the native Codex memory store or import other profiles. The configured `projects_dir` may be outside the profile. Inspect only the verified project's memory folder there.
3. Normalize the resolved native absolute path of the project, using the project root selected during reconnaissance. On Windows use the verified long native project path, rather than a DOS 8.3 alias or a path translated by another shell. Replace every character outside ASCII `A–Z`, `a–z`, and `0–9` with one hyphen. For example, the Windows path `C:\Example\My_Project` yields `C--Example-My-Project`. On Windows match the slug case-insensitively and use the actual directory spelling. Use only the existing `<projects_dir>/<matched-slug>/memory` directory. Verify the association against the project if the slug is ambiguous, especially when different paths normalize to the same name. Read no neighboring memory contents.
4. If no relevant memory is verified, mark the area skipped. Do not infer broken hooks or create new memory files from absence.

### Memory checks

- Check `MEMORY.md` and `INDEX.md` links, when present. Read linked entries within the verified project memory only, following important project references one level deep. Report sampling limits.
- Check orphan rule and reference files only where the indexes are intended to be exhaustive together. An entry in an overflow index counts. Exclude indexes, archives, and journals from orphan checks. Where documented or verified as generated, recommend editing the owning source, such as the entry's `metadata.index_line` or an index header template, instead of the assembled index.
- Check each sampled entry against the active memory schema, if documented. A memory-kit rule may use `name`, `description`, and `metadata.type`; older entries may use top-level `type`. Assess confirmed obsolete entries, broken local references, contradictory duplicates, or unclear status.
- Review memory purpose and scope. Keep unrelated project records and private conversations outside the audit.

## File structure

- Review the [project-type reference](project-type-checklists.md) and compare it with the documented workflow.
- Inspect the root and a representative set of directories. Check for missing areas the workflow actually expects, unexpected root clutter, duplicate filename patterns, temporary files, empty planned directories, or misplaced assets. Filename patterns are candidates, not proof of duplication. Consider whether root documents, media or site files serve a clear purpose.
- Check sizes using metadata. Files over 1 MB are candidates for inspection when they affect sharing, storage, or the workflow. Keep large deliverables and normal project assets in context.
- For shell discovery prefer `rg --files` with exclusions, or native file listing. On Windows use `Get-ChildItem -LiteralPath` and cap printed output with `Select-Object -First`. Inspect excluded directories only when the audit requires it. Do not follow symlinks or junctions into unrelated directories.

## Git hygiene

- In Full only, use the verified project root with read-only operations. For Git status use `git --no-optional-locks -C <project> status --short`. Scope file commands to the audited project when its Git work tree includes other projects, and limit the output. Check paths with `git ls-files` or ignore rules with `git check-ignore`; use `git log` locally only when relevant.
- Look at representative tracked and untracked path names, ignore coverage, relevant generated paths, and asset sizes. Flag ignore issues only where coverage is expected and ineffective. Document work in progress based on evidence.
- Flag tracked filenames suggestive of credentials for safe verification. Treat a filename as a risk indicator. Never open secret files, search history for values, show raw diffs containing sensitive text, or claim that a name proves a disclosure. Account for clearly designated template paths.
- If Git is absent or its root points at an unrelated enclosing repository, skip repository-wide review and explain the scope limit.

## Automations

- In Full only, inspect existing project-declared policies, workflows, hooks and integrations relevant to the project. Separate a declaration from availability, trust and successful execution. Do not run or validate externally.
- When settings matter, use declarations such as project `.codex/config.toml`, `.codex/hooks.json`, and relevant CI files only if present and applicable. Consult the active profile only for a specifically identified setting necessary for this project. Use a structured parser or safe filtering for expected field names and in-scope relative paths. Keep credentials, inline commands, environment values, external service endpoints and raw configuration out of output. When safe extraction is unavailable, report limited coverage.
- Verify static references when their target is within authorized scope, and note whether dynamic paths or host state could be checked. Recommend changes only for demonstrated workflow needs. Missing optional hooks, MCP servers, CI, tests, or settings are not findings by themselves.
