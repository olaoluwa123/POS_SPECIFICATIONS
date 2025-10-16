from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'web_page/index.html')

def next_page(request):
    return render(request, 'web_page/nextpage.html')