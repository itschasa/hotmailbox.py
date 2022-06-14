<div align="center">
    <h1>hotmailbox.py</h1>
    <p>📧 Use hotmailbox.me quickly and efficiently</p>
    <img src="https://img.shields.io/github/license/ItsChasa/hotmailbox.py?style=flat">
    <img src="https://img.shields.io/github/downloads/ItsChasa/hotmailbox.py/total?style=flat">
    <img src="https://img.shields.io/github/stars/ItsChasa/hotmailbox.py?style=flat">
    <img src="https://img.shields.io/github/forks/ItsChasa/hotmailbox.py?style=flat">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=itschasa_hotmailbox.py&metric=ncloc"/>
    <br>
    <p><i>⭐ star the repo pls <3</i></p>
</div>


## Support + Community
[Discord Server](https://chasa.wtf/discord) | [Telegram Chat](https://chasa.wtf/telegram) | [Website](https://chasa.wtf/)


## Features:
- Purchase Emails in Different Quantities
- Fetch Verification Codes/Links
- Check Balance and Stock


## Installation
Using PyPi:
```
python3 -m pip install hotmailbox.py
```

Using GitHub Source
```
python3 -m pip install git+https://github.com/itschasa/hotmailbox.py
```


## Example
```python
# Import the hotmailbox library
import hotmailbox

# Fetch the stock for hotmailbox
stock = hotmailbox.stock()

# Print the price and stock amount for Hotmail emails
print(stock['HOTMAIL']['Price'])
print(stock['HOTMAIL']['Stock'])

# Create a user class
user = hotmailbox.User("api_key")

# Purchase a Hotmail email
emails = user.purchase("HOTMAIL", 1)

# Get the first entry from the list of emails,
# and print the "email" and "password" of it
print(emails[0].email)
print(emails[0].password)

# Fetch and print verification link from Discord
print(emails[0].discord())
```
