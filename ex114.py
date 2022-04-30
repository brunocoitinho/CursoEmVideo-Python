import requests

def pudim_online():
    url = 'http://pudim.com.br/'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except:
        return False


if pudim_online():
    print(f'\033[33mConsegui acessar o site Pudim!\033[m')
else:
    print(f'\033[31mO site Pudim não está acessível no momento!\033[m')