import requests

response = requests.get('https://reqres.in/api/users/2')
print(type(response))

# Verify response code is 200, else return appropriate message
assert response.status_code == 200, 'response status code is not 200/Success'

# Convert object into dataframe json format
exp_response = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
df_response = response.json()
#print(df_response)

# Verify expected and actual response matches with correct user details
assert exp_response == df_response, 'response does not matches with expected one'

