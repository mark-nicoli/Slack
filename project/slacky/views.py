from django.shortcuts import render, redirect
import re
import requests
from slacker import Slacker
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form=UserCreationForm()
        args={'form':form}
        return render(request, 'register.html',args)

def signup(request):
    return render(request, 'signup.html')

def select(request):
    return render(request, 'select.html')

def output(request):
    #airbnb token requested
    #slack = Slacker('xoxp-599483118967-595997435696-599854938486-ba620468657b72088d155e8ec3bcfdf4') #test 1 authentication token
    #slack = Slacker('xoxp-592981392049-587776303283-612507367781-b6f49e0d4b37e04a85dad10e83cfde99') #test 2 authentication token
    slack = Slacker('xoxp-623305680485-623305681381-623306147781-7ee6587e9ddd5b660fee085e9bf81593') #test 4 auth token

    #leave channel with ID...
    #slack.channels.leave('CHMR17JMC')

    '''list members of slack workspace and get their ID from their username
        ali ID - DHKMJJYSU
        emmet ID - DHKM3EEG0
        me - UHHVBCTLG
        slack.channels.kick('CHLB8SN4C','DHKMJJYSU')
        update(8/4/2019): keep Steve in certain extpat channels'''

    # Get users list
    #response = slack.users.list()
    #users = response.body['members']

    response = slack.channels.list()
    channels = response.body['channels']           #the actual thing I said I was gonna do!
    for channel in channels:
        print(channel['id'], channel['name'])
        if "extpat" in channel['name']:
            slack.channels.leave(channel['id'])
    print()

    return render(request, 'confirmation.html')                 #render this page when the task is completed

    proxy_endpoint = 'http://myproxy:3128'
    slack = Slacker('xoxp-623305680485-623305681381-623306147781-7ee6587e9ddd5b660fee085e9bf81593',
                    http_proxy=proxy_endpoint,
                    https_proxy=proxy_endpoint)

    from requests.sessions import Session

    token = Slacker('xoxp-592981392049-587776303283-599294916432-e6bfef66c73c89f9fecbfbc931e8b25a')

    with Session() as session:
        slack = Slacker(token, session=session)
        slack.chat.post_message('#random', 'All these requests')
        slack.chat.post_message('#random', 'go through')
        slack.chat.post_message('#random', 'a single https connection')

        '''create a web page with 2 buttons: one saying i am steve and another one saying i am not steve.
        each will execute a different python file when clicked '''
