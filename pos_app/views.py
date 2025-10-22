from django.shortcuts import render

# Create your views here.

def next_page(request):
    return render(request, 'web_page/nextpage.html')


def intro(request):
    return render(request, 'web_page/intro.html')

def external_types(request):
    return render(request, 'web_page/external_message_types.html')

def external_message_types_layouts(request):
    return render(request, 'web_page/external_types.html')

def data_element(request):
    return render(request, 'web_page/data_element.html')

def key_management(request):
    return render(request, 'web_page/key_management.html')