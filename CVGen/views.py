from django.shortcuts import render

# Create your views here.


# def header(request, *args, **kwargs):
#     context = {}
#     return render(request, 'index/shared/Header.html', context)


# def footer(request, *args, **kwargs):
#     context = {}
#     return render(request, 'index/shared/Footer.html', context)


def index(request):
    context = {}
    return render(request, "index.html", context)
