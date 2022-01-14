from atexit import register
from mimetypes import init
from django.shortcuts import render
from django import template
import pandas as pd
import requests
import json

register = template.Library()


@register.simple_tag
def main_view(request):

    rest_api_key = "pvkyxw51gJFXcqPCn8Gjb9ZHKeVSz72Ii"
    url = "https://api.corona-19.kr/korea/?serviceKey=" + rest_api_key
    request = requests.get(url).text
    context = json.loads(request)
    context = {'df': context.to_html(justify='center')}

    return render(request, 'graph.html', context)
