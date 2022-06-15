import httpx
from hotmailbox.errors import *

class Email():
    """Represent an email account from hotmailbox.me 

    email :class:`str`
        Email returned from order
    password :class:`str`
        Password returned from order
    trans_id :class:`str`
        Transaction ID
    product :class:`str`
        Product Name
    quantity :class:`int`
        Amount of emails in the order
    unit_price :class:`int`
        Price of each email
    unit_price_usd :class:`float`
        Price of each email in USD
    total_amount :class:`int`
        Total price of order
    total_amount_usd :class:`float`
        Total price of order in USD
    """

    def __init__(self, email:str, password:str, trans_id:str=None, product:str=None, quantity:int=None, unit_price:int=None, unit_price_usd:float=None, total_amount:int=None, total_amount_usd:float=None) -> None:
        self.trans_id         = trans_id
        self.product          = product
        self.quantity         = quantity
        self.unit_price       = unit_price
        self.unit_price_usd   = unit_price_usd
        self.total_amount     = total_amount
        self.total_amount_usd = total_amount_usd
        self.email            = email
        self.password         = password
    
    
    def facebook(self, timeout=30):
        """Fetch Facebook verification code and returns as `str`
        
        timeout :class:`int`
            How long to wait for code before returning `None`
        """

        try:
            request = httpx.get(f"https://getcode.hotmailbox.me/facebook?email={self.email}&password={self.password}&timeout={timeout}", timeout=timeout+2)
            request_json = request.json()
        
        except httpx.TimeoutException:
            return None
        
        else:
            if request_json['Success'] == True:
                return request_json['VerificationCode']
            
            else:
                return None
    

    def twitter(self, timeout=30):
        """Fetch Twitter verification code and returns as `str`
        
        timeout :class:`int`
            How long to wait for code before returning `None`
        """

        try:
            request = httpx.get(f"https://getcode.hotmailbox.me/twitter?email={self.email}&password={self.password}&timeout={timeout}", timeout=timeout+2)
            request_json = request.json()
        
        except httpx.TimeoutException:
            return None
        
        else:
            if request_json['Success'] == True:
                return request_json['VerificationCode']
            
            else:
                return None
    

    def amazon(self, timeout=30):
        """Fetch Amazon verification code and returns as `str`
        
        timeout :class:`int`
            How long to wait for code before returning `None`
        """

        try:
            request = httpx.get(f"https://getcode.hotmailbox.me/twitter?email={self.email}&password={self.password}&timeout={timeout}", timeout=timeout+2)
            request_json = request.json()
        
        except httpx.TimeoutException:
            return None
        
        else:
            if request_json['Success'] == True:
                return request_json['VerificationCode']
            
            else:
                return None
    

    def discord(self, timeout=30):
        """Fetch Discord verification code and returns as `str`
        
        timeout :class:`int`
            How long to wait for code before returning `None`
        """

        try:
            request = httpx.get(f"https://getcode.hotmailbox.me/discord?email={self.email}&password={self.password}&timeout={timeout}", timeout=timeout)
            request_json = request.json()
        
        except httpx.TimeoutException:
            return None
        
        else:
            if request_json['Success'] == True:
                return request_json['VerificationCode'].replace(r"\r", "").replace(r"\n", "").replace("\n", "").replace("%0D", "")
            
            else:
                return None
        
