import re
import requests
from slacker import Slacker

#slack = Slacker('slack legacy token') #test 1 authentication token
slack = Slacker('slack legacy token') #test 2 authentication token

#leave channel with ID...
#slack.channels.leave('CHMR17JMC')

'''list members of slack workspace and get their ID from their username'''

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
slack = Slacker('slack legacy token',
                http_proxy=proxy_endpoint,
                https_proxy=proxy_endpoint)

from requests.sessions import Session

token = Slacker('slack legacy token')

with Session() as session:
    slack = Slacker(token, session=session)
    slack.chat.post_message('#random', 'All these requests')
    slack.chat.post_message('#random', 'go through')
    slack.chat.post_message('#random', 'a single https connection')
