# Codex Windows triage matrix

Use this matrix to classify evidence. Error signatures are routing clues, not proof of a specific fix.

## 1. App or extension startup

| Evidence | Likely boundary | Next read-only check |
|---|---|---|
| App never opens, freezes before a task starts, or IDE extension is unresponsive | UI, packaged runtime, or extension host | Record surface and version; test whether `codex --version` works in an external terminal |
| Codex CLI works but Desktop does not | Desktop packaging or app-host boundary | Record AppX metadata and whether the bundled/selected CLI path resolves |
| Failure started immediately after an update | Version or packaged-resource drift | Record current version and last-known-good version; do not patch the package |

## 2. PowerShell or process host

| Signature or observation | Interpretation | Discriminating check |
|---|---|---|
| `8009001d`, internal PowerShell host error, or command fails before producing output | Host/session startup failed before repo work | Run `powershell.exe -NoLogo -NoProfile` and `pwsh -NoLogo -NoProfile` outside Codex |
| Commands work externally but every Codex command fails | Codex-hosted process environment or sandbox boundary | Compare `SystemRoot`, `windir`, shell version, and command resolution; do not dump all environment values |
| PowerShell syntax alone fails but `cmd.exe /c ver` succeeds | Shell-language or quoting issue | Reduce to a one-line shell-neutral command and classify separately from sandbox setup |

## 3. Native Windows sandbox

| Signature | Route |
|---|---|
| `orchestrator_helper_launch_failed` or helper not found | Sandbox helper discovery or packaged-resource boundary |
| `CreateProcessWithLogonW failed` / `CreateProcessAsUserW failed` | Sandbox-user logon or process-creation boundary |
| Error `2` | File or helper path not found |
| Error `5`, `Access is denied`, or `SetNamedSecurityInfoW failed: 5` | Permission or ACL boundary |
| Error `740` / `ERROR_ELEVATION_REQUIRED` | Elevation requirement was not satisfied in the launch path |
| Error `1223` | User canceled or the elevation prompt could not complete |
| Error `1326`, `1385`, or `1909` | Sandbox-user credential, logon-right, or account-policy boundary |
| Commands run but stdout is empty | Capture/transport boundary after process launch |

For managed devices, record policy context and involve the administrator. Never bypass policy by taking ownership of WindowsApps or changing sandbox-user rights without explicit authorization and a rollback plan.

## 4. Windows/WSL boundary

| Evidence | Interpretation | Next check |
|---|---|---|
| Native Windows process has `WSL_DISTRO_NAME` set | Possible leaked WSL environment marker | Confirm selected agent environment and process path before changing the variable |
| Intended WSL task reports `powershell` and a `C:\...` working directory | Windows runner may be handling a WSL workspace | Compare app environment selection, workspace URI, and actual process working directory |
| `CODEX_CLI_PATH` points to a Windows `.cmd` but WSL tries to execute it | Binary/path type mismatch | Resolve Codex independently inside Windows and inside WSL |
| WSL repo is under `/mnt/c` and feels slow or has permission/symlink issues | Cross-filesystem overhead | Compare with a small repo under the WSL Linux home; do not move the real repo during diagnosis |
| Windows and WSL show different skills, config, or credentials | Separate home directories and tool installations | Record both `CODEX_HOME` locations and command paths without copying secrets |

## 5. Working directory or tool resolution

| Evidence | Interpretation | Next check |
|---|---|---|
| Codex reports the workspace but command output comes from `C:\` or another root | Workdir propagation or sandbox junction issue | Run a read-only current-directory command and compare with the task workspace |
| Tool exists externally but not inside Codex | PATH inheritance, sandbox visibility, or command shadowing | Compare `Get-Command <tool> -All` results and source paths |
| Tool resolves inside WindowsApps or an unexpected package directory | Packaged executable visibility may differ in sandbox | Record the path and file metadata; do not copy or alter the package |
| Only the repository build/test fails | Repo-specific issue is more likely | Re-run the exact command outside Codex with the same working directory and inputs |

## 6. Network or credential propagation

| Evidence | Interpretation | Next check |
|---|---|---|
| Host terminal reaches a service but sandbox does not | Sandbox network policy or partial setup | Confirm the task's network permission and run an explicitly approved TCP reachability check |
| Network works but `gh`, package manager, or MCP auth fails only in Codex | Credential-store or environment propagation boundary | Check authentication status without printing token values |
| Both host and Codex fail | Machine, proxy, DNS, VPN, or service issue | Diagnose outside Codex first |

## Escalation bundle

Include:

- Surface and exact version
- Windows version and architecture
- Native Windows versus WSL2
- Sandbox mode if known
- Sanitized exact error
- Minimal reproduction
- Whether the same command works outside Codex
- `codex-windows-diagnostics.json` and `.md`

Exclude:

- `CODEX_HOME/.sandbox-secrets/*`
- API keys, tokens, cookies, credential-store exports, or complete environment dumps
- Raw `config.toml` unless the user reviews and sanitizes it
- Full logs without manual privacy review