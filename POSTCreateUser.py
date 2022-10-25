import requests

response = requests.post('https://reqres.in/api/users',json={
    "name": "morpheus",
    "job": "leader"
},)

assert response.status_code == 201

df_response = response.json()
print((df_response))
assert df_response['name'] == "morpheus"
assert df_response['job'] == "leader"