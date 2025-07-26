import os

os.system("python scrape_emails.py")
os.system("python validate_scraped.py")
os.system("python sender.py")  # Make sure sender.py reads from data/valid_emails.txt