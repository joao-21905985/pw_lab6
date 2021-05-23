from django.shortcuts import render
import datetime


# Create your views here.
def base_page_view(request):
    return render(request, 'website/base.html')


def html2_page_view(request):
    context = {
        'data': datetime.datetime.now()
    }
    return render(request, 'website/html2.html', context)


def html3_page_view(request):
    return render(request, 'website/html3.html')


def html4_page_view(request):
    return render(request, 'website/html4.html')
