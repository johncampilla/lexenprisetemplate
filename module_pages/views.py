from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'module_pages/home.html')

def client_list(request):
    return render(request, 'module_pages/client.html')

def matter_list(request):
    return render(request, 'module_pages/matters.html')

def activity_list(request):
    return render(request, 'module_pages/activity.html')

def duedate_list(request):
    return render(request, 'module_pages/duedate.html')

def AR_list(request):
    return render(request, 'module_pages/AR.html')

def document_list(request):
    return render(request, 'module_pages/document.html')

def folder_list(request):
    return render(request, 'module_pages/case_folder.html')
