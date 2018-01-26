from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from . import crawler
# Create your views here.

def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['네이버 웹툰','다음 웹툰']
        })

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    
    if return_str == '네이버 웹툰':
        order = 1
        title_list = ''
        titles = crawler.find_naver_toon()
        for title in titles:
            title_list += str(order) + ") " + title['title'] + "\n"
            order+=1
        return JsonResponse({
            'message': {
                'text': title_list
                 },
            'keyboard': {
                'type' : 'buttons',
                'buttons' : ['네이버 웹툰','다음 웹툰']
                }
            })
