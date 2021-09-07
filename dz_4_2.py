from requests import get, utils


def currency_rates():
    print('Input currency code: ')
    currency_code = input()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency_code = currency_code.upper()

    if currency_code not in content:
        print('None')
    else:
        # print(content)
        currency = content.split(currency_code)[1]
        currency_2 = currency.split('</Value>')[0]
        currency_3 = currency_2.split('<Value>')[1]
        currency_4 = currency_3.split(',')
        currency_5 = '.'.join(currency_4)
        currency_5 = float(currency_5)
        print(currency_5)
        print(type(currency_5))


currency_rates()
