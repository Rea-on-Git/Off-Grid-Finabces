import locale 

def format_currency(amount):

    try:
        locale.setlocale(locale.LC_ALL, '')
        return locale.currency(amount, grouping=True)
    except Exception:
        return F"$ {amount: .2f}"

