import requests

response = requests.post('https://reqres.in/api/register',json={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
},)

assert response.status_code == 200, 'response status code is not 200'

exp_response = {
    "id": 4,
    "token": "QpwL5tke4Pnpja7X4"
}

df_response = response.json()
print(df_response)
assert df_response == exp_response, 'response does not matches with expected one'
