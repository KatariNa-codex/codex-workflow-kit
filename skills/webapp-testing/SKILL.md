---
name: webapp-testing
description: Check the behavior of an authorized web application, using host UI capabilities or a local test fixture. Use for verifying controls, forms and status feedback.
---

# Web App Testing

Use the tools authorized by the host and the user. Define what action to test and what should change on screen. For a local static fixture, use the Playwright example in examples/static_html_automation.py. It takes the path of the HTML file, an output path, and an optional local browser executable. The fixture must provide a button named Run check and a status element with an accessible status role that changes to PASS when the button is used.

Install Python with Playwright in an isolated project environment. The example accepts an installed compatible Chromium browser through the browser option. The browser uses an isolated context. Run the script with --help for the exact arguments. Use a fresh output file. Other app flows require app-specific assertions and authorized tools.
