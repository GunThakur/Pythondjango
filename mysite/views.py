# # I have created this file
# # Code of video no 6
# # def index(request):
# #     s = '''<h1><a href='https://youtube.com'>Music</a></h1>
# #            <h1><a href='https://facebook.com'>Entertainment</a></h1>
# #            <h1><a href='https://instagram.com'>Entertainment2</a></h1>
# #            <h1><a href='https://poki.com'>Gaming in PC</a></h1>
# #            <h1><a href='https://typerush.com'>Typing Race</a></h1>'''
# #     return HttpResponse(s)
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removedpunc','off')
    full_caps=request.GET.get('full_caps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    character_counter=request.GET.get('character_counter','off')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # return render(request, 'analyze.html', params)
        purpose = 'Remove Punctuations, '
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if(full_caps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params= {'purpose': 'Full Caps', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params2)
    if(newlineremover=='on'):
        analyzed = ''
        for char in djtext:
            if (char !="\n" and char!='\r'):
                analyzed = analyzed + char  
        params= {'purpose': 'New line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        
        # return render(request, 'analyze.html', params3)
    if(extraspaceremover=='on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params= {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed 


# '''Character Counter'''
    if character_counter=='on':
        analyzed1=len(djtext)
        params= {'purpose': 'Characters Counted', 'analyzed_text': analyzed1}
        
    if removepunc!='on'and newlineremover!='on'and full_caps !='on'and extraspaceremover!='on':
        return HttpResponse("Please select the Operation")
    return render(request, 'analyze.html', params)
