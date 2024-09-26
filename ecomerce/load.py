import requests
url = 'http://127.0.0.1:8000/products/'
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3Mzc5OTMyLCJpYXQiOjE3MjczNzYzMzIsImp0aSI6ImZmZTRmMTcwYmMzNTRhNjliOTYxODg3Y2I0MGZhMDA3IiwidXNlcl9pZCI6MX0.OnYAZ3Li67bxKLW_3ClywO44h1jsM1aeF6ePugmvRvw' 
}
res = requests.get(url, headers=headers)
print(res.json())