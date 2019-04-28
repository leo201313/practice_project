import requests
import json
headers = {'Authorization':'token b260286a083b2b2098c07c8cebd62deb1a2e0e2e'}
response = requests.get('https://api.github.com/users/leo201313/orgs',headers=headers)
print(response.json())
