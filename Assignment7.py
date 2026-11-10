import re

# Sample text
text = """
"""

# Regular expression pattern for email
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the email addresses
print("Email addresses found:")

for email in emails:
    print(email)
