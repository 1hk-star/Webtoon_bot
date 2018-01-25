from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

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

    return JsonResponse({
        'message': {
            'text': "you type "+return_str+"!"
            },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : ['네이버 웹툰','다음 웹툰']
            }
        })
