# Email Credential Checker

You can get information about this project in Turkish and English.

- [Türkçe Dokümantasyon (Varsayılan)](README.md)
- [English Documentation](README_EN.md)

This Python script checks the validity of email credentials from a text file and identifies working and non-working accounts. The script specifically checks credentials for emails with domains `@hotmail.com` and `@outlook.com`. After checking the credentials, the script offers an option to delete non-working accounts from the file.

## Features
- Validates email credentials (username and password) using SMTP.
- Checks only email addresses with the domains `@hotmail.com` and `@outlook.com`.
- Asynchronous operation for checking multiple email accounts.
- Language selection (Turkish or English) saved for future use.
- Option to remove non-working accounts from the input file.

## Prerequisites
- Python 3.x installed on your machine.
- Required libraries listed in `requirements.txt`.

## Installation
1. Clone the repository or download the files.
2. Install the required Python packages using:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use
1. Prepare a `mails.txt` file where each line contains an email and password separated by a colon (`:`). Example:
    ```
    user1@hotmail.com:password1
    user2@outlook.com:password2
    ```
2. Run the script:
    ```bash
    python Checker.py
    ```
3. On the first run, you will be prompted to select a language:
    ```
    Which language you want to use?
    1) Türkçe
    2) English
    ```
   This choice will be saved for future use.
   
4. After the credential checks are complete, you will be asked:
    ```
    Do you want to delete non-working accounts from the file? (Y/N)
    ```

## Files
- `Checker.py`: The main script that performs the email credential check.
- `lang.pkl`: Stores the language preference and language-specific messages.
- `mails.txt`: Input file with email credentials.
- `requirements.txt`: List of dependencies to install.
