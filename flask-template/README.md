# Email Tool Project

This repo contains a Python-based tool for scraping, validating, extracting, and sending emails.  
You can fork this repo and use it for your own educational or research purposes.

## Features

- Scrape emails from web pages
- Validate email addresses
- Extract emails by domain or from files
- Send emails using Gmail and app passwords

## Getting Started

### Prerequisites

- Python 3.8+ (see install guide below)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Gmail account with [App Passwords enabled](https://support.google.com/accounts/answer/185833?hl=en)
- (Recommended) VS Code with:
  - [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

### How to Install Python

#### **Windows (PowerShell):**
1. Download Python from [python.org](https://www.python.org/downloads/windows/).
2. Run the installer and check **"Add Python to PATH"**.
3. Open PowerShell and check installation:
   ```powershell
   python --version
   pip --version
   ```

#### **Linux/macOS (Terminal):**
- **Linux:**
  ```sh
  sudo apt update
  sudo apt install python3 python3-pip
  ```
- **macOS:**
  ```sh
  brew install python
  ```

### Setup

1. **Fork and clone this repo:**
   ```sh
   git clone https://github.com/obapluto-ob/spammingtool.git
   cd spammingtool/email_tool
   ```

2. **Create and activate a virtual environment:**
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate
     ```
   - **Linux/macOS:**
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```sh
   pip install -r data/requirements.txt
   ```

### Usage

- **Scrape emails from a website:**
  ```sh
  python scrape_emails.py
  ```
  Edit the URL in `scrape_emails.py` to your target site.

- **Validate scraped emails:**
  ```sh
  python validate_scraped.py
  ```

- **Extract emails by domain:**
  Edit `extractor.py` and set the domain variable.

- **Send emails:**
  ```sh
  python sender.py
  ```
  Follow the prompts for Gmail, app password, subject, and message.

## Notes

- Only use this tool for ethical and legal purposes.
- Respect website terms of service and privacy laws.
- For Gmail, you must use an App Password (not your regular password).

## Contributing

Feel free to fork, improve, and submit pull requests!

## License

MIT License
