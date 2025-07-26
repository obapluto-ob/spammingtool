from extractor import extract_emails_from_file

def save_leads(input_file, output_file, domain=None):
    emails = extract_emails_from_file(input_file, domain)
    with open(output_file, 'w') as f:
        for email in emails:
            f.write(email + '\n')
    print(f"Saved {len(emails)} leads to {output_file}")

if __name__ == "__main__":
    # Change domain to filter, or set to None for all emails
    save_leads("data/sample.txt", "data/leads.txt", domain=None)