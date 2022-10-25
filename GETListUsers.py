import requests

response = requests.get('https://reqres.in/api/users', params={'page':2})
print(type(response))

# Verify response code is 200, else return appropriate message
assert response.status_code == 200, 'response status code is not 200/Success'

# Convert object into dataframe json format
df_response = response.json()
#print(df_response)

# Verify response have  total 2 pages
assert df_response['total_page'] == 2, 'list of many users not returned in response'

