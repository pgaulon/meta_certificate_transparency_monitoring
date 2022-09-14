import requests
import os

# https://developers.facebook.com/docs/facebook-login/guides/access-tokens#apptokens
app_id = os.environ.get('APP_ID')
app_secret = os.environ.get('APP_SECRET')

# here we only want the list of Certificate Authorities
ca = []
response = requests.get('https://graph.facebook.com/certificates', params={'query': 'facebook.com', 'fields': 'issuer_name', 'access_token': '{}|{}'.format(app_id, app_secret)}).json()
while(True):
    try:
        for data in response['data']:
            issuer = data['issuer_name'].split('/')[-1]
            if issuer not in ca:
                ca.append(issuer)
        response = requests.get(response['paging']['next']).json()
    except KeyError:
        break
print(ca)
