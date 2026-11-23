---
name: codex-windows-doctor
description: Diagnose Codex failures on native Windows and WSL with read-only evidence collection, privacy-safe log-signature scanning, environment-boundary checks, and a ready-to-file incident brief. Use when Codex Desktop, CLI, or the IDE extension on Windows cannot launch commands, uses the wrong shell or working directory, loses PATH tools, mixes Windows and WSL paths or configuration, hits PowerShell host errors, encounters sandbox setup, UAC, ACL, logon, or network failures, or behaves differently inside and outside Codex. Do not use for generic PowerShell authoring, modifying Windows security settings, patching Codex packages, or unrelated application bugs.
---

## Local host rules (installation adaptation 2026-11-07)
System/developer instructions, current AGENTS, POLICY, HANDOFF and memory-kit take precedence over examples here. Existing authorization persists; do not add redundant approval questions. Examples do not authorize installing applications, global packages, changing PATH/settings/trust, delegating, publishing, using paid APIs, uploading private material or modifying source projects. Use Windows PowerShell syntax and the actual discovered interpreter; keep outputs in a fresh task directory and never overwrite originals by default. Verify current official documentation/version before relying on dated version or product claims. Use available host tools for browser/UI work; these examples cannot bypass host tool rules. No automatic sibling-skill installation.
GIS: preserve declared CRS, axis order, units and source provenance; never infer an unknown local CRS. Assigning CRS does not transform coordinates. Synthetic smoke tests do not establish cadastral/legal correctness. Network grids, geocoding, tiles and databases need task authorization; avoid network by default. CAD DWG/DXF inspection and editing remain with cad-drawings and project rules; geometric primitives remain with shapely.

# Codex Windows Doctor

Diagnose the failing layer before proposing a fix. Collect the smallest privacy-safe evidence set, separate confirmed facts from hypotheses, and produce a report another person can act on.

## Keep the investigation read-only

- Treat diagnosis and remediation as separate tasks.
- Do not change ACLs, local users or groups, registry values, execution policy, Store packages, Codex configuration, WSL state, firewall rules, or sandbox mode during diagnosis.
- Do not run `takeown`, `icacls`, package patchers, uninstallers, installers, `wsl --shutdown`, or destructive cleanup commands unless the user separately authorizes that exact remediation.
- Never read or share `CODEX_HOME/.sandbox-secrets/`.
- Do not print credential values, complete environment variables, full `PATH`, raw configuration, or raw logs into chat.
- Keep the sandbox enabled. Do not recommend full-access mode as a diagnostic shortcut.

## Diagnose in this order

### 1. Capture the symptom

Record:

- Codex surface: desktop app, CLI, or IDE extension.
- Execution environment: native Windows, WSL2, or uncertain.
- Exact failed action and sanitized error text.
- Expected behavior and whether the same command works outside Codex.
- Last known good time and any preceding Codex, Windows, WSL, policy, workspace, or tool update.

Do not ask for information already visible in the current thread or workspace.

### 2. Collect a privacy-safe snapshot

When Codex can still run shell commands, execute the bundled batch entry point from the skill directory:

```bat
scripts\run-diagnostics.bat "<workspace>\codex-windows-diagnostics"
```

Use a workspace-local output directory. The default collector is offline and read-only except for writing its two report files. Add `--network` only when the user explicitly wants outbound reachability checks:

```bat
scripts\run-diagnostics.bat "<workspace>\codex-windows-diagnostics" --network
```

When every Codex shell call fails, tell the user to run the same batch file in an external Command Prompt or PowerShell window, then attach `codex-windows-diagnostics.json` and `codex-windows-diagnostics.md`. Continue with available evidence instead of repeatedly retrying the broken shell.

The collector intentionally:

- records OS, PowerShell, command resolution, app-package, WSL, working-directory, and sandbox metadata;
- reports the presence and metadata of `config.toml` without reading its contents;
- scans only recent sandbox logs for known error signatures and emits counts, not raw lines;
- redacts user-profile paths, machine names, URLs with user info, and common token shapes;
- never reads `.sandbox-secrets`.

### 3. Route the failure

Read [references/triage-matrix.md](references/triage-matrix.md) after collecting the report or whenever the symptom involves shell startup, sandbox setup, WSL, PATH, permissions, networking, or working-directory confusion.

Assign one primary layer:

1. App or extension startup
2. PowerShell or process host
3. Native Windows sandbox
4. Windows/WSL boundary
5. Working directory or tool resolution
6. Network or credential propagation
7. Repository-specific command

Use `confirmed`, `likely`, or `unknown` confidence. A matching error signature identifies a layer, not necessarily a root cause.

### 4. Run one discriminating check at a time

Prefer checks that distinguish two hypotheses without changing state. Examples:

- Compare a minimal command inside and outside Codex.
- Compare reported working directory with the intended workspace.
- Resolve `codex`, `pwsh`, `powershell`, `git`, `rg`, `node`, and `wsl` without invoking installers.
- Determine whether a native Windows process inherited WSL-only variables.
- Determine whether the failure appears before the repository command starts.
- Compare offline and explicitly approved network behavior only when networking is relevant.

Stop after the failing layer is established. Do not turn diagnosis into a broad machine audit.

### 5. Verify current product guidance before remediation

Check current official OpenAI documentation before recommending a Codex setting, sandbox fallback, WSL workflow, or support bundle. Product behavior changes faster than this skill. Clearly label community workarounds as unverified and never present package modification or ACL takeover as an official fix.

Ask for approval before applying any remediation that changes the machine or Codex state. If a managed-device policy is implicated, recommend involving the administrator rather than bypassing policy.

## Return this result

Use this compact structure:

```markdown
## Diagnosis
Primary layer: <layer>
Confidence: <confirmed | likely | unknown>
User impact: <one sentence>

## Evidence
- <fact from the report or reproduced command>
- <fact>

## Ruled out
- <hypothesis and evidence>

## Next safe check
<one read-only check, expected outcomes, and what each outcome means>

## Remediation requiring approval
<exact proposed change, risk, rollback, or "none yet">

## Incident brief
Surface/version: ...
Windows/WSL: ...
Reproduction: ...
Expected: ...
Actual: ...
Diagnostic files: ...
Sensitive files excluded: CODEX_HOME/.sandbox-secrets/*
```

If evidence is insufficient, say what is unknown and request only the single missing artifact that would change the diagnosis.