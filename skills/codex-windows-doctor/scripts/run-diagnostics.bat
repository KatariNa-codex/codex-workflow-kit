@echo off
setlocal EnableExtensions

set "SCRIPT_DIR=%~dp0"
set "OUTPUT_DIR=%~1"
if not defined OUTPUT_DIR set "OUTPUT_DIR=%CD%\codex-windows-diagnostics"

set "NETWORK_ARG="
if /I "%~2"=="--network" set "NETWORK_ARG=-IncludeNetworkChecks"

where pwsh.exe >nul 2>nul
if %ERRORLEVEL% NEQ 0 goto try_windows_powershell
pwsh.exe -NoLogo -NoProfile -ExecutionPolicy RemoteSigned -File "%SCRIPT_DIR%collect-diagnostics.ps1" -OutputDirectory "%OUTPUT_DIR%" %NETWORK_ARG%
exit /b %ERRORLEVEL%

:try_windows_powershell
where powershell.exe >nul 2>nul
if %ERRORLEVEL% NEQ 0 goto no_powershell
powershell.exe -NoLogo -NoProfile -ExecutionPolicy RemoteSigned -File "%SCRIPT_DIR%collect-diagnostics.ps1" -OutputDirectory "%OUTPUT_DIR%" %NETWORK_ARG%
exit /b %ERRORLEVEL%

:no_powershell
echo [ERROR] Neither pwsh.exe nor powershell.exe was found on PATH.
exit /b 1