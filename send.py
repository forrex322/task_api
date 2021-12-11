import requests

headers = {}
headers[
    'Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MTgwMDk0LCJpYXQiOjE2MzkxNzk3OTQsImp0aSI6IjczZmRjZTE5NTZhZjQ2NTg4NTc1OThiZDI0NWE3MzhjIiwidXNlcl9pZCI6MX0.-cTVU6JIrYXG7h3H-uA6qEc0grq6cezwigT-M5RcN2s'

r = requests.get('http://127.0.0.1:8000/users/', headers=headers)

print(r.text)