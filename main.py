r"""
Phone number and email searcher.

"""

# Import re and pyperclip
import re
import pyperclip

# Get text from clipboard
# pyperclip.paste() will be the text in your clipboard
text = pyperclip.paste()

# Search for phone numbers + emails
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')  # This compiles a regex pattern for phone numbers in the format 123-456-7890
email_regex = re.compile(r'\w+@\w+\.\w+')  # This compiles a regex pattern for email addresses in the format user@domain.extension

phone_numbers = phone_regex.findall(text)  # This finds anything with the phone number pattern in the text and returns them as a list
emails = email_regex.findall(text)  # This Finds anything with the email pattern in the text and returns them as a list

# Replace text in keyboard with found phone numbers and email
# pyperclip.copy() will put the new text back onto the clipboard
results = ('\n'.join(phone_numbers + emails))

pyperclip.copy(results)

print('Copied to clipboard:')
print(results)