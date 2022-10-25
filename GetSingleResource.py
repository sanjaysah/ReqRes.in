import requests

response = requests.get('https://reqres.in/api/unknown/2')
print(type(response))

# Verify response code is 404, else return appropriate message
assert response.status_code == 200, 'response status code is not 200/Success'

# Convert object into dataframe json format
exp_response = {
    "data": {
        "id": 2,
        "name": "fuchsia rose",
        "year": 2001,
        "color": "#C74375",
        "pantone_value": "17-2031"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
df_response = response.json()
print(df_response)

# Verify expected and actual response matches with correct user details
assert exp_response == df_response, 'response does not matches with expected one'

