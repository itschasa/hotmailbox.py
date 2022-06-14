# Import the hotmailbox library
import hotmailbox

# Create a user class
user = hotmailbox.User("api_key")

# Purchase a Hotmail email
emails = user.purchase("HOTMAIL", 1)

# Get the first entry from the list of emails,
# and print the "email" and "password" of it
print(emails[0].email)
print(emails[0].password)
