from django.shortcuts import render

# Create your views here.

def appmain(request):
	return render(request, 'aaa.html', {})
