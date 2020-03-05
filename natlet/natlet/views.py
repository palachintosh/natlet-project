from django.shortcuts import redirect

def based_page(request):
    return redirect('index_page_url', permanent=True)