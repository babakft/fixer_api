URL = "https://api.apilayer.com/fixer/latest?base=USD"

API_KEY = "ODcn4W0uYqyyRVoY2xYCVmR5thzggjF2"

RULES = {
    "save": False,
    "email": {
        "enable": False,
        "receiver": 'babakft082@gmail.com',
        "preferred": ['BTC', 'IRR']
    },
    "notification": {
        "enable": False,
        "receiver": '09337715290',
        "preferred": {
             'BTC': {'min': 0.000101, 'max': 0.000110},
             'IRR': {'min': 30000, 'max': 50000}
         }

    }
}
