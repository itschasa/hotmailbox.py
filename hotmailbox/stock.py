import httpx
from hotmailbox.errors import *

def stock() -> dict:
    """Returns a `dict` of stock items
    
    Example Return:
    ```json
    {
        "HOTMAIL": {
            "Price": 50,
            "PriceUsd": 0.002173,
            "Stock": 142083,
            "LiveTime":"24-30 Hrs"
        },
        ...
    }
    ```
    """
    request = httpx.get(f"https://api.hotmailbox.me/mail/currentstock")
    request_json = request.json()
    
    if request_json['Code'] == 0:
        data = {}
        for entry in request_json['Data']:
            data[entry['MailCode']] = {
                "Price": int(entry['Price']),
                "PriceUsd": float(entry['PriceUsd']),
                "Stock": int(entry['Instock']),
                "LiveTime": str(entry['LiveTime'])
            }
        return data
    
    else:
        raise APIError(f"unknown error: {request_json['Code']}")
    