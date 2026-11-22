---
license: MIT
name: youtube-downloader
description: Download authorized video/audio with existing yt-dlp and ffmpeg; inspect metadata and available formats. No automatic dependency or PO Token setup.
---
# Video downloads
Use the user's authorized URL and save location. Check existing files before downloading; do not silently overwrite prior downloads. Playlist and browser-cookie access require authorization. Follow host rules for computer use, authentication and media display.

Run the existing Python interpreter with `scripts/download_video.py URL --info` or `--list-formats`; download with `-o NEW_FOLDER`, optional `--quality 1080p`, `--audio-only`, `--subtitles`. Dependencies must already be installed. Executable discovery uses shutil.which on Windows and Unix. No shell is used by this helper.

Automatic package installation, upgrade, Docker lifecycle and browser PO Token provisioning are disabled, including after 403 errors. `--auto-po-token` is a compatibility no-op with a notice; `--no-auto-po-token` is accepted. `--wpc-browser-path` has no effect while provisioning is disabled. A separate explicitly authorized setup task must review sources, versions and lifecycle before configuring providers; do not execute historical installation recipes. Existing yt-dlp plugins may still affect yt-dlp's behavior.

On failure, report the actual error and limitations; do not promise quality or bypass authentication. The helper may retry progressive formats or a player client, but never installs dependencies. Never print a command containing proxy/cookie credentials. Child output is captured and redacted; cookie-authenticated child output is withheld. Raw returned CompletedProcess is internal evidence and must never be logged. Metadata may be unavailable; oEmbed fallback provides limited fields.

Offline verification 2026-11-07: mocked subprocess tests cover discovery, info/formats/download failures, 403 and credential echo. No real network, Docker, browser, ffmpeg or download was tested. External tools and automatic skill triggering remain unverified. HLS use requires an already available approved tool and secret-safe arguments/output; do not use shell examples from prior versions.
