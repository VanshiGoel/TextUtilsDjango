from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc',"off")
    fullcaps=request.POST.get('fullcaps',"off")
    removenewlines=request.POST.get('removenewlines',"off")
    removeextraspaces=request.POST.get('removeextraspaces',"off")
    countcharacters=request.POST.get('countcharacters',"off")
    punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyzed=""

    if(removepunc=="on"):
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
       
        djtext=analyzed
       
    
    if(removenewlines=="on"):
        analyzed=""
        for char in djtext:
            if(char!="\n" and char!="\r"):
              analyzed=analyzed+char
            elif char=="\n":
                analyzed=analyzed+" "
  
        djtext=analyzed
   
    
    if(removeextraspaces=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
              analyzed=analyzed+char
        
        djtext=analyzed
    
    if(countcharacters=="on"):
        analyzed=""
        length=len(djtext)
        analyzed=(f"Your text is {djtext} and The no of characters in your text is {length}")
        djtext=analyzed
     

    if(removepunc != "on" and removenewlines!="on" and removeextraspaces!="on" and fullcaps!="on" and countcharacters!="on"):
        return HttpResponse("please select any operation and try again")
    
    params={'analyzedtext':analyzed}
    return render(request,'analyze.html',params)

