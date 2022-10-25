import requests

response = requests.delete('https://reqres.in/api/users/2')

assert response.status_code == 204, 'response status code is not 204'

print(response.status_code)


# Verify if user is deleted, by accessing details using GET
verify_del_user = requests.get('https://reqres.in/api/users/2')
assert verify_del_user.status_code == 404, 'response status code is not 404 i.e. user is not deleted'
print(verify_del_user.status_code)
