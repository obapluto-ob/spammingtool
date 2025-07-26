import requests
import re
from bs4 import BeautifulSoup
from utils.validators import is_valid_email
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_emails_from_url(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    emails = re.findall(r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b', text)
    emails = list(set(emails))
    return emails

if __name__ == "__main__":
    url = "https://kmtc.ac.ke/"  # Change to your target website
    emails = scrape_emails_from_url(url)
    valid_emails = [email for email in emails if is_valid_email(email)]
    print("Valid emails:")
    for email in valid_emails:
        print(email)

    # Save only valid emails to a file
    with open("data/scraped_emails.txt", "w") as f:
        for email in valid_emails:
            f.write(email + "\n")
    print(f"Saved {len(valid_emails)} valid emails to data/scraped_emails.txt")