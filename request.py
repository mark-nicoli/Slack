import re
import requests
from slacker import Slacker

#slack = Slacker('xoxp-599483118967-595997435696-599854938486-ba620468657b72088d155e8ec3bcfdf4') #test 1 authentication token
slack = Slacker('xoxp-592981392049-587776303283-599294916432-e6bfef66c73c89f9fecbfbc931e8b25a') #test 2 authentication token

#leave channel with ID...
#slack.channels.leave('CHMR17JMC')

'''list members of slack workspace and get their ID from their username
    ali ID - DHKMJJYSU
    emmet ID - DHKM3EEG0
    me - UHHVBCTLG
    slack.channels.kick('CHLB8SN4C','DHKMJJYSU')
    update(8/4/2019): keep Steve in certain extpat channels'''

# Get users list
response = slack.users.list()
users = response.body['members']
print response

response = slack.channels.list()
channels = response.body['channels']         
for channel in channels:
    print(channel['id'], channel['name'])
    if "extpat" in channel['name']:
        slack.channels.leave(channel['id'])
print()



proxy_endpoint = 'http://myproxy:3128'
slack = Slacker('xoxp-592981392049-587776303283-599294916432-e6bfef66c73c89f9fecbfbc931e8b25a',
                http_proxy=proxy_endpoint,
                https_proxy=proxy_endpoint)

from requests.sessions import Session

token = Slacker('xoxp-592981392049-587776303283-599294916432-e6bfef66c73c89f9fecbfbc931e8b25a')

with Session() as session:
    slack = Slacker(token, session=session)
    slack.chat.post_message('#random', 'All these requests')
    slack.chat.post_message('#random', 'go through')
    slack.chat.post_message('#random', 'a single https connection')
