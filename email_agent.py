import imaplib
import email
from email.header import decode_header
from google import genai

import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')

client = genai.Client(api_key=GEMINI_API_KEY)

def connect_to_gmail():
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        print('Connected to Gmail')
        return mail
    except Exception as e:
        print(f"Error connecting to Gmail API: {e}")
        return None

def decode_email_subject(subject):
    if not subject:
        return "Without subject"

    decoded_parts = decode_header(subject)

    decoded_subject = ""

    try:
        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                decoded_subject += part.decode(encoding or "utf-8", errors="ignore")
            else:
                decoded_subject += part
        return decoded_subject

    except Exception as e:
        print(f"Error decoding subject: {e}")
        return subject if isinstance(subject, str) else "Error decoding subject"

def get_email_body():
    body = ""


def get_emails():
    pass

def analyze_emails_with_ai():
    pass

def main():
    pass

if __name__ == '__main__':
    main()