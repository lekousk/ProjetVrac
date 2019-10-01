from django.shortcuts import render

# Create your views here.

def page_accueil(request):

	return render(request, 'pages/accueil.html')

