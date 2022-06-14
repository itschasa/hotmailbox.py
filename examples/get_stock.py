# Import the hotmailbox library
import hotmailbox

# Fetch the stock for hotmailbox
stock = hotmailbox.stock()

# Print the price and stock amount for Hotmail emails
print(stock['HOTMAIL']['Price'])
print(stock['HOTMAIL']['Stock'])
