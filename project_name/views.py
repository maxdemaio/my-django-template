from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Note: for apps, you would use a subdirectory structure
def index(request):
    """ Welcome Page """
    return render(request, "index.html")
