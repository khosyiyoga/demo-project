import requests

APIToken = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjY0NjgyMjY4LCJ1aWQiOjE1MjYzMDE1LCJpYWQiOiIyMDIwLTA3LTMxVDA1OjE3OjI4LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.1A3FwTufy2jJmC_3-rkHu9-0eWofvKZwAc7UQvxNbbk'
APIURL = 'https://api.monday.com/v2'
headers = {'Authorization': APIToken}

query = ' { boards { activity_logs { account_id user_id id event } } }' #request for activity logs with accound_id, user_id, id, and event
data = {'query' : query}

jsonResult = requests.post(url=APIURL, json=data, headers=headers)
print(jsonResult.json())
