import requests

def fetch_crypto_data(vs_currency='usd', per_page=10, page=1):
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': vs_currency,
        'order': 'market_cap_desc',
        'per_page': per_page,
        'page': page,
        'sparkline': 'false'
    }

    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
          
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data:", response.text)
        return []
    
