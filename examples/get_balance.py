# Import the hotmailbox library
import hotmailbox

# Create a user class
user = hotmailbox.User("api_key")

# Fetch and print the user's balance in USD
print(user.balance())

# Fetch and print the user's balance in Vietnamese currency
print(user.balance(vietnamese_dong=True))
