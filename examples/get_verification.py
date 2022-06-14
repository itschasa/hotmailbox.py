# Import the hotmailbox library
import hotmailbox

# Create a user class
user = hotmailbox.User("api_key")

# Purchase a Hotmail email
emails = user.purchase("HOTMAIL", 1)

# Fetch and print verification codes/links from each platform
print(emails[0].discord())
print(emails[0].facebook())
print(emails[0].amazon())
print(emails[0].twitter())
