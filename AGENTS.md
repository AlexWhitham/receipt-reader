# Instructions for Coding Agents

- Ask for clarification when requirements or expected behavior are unclear; do not guess.
- Keep instructions, comments, and documentation concise. Put the guidance most relevant to the current task first.
- Write tests that verify observable behavior and would fail if that behavior regressed. Avoid tests that merely repeat implementation details.

## Project Notes

- This is a Python 3.15 uv project. See [README.md](README.md) for setup and the receipt-processing command.
- `GCloud/gcloud_parser.py` owns receipt OCR and parsing. `GCloud/parse_all.py` coordinates configuration, Google Sheets access, and receipt processing.
- `TestThisFirst/` contains manual scripts that access Google services and use machine-specific paths; do not treat them as a safe automated test suite or run them without authorization and valid test credentials.
- There is no configured automated test runner. For changes involving OCR or Google APIs, isolate behavior behind mocks or test doubles so tests do not require credentials, network access, or real receipts.
- Keep credentials, tokens, receipt contents, and personal data out of source control and test output. Avoid introducing machine-specific absolute paths.
- Preserve the existing Poetry dependency and formatting conventions; keep changes focused on the requested behavior.
