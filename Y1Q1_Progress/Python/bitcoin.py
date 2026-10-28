import sys
import requests
bitcoin_api = requests.get(
    "https://rest.coincap.io/v3/assets/bitcoin?apiKey=9559e04a9144371efe44c55a57ca03daac2cbfbd5fedb641b899b3a43a4f09a3"
    )
bitjson = bitcoin_api.json()
try:
    if len(sys.argv) == 1:
        print("Missing command-line argument")
    elif len(sys.argv) == 2 and str(int(float(sys.argv[1]))).isdigit():
        bitcoin_amount = float(sys.argv[1])
        print(f"${bitcoin_amount * float(bitjson["data"]["priceUsd"]):,.4f}")


except Exception:
    sys.exit("Command-line argument is not a number")
