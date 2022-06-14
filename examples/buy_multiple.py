# Import the hotmailbox library
import hotmailbox

# Create a user class
user = hotmailbox.User("api_key")

# Purchase 25 Hotmail emails
emails = user.purchase("HOTMAIL", 25)

# Iterate through the list of emails,
# and print the "email" and "password" for each one
for email in emails:
    print(email.email)
    print(email.password)
    print()
