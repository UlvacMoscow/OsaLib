import osa


# курс валют http://www.webservicex.net/CurrencyConvertor.asmx?WSDL http://http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL
# температура http://www.webservicex.net/ConvertTemperature.asmx?WSDL
# длина http://www.webservicex.net/length.asmx?WSDL

URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
CURRENCY = 'currencies.txt'
COUNTRIES = 'Countries.txt'


def server_currency_converter(currency, amount, way, url):
    client = osa.client.Client(url)
    response = client.service.ConvertToNum(toCurrency='RUB', fromCurrency=currency, amount=amount, rounding=True)
    print('Путь {} в российских рублях будет стоить = {}'.format(way, round(response, 0)))


def server_request(text, url):
    with open(text, encoding='utf-8') as data:
        for line in data:
            part = line.split()
            server_currency_converter(str(part[2]), float(part[1]), str(part[0]), url)


def open_text_to_list(text, url):
    with open(text, encoding='utf-8') as data:
        for line in data:
            part = line.split()
            country_to_currency(part[0], url)


def country_to_currency(part, url):
    client = osa.client.Client(url)
    response = client.service.CountryToCurrency(country=part, activeOnly=True)
    print('Страна {} код валюты {}'.format(part, response))


def seconds_since_last_change(url):
    client = osa.client.Client(url)
    response = client.service.SecondsSinceLastChange()
    print('Последнего обновления курса валют было {} секунд назад'.format(response))


seconds_since_last_change(URL)
server_request(CURRENCY, URL)
open_text_to_list(COUNTRIES, URL)





