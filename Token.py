import requests
my_domain = 'LucianaReguera.pythonanywhere.com'
username = 'LucianaReguera'
token = '221791643023a67f0a5b576c33be6f73ad5463a7'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
  