import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, app_password, recipient, subject, body, sender_name="Emonigatsaucee"):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = f"{sender_name} <{sender_email}>"
    msg['To'] = recipient
    msg.attach(MIMEText(body, "plain"))


    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        print(f"✅ Sent to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send to {recipient}: {e}")

if __name__ == "__main__":
    sender_email = input("Your Gmail: ")
    app_password = input("App Password: ")
    subject = input("Subject: ")
    body = input("Message Body: ")

    with open("data/valid_emails.txt", "r") as f:
        recipients = [line.strip() for line in f if line.strip()]

    for recipient in recipients:
        send_email(sender_email, app_password, recipient, subject, body)