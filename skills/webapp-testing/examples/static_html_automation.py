from argparse import ArgumentParser
from pathlib import Path

from playwright.sync_api import expect, sync_playwright


def main():
    parser = ArgumentParser(description="Verify a local HTML test fixture")
    parser.add_argument("html", type=Path)
    parser.add_argument("screenshot", type=Path)
    parser.add_argument("--browser", type=Path)
    args = parser.parse_args()

    source = args.html.resolve(strict=True)
    output = args.screenshot.resolve()
    if source.suffix.lower() not in (".html", ".htm") or output.suffix.lower() != ".png":
        parser.error("Choose a local HTML fixture and a new PNG output")
    if output.exists():
        parser.error("Screenshot path already exists")

    with sync_playwright() as playwright:
        options = {"executable_path": str(args.browser.resolve(strict=True))} if args.browser else {}
        browser = playwright.chromium.launch(**options)
        try:
            page = browser.new_page()
            page.route("http://**/*", lambda route: route.abort())
            page.route("https://**/*", lambda route: route.abort())
            page.goto(source.as_uri())
            page.get_by_role("button", name="Run check").click()
            expect(page.get_by_role("status")).to_have_text("PASS")
            screenshot = page.screenshot()
        finally:
            browser.close()
    with output.open("xb") as file:
        file.write(screenshot)
    print("Local fixture passed")


if __name__ == "__main__":
    main()
