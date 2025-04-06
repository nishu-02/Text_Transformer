from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    incoming = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    removenewlines = request.GET.get('removenewlines', 'off')
    removespaces = request.GET.get('removespaces', 'off')
    charcount = request.GET.get('charcount', 'off')

    analyzed = ""

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in incoming:
            if char not in punctuations:
                analyzed += char
        incoming = analyzed

    if capitalize == 'on':
        analyzed = ""
        for char in incoming:
            analyzed += char.upper()
        incoming = analyzed

    if removenewlines == 'on':
        analyzed = ""
        for char in incoming:
            if char != '\n' and char != '\r':
                analyzed += char
        incoming = analyzed

    if removespaces == 'on':
        analyzed = ""
        i = 0
        while i < len(incoming):
            if not (incoming[i] == ' ' and i + 1 < len(incoming) and incoming[i + 1] == ' '):
                analyzed += incoming[i]
            i += 1
        incoming = analyzed

    result = {
        'analyzed_text': incoming
    }

    if charcount == 'on':
        result['charcount'] = f"Character Count (excluding spaces): {len(incoming.replace(' ', ''))}"

    return render(request, 'analyze.html', result)
