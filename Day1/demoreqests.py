import requests
proxy_info = {'http' : '165.225.104.34:10015',
              'https' : '65.225.96.34:9480'}
r = requests.get('http://google.com', proxies=proxy_info)
print r.content