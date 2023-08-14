import openpyxl
from verify_email import verify_email

def verify_emails_from_excel(filename):
    try:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        email_column = sheet['A']  # Assuming emails are in the first column

        for cell in email_column:
            email = cell.value
            if email:
                status = "Verified" if verify_email(email) else "Not Verified"
                cell.offset(column=1).value = status
                print(f"Email: {email}, Status: {status}")

        workbook.save(filename)

        print("Verification status updated successfully.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    excel_filename = "emails.xlsx"
    verify_emails_from_excel(excel_filename)
