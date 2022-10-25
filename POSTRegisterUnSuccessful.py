import requests

response = requests.post('https://reqres.in/api/register',json={
    "email": "sydney@fife"
},)

assert response.status_code == 400, 'response status code is not 400'

exp_response = {
    "error": "Missing password"
}
df_response = response.json()
print(df_response)
assert df_response == exp_response, 'response does not matches with expected one'
