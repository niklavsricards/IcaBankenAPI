# IcaBankenAPI

Python code to get transactions from Ica Banken Api Sandbox environment. 

## Setup

1. Make sure you have newest Python version installed using `python --version` in cmd.
2. Install pip using `py -m ensurepip --upgrade`
3. Install requests using `python -m pip install requests`
4. Sign-in or create an account in IcaBanken developer [portal](https://apim-icabanken.ica.se/store).
5. Go to Applications and create a new application called 'psd2_sandbox'.
6. Go to Subscriptions and subscribe to 'Accounts Sandbox' API.
7. Go to your psd2_sandbox application and in Sandbox Keys tab generate your Client Id and Client secret.
8. Provide Client Id and Client Secret in `main.py` file as shown there.
9. In `Functional description Sandbox.pdf` in section GET /Accounts/{accountId}/transactions choose a SSN, status and AccountID
and provide them also in `main.py`.
10. Open cmd, go to the directory of your project and run `main.py`. 
The result, either an error and details or list of transactions will be written in `data.json` file.

## Result

As only one endpoint is defined (for getting transactions) you will get and error and details or transactions for the specific acccount written in .json file.
