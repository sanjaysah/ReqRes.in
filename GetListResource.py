import requests

response = requests.get('https://reqres.in/api/unknown')
print(type(response))

# Verify response code is 404, else return appropriate message
assert response.status_code == 200, 'response status code is not 200/Success'

# Convert object into dataframe json format
exp_response = {
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "name": "cerulean",
      "year": 2000,
      "color": "#98B2D1",
      "pantone_value": "15-4020"
    },
    {
      "id": 2,
      "name": "fuchsia rose",
      "year": 2001,
      "color": "#C74375",
      "pantone_value": "17-2031"
    },
    {
      "id": 3,
      "name": "true red",
      "year": 2002,
      "color": "#BF1932",
      "pantone_value": "19-1664"
    },
    {
      "id": 4,
      "name": "aqua sky",
      "year": 2003,
      "color": "#7BC4C4",
      "pantone_value": "14-4811"
    },
    {
      "id": 5,
      "name": "tigerlily",
      "year": 2004,
      "color": "#E2583E",
      "pantone_value": "17-1456"
    },
    {
      "id": 6,
      "name": "blue turquoise",
      "year": 2005,
      "color": "#53B0AE",
      "pantone_value": "15-5217"
    }
  ],
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
df_response = response.json()
print(df_response)

# Verify expected and actual response matches with correct user details
assert exp_response == df_response, 'response does not matches with expected one'

