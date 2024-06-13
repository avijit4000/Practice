import re


def find_emails(text):
    # Regular expression pattern for matching email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches of the pattern in the text
    emails = re.findall(pattern, text)

    return emails


# Example usage:
text = "Contact me at john@example.com or jane.doe@example.co.uk, avijit4000@gmail.com"
emails_found = find_emails(text)
print("Email addresses found:", emails_found)
