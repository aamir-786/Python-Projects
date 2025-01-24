import requests

# API details
API_KEY = "bb61f514-85bb-446e-81cf-17731ea3deb4"
TOKEN_MINT_ADDRESS = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"  # Replace with your mint address
url = f"https://rpc.helius.xyz/?api-key={API_KEY}"

# Payload to fetch the largest token accounts
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getTokenLargestAccounts",
    "params": [TOKEN_MINT_ADDRESS]
}

try:
    # Make the API request
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()

        # Check for errors
        if "error" in data:
            print("API Error:", data["error"]["message"])
        else:
            holders = data["result"]["value"]
            print(f"Total Holders Fetched: {len(holders)}")
            print("Top Holders:")

            # Print details of each holder (limit to 50 if more are available)
            for idx, holder in enumerate(holders[:50], start=1):
                print(f"{idx}. Address: {holder['address']}, "
                      f"Amount: {holder['uiAmount']}, "
                      f"Decimals: {holder['decimals']}")
    else:
        print(f"API returned an error. Status Code: {response.status_code}")
        print("Error Message:", response.text)
except requests.exceptions.RequestException as e:
    print("An error occurred while making the request:", str(e))

