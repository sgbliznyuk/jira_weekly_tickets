import requests
from requests.auth import HTTPBasicAuth
import json

user = 'sgbliznyuk'
password = 'sgbliznyuk'
headers = {'Content-Type' : 'application/json'}
basic_auth = HTTPBasicAuth(user, password)

print('Vvedite kol-vo dney')    
days = str(input())

all_tickets_uri = 'http://localhost:8080/rest/api/2/search?jql=project=LOGOS+AND+reporter+in+(membersOf(cko_users))+AND+created>=-'+days+'d+OR+project=LOGOS+AND+updated>=-'+days+'d+AND+reporter+in+(membersOf(cko_users))+OR+project=LOGOS+AND+resolved>=-'+days+'d+AND+reporter+in+(membersOf(cko_users))+ORDER+BY+updatedDate+DESC&fields=id,key'

r = requests.get(
    all_tickets_uri,
    headers=headers,
    auth=basic_auth
)

string = r.json()

for n in range(100):
    try:
        ticket = string['issues'][n]['key']
        print(ticket)
        uri = 'http://localhost:8080/rest/api/latest/issue/'+str(ticket)
        r = requests.get(
        uri,
        headers=headers,
        auth=basic_auth
        )
        ticket_content = r.json()
        try:
            print(ticket_content['fields']['comment']['comments'][-1]['updateAuthor']['name'])
        except IndexError:
            pass
    except IndexError:
        break
