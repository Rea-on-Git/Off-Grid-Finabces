import locale 
print("Currency Formatter has run succesfully ")

def get_users_currency():

    try:
        locale.setlocale(locale.LC_ALL, '')
        symbol = locale.localeconv() ['currency_symbol']
        return symbol  if symbol else '$'
    except Exception:
        return '$ Read '
    
def format_currency(amount):

    try:
        locale.setlocale(locale.LC_ALL, '')
        return locale.currency(amount, grouping=True)
    except Exception:
        return F"$ {amount: .2f}"

