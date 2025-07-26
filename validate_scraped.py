from utils.validators import is_valid_email

def validate_emails(input_file, output_file):
    with open(input_file, "r") as f:
        emails = [line.strip() for line in f if line.strip()]
    valid_emails = [email for email in emails if is_valid_email(email)]
    with open(output_file, "w") as f:
        for email in valid_emails:
            f.write(email + "\n")
    print(f"Saved {len(valid_emails)} valid emails to {output_file}")

if __name__ == "__main__":
    validate_emails("data/scraped_emails.txt", "data/valid_emails.txt")