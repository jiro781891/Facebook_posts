from django.shortcuts import render
import requests
import inspect
import os
import json
import urllib.request
from django.http import HttpResponseForbidden, HttpResponse

# Create your views here.
token = 'EAACEdEose0cBAOc9ZCOiVOwohj3P0hKGRbe8RLE1ZCoI0xBolPbGmgKadYIoBZChKEayurptbtGVMOTzVDf6nwNaYEO9wxynQ6nXs7YktZC7mTA9ubWmnUZA6aQsyq23OOFtxqKe4DfXAFeJrVMiHCGviZC4FzTmWugElMlmXa4IogDR06ObDhRsNppW6lUzR9FVR9HetB7UTXcjX2lz6dY7Hiy1z3OlEZD'


def fetch_post(request):
    user_name_link = "https://graph.facebook.com/v2.12/me?fields=name&access_token=" + token #Url for fetching user's name and id
    user_name_get = requests.get(user_name_link) #Get's user's name and id as json
    user_name_data = json.loads(user_name_get.text) #Reads json text
    try:
        user_name = user_name_data['name']
    except KeyError:
        return HttpResponse("Please update Accses Token")

    outputlist = []

    link = 'https://graph.facebook.com/v2.9/me/feed?access_token=' + token #Url for fetching user's feed
    info = requests.get(link) # Get's user's feed as json
    data1 = json.loads(info.text) # Reads json
    try:
        posts = data1['data']
    except KeyError:
        return HttpResponse("Please update Accses Token")
    for i in range(len(posts)): #Generates a list which contains users posts separately
        for g in data1['data'][i]:
            if g == "message" or g == "story":
                outputlist.append(data1['data'][i][g])


    if 'button-pressed' in request.POST: #If user press "POST" button this code takes data from comment box and post to facebook
        user_input = request.POST.get("postext")
        link_for_post = 'https://graph.facebook.com/v2.9/me/feed?message=' + user_input + '&access_token=' + token
        post1 = requests.post(link_for_post)
        data2 = json.loads(post1.text) #post messege


    if  request.method == "GET": #If user change value of selection menu this code reverse the outputlist
        if request.GET.get('dropdown') and 'reversed' in request.GET.get('dropdown'):
            outputlist = reversed(outputlist)

    return render(request, "base.html", {'outputlist': outputlist, 'user_name': user_name}  ) # output data to website
