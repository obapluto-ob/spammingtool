from extractor import extract_from_file
from sender import send_email

def main():
    # Inputs
    sender_email = input("Your Gmail: ")
    app_password = input("App Password: ")
    subject = input("Subject: ")
    message_body = input("Message Body: ")
    if not message_body:
        message_body = "Hello, this is a test message sent for the tool testing purposes."
    file_path = "data/sample.txt"  # Change if needed

    # Extract
    emails = extract_from_file(file_path)
    print(f"📩 {len(emails)} email(s) found.")

    # Send
    for email in emails:
        send_email(sender_email, app_password, email, subject, message_body)

if __name__ == "__main__":
    main()