import re

def extract_emails_from_file(filepath, domain=None):
    with open(filepath, 'r') as file:
        content = file.read()
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content)
    emails = list(set(emails))
    if domain:
        emails = [email for email in emails if email.lower().endswith(f"@{domain.lower()}")]
    return emails

# Example usage:
if __name__ == "__main__":
    # Change domain to filter, or set to None for all emails
    domain = None  # e.g., "chase.com" or None
    extracted_emails = extract_emails_from_file("data/scraped_emails.txt", domain=domain)
    print(extracted_emails)