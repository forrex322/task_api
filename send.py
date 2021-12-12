import requests

headers = {}
headers[
    'Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5NDI4NTc1LCJpYXQiOjE2MzkzNDIxNzUsImp0aSI6IjhkNGYzMjA0ZmQ0NTRjYTI5ZTgyNTk4NzYzYjIyYzBkIiwidXNlcl9pZCI6MX0.2drNL0vhPh79kl5gXMZmfr2acWpNwiwLDwZecfQrm_0'

r = requests.get('http://127.0.0.1:8000/users/', headers=headers)

print(r.text)