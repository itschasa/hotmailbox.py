import httpx, time, typing
from hotmailbox.email import *
from hotmailbox.errors import *
from hotmailbox.translate import __translations__

class User:
    """Represent a user

    api_key: :class:`str`
        API Key obtained from hotmailbox.me
    retries :class:`int`
        If rate limited, amount of retries that will be attempted
    """
    
    def __init__(self, api_key:str, retries:int=5) -> None:
        self.api_key = api_key
        self.retries = retries
        if self.retries == 0: self.retries = 1
        
        # check if api key is valid
        self.balance()
    

    def balance(self, vietnamese_dong:bool=False) -> float:
        """Returns balance of the account
    
        vietnamese_dong :class:`bool`
            If `True`, returns vietnamese currency instead of USD
        """
        
        for x in range(self.retries):
            request = httpx.get(f"https://api.hotmailbox.me/user/balance?apikey={self.api_key}")
            request_json = request.json()
            
            if request_json['Code'] == 0:
                if vietnamese_dong:
                    return float(request_json['Balance'])
                else:
                    return float(request_json['BalanceUsd'])
            
            elif request_json['Code'] == 401:
                raise InvalidAPIKey("api key provided is invalid")
            
            elif __translations__["Rate Limited"] == request_json['Message']:
                if x != self.retries - 1: time.sleep(1)
            
            else:
                raise APIError(f"unknown error: {request_json['Code']}")
        
        raise MaxRateLimit("max retries reached")
    
    
    def purchase(self, type:str, amount:int=1) -> typing.List[Email]:
        """Makes a purchase from the account and returns a list of `Email` classes 
    
        type :class:`str`
            The type of email you want to purchase
        amount :class:`int`
            The amount you want to purchase
        """
        
        for x in range(self.retries):
            request = httpx.get(f"https://api.hotmailbox.me/mail/buy?apikey={self.api_key}&mailcode={type}&quantity={amount}")
            request_json = request.json()
            
            if request_json['Code'] == 0:
                data = []
                for email in request_json['Data']['Emails']:
                    data.append(
                        Email(
                            email['Email'],
                            email['Password'],
                            request_json['Data']['TransId'],
                            request_json['Data']['Product'],
                            request_json['Data']['Quantity'],
                            request_json['Data']['UnitPrice'],
                            request_json['Data']['UnitPriceUsd'],
                            request_json['Data']['TotalAmount'],
                            request_json['Data']['TotalAmountUsd']
                        )
                    )
                return data
            
            elif request_json['Code'] == 401:
                raise InvalidAPIKey("api key provided is invalid")
            
            elif __translations__["Rate Limited"] == request_json['Message']:
                if x != self.retries - 1: time.sleep(1)
            
            elif __translations__["Insufficient Balance"] == request_json['Message']:
                raise InsufficientBalance("not enough balance to make purchase")
            
            else:
                raise APIError(f"unknown error: {request_json['Code']}")
        
        raise MaxRateLimit("max retries reached")
    

    