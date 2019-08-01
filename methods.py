import requests

apiKey = "3dfa33b684-bf589217d6-449406490e"


# Используется для изменения типа (протокола) у списка прокси.
def setType(type='http', **ids):
    strIds = ''
    for i in ids:
        strIds = strIds + i + ","
    strIds = list(strIds)
    strIds = str(strIds[:-1])
    session = requests.session()
    r = session.get('https://proxy6.net/api/{0}/settype?ids={1}&type={2}'.format(apiKey, strIds, type))
    status = r.json()['status']
    user_id = r.json()['user_id']
    balance = r.json()['balance']
    currency = r.json()['currency']
    return status


# Используется для обновления технического комментария у списка прокси, который был установлен при покупке (метод buy).
def setDescr(comment, **ids):
    strIds = ''
    for i in ids:
        strIds = strIds + i + ","
    strIds = list(strIds)
    strIds = str(strIds[:-1])
    session = requests.session()
    r = session.get('https://proxy6.net/api/{0}/setdescr?ids={1}&new={2}'.format(apiKey, strIds, comment))
    status = r.json()['status']
    user_id = r.json()['user_id']
    balance = r.json()['balance']
    currency = r.json()['currency']
    count = r.json()['count']  # count - Кол-во прокси у которых был изменен комментарий.
    return int(count)


# Используется для покупки прокси.
def buy(count, period, country):
    session = requests.session()
    r = session.get(
        'https://proxy6.net/api/{0}/buy?count={1}&period={2}&country={3}'.format(apiKey, count, period, country))
    status = r.json()['status']
    user_id = r.json()['user_id']
    balance = r.json()['balance']
    currency = r.json()['currency']
    count = r.json()['count']
    price = r.json()['price']
    price_single = r.json()['price_single']
    period = r.json()['period']
    country = r.json()['country']
    list = r.json()['list']
    count = r.json()['count']  # count - Кол-во прокси у которых был изменен комментарий.
    return int(count)
