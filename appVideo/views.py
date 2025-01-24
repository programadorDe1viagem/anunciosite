from django.shortcuts import render

# Create your views here.
def joguinho(request):
    return render(request, 'joguinho.html')
