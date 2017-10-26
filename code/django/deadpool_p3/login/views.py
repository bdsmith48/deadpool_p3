from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(request):
    # return HttpResponse("<h2>Ole!</h2>")
    return render(request, 'login/test.html')