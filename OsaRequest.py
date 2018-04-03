import osa


# курс валют http://www.webservicex.net/CurrencyConvertor.asmx?WSDL http://http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL
# температура http://www.webservicex.net/ConvertTemperature.asmx?WSDL
# длина http://www.webservicex.net/length.asmx?WSDL


URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
CURRENCY = 'currencies.txt'


def server_currency_converter(currency, amount, way, url):
    client = osa.client.Client(url)
    response = client.service.ConvertToNum(toCurrency='RUB', fromCurrency=currency, amount=amount, rounding=True)
    print('Путь {} в российских рублях будет стоить = {}'.format(way, round(response, 0)))


def server_request(text, url):
    with open(text, encoding='utf-8') as data:
        for line in data:
            part = line.split()
            server_currency_converter(str(part[2]), float(part[1]), str(part[0]), url)


server_request(CURRENCY, URL)

# licenseKey=string&
# fromCurrency=RUB
# toCurrency=USD
# amount=100
# rounding=True
# format=string&
# date=string&
# type=string HTTP/1.1
#
#
# FromUnit = 'degreeFahrenheit'
# ToUnit = 'degreeCelsius'
# Temperature = '67'

# def convert(a,b,c):
#     return client.services(Temperature = a, FromUnit = b, ToUnit = c )


# def convert(a,b,c):
#     params = {
#         'Temperature' : a,
#         'FromUnit' : b,
#         'ToUnit' : c
#     }
#     return client.services(params)

# print(convert(Temperature, FromUnit, ToUnit))



# current_dir = os.path.dirname(os.path.abspath(__file__))
# temps_dir = os.path.join(current_dir,'temps.txt')
# currencies_dir = os.path.join(current_dir, 'currencies.txt')
# travel_dir = os.path.join(current_dir, 'travel.txt')


# def read_text(text):
#     with open(text, encoding='UTF-8') as f:
#         data = f.read()
#         text_for_osa = data.split()
#         client._services.Temperature(text_for_osa[0])
#         print(text_for_osa[0], 'lasdlsd', text_for_osa[1])
#
#
# print(temps_dir, read_text(temps_dir) )
# print(currencies_dir, read_text(currencies_dir))
# print(travel_dir, read_text(travel_dir))

