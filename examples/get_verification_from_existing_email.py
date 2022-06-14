# Import the hotmailbox library
import hotmailbox

# Create an email class, using an email and password
email = hotmailbox.Email("email", "password")

# Fetch and print verification codes/links from each platform
print(email.discord())
print(email.facebook())
print(email.amazon())
print(email.twitter())
