from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

def contacts(request):
    if request.method == "GET":
        return render(request, 'contacts.html')
