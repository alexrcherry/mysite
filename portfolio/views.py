from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def IndexView(request):
    context = {}
    template = "portfolio/index.html"

    return render(
        request,
        template,
        context,
    )

def main(request):
    context = {}
    template = "portfolio/main.html"

    return render(
        request,
        template,
        context,
    )
