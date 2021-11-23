import requests
from pprint import pprint

res = requests.get('https://copyfuture.com/blogs-details/20200827201826937pyuad1fxeqmdx5h')
if res.status_code == 200:
    print('OK')
else:
    print('error')