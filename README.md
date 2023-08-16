# BULK-EMAIL-VERIFIER-PYTHON

BULK-EMAIL-VERIFIER-PYTHON is a Python script that verifies a list of email addresses stored in an Excel file using the `openpyxl` library to read the Excel file and the `verify-email` library to validate email addresses based on domain MX records.

## Features

- Reads email addresses from an Excel file.
- Validates email addresses based on domain MX records using the `verify-email` library.
- Updates the verification status in the Excel file.
- Provides clear verification results for each email address.

## Requirements

- Python 3.6 or higher
- `openpyxl` library
- `verify-email` library

## Usage

1. Install the required libraries:

   ```bash
   pip install openpyxl verify-email

-Prepare an Excel file with a column containing email addresses.
-Clone or download this repository.
-Run the script:
    python bulk_email_verifier.py


-The script will verify the email addresses and update the Excel file with verification status.

-Example
-Assuming you have an Excel file named emails.xlsx with email addresses in the first column:

Email
email1@example.com
email2@example.com
email3@example.com

-After running the script, the Excel file might look like this:

Email               Verification Status
email1@example.com  Verified
email2@example.com  Not Verified
email3@example.com  Verified

-This script checks the validity of email addresses based on domain MX records but doesn't guarantee active usage.
-For improved accuracy, consider additional verification methods.
