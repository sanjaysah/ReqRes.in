import requests

response = requests.get('https://reqres.in/api/users/2a3')
print(type(response))

# Verify response code is 404, else return appropriate message
assert response.status_code == 404, 'response status code is not 404/Not Found'

# Convert object into dataframe json format
df_response = response.json()
print(df_response)

