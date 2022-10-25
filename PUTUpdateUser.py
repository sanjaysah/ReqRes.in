import requests

response = requests.put('https://reqres.in/api/users/2',json={
    "name": "morpheus",
    "job": "zion resident"
},)

assert response.status_code == 200, 'response status code is not 200'

df_response = response.json()
print(df_response)
assert df_response['name'] == "morpheus"
assert df_response['job'] == "zion resident"
