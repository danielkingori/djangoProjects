import requests
url = 'http://127.0.0.1:8000/products/'
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2NDIxNTU5LCJpYXQiOjE3MjY0MTc5NTksImp0aSI6IjE2YTYzZTdjNTM1YzQwODU5Nzg3MTZjYjExMjI3ZWUyIiwidXNlcl9pZCI6MX0.s_35WWvcqkAado1rXNwXolrIL7k_UCEYSHaOIdh13ag' 
}
res = requests.get(url, headers=headers)
print(res.json())