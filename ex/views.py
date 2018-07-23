from django.shortcuts import render
import random

# Create your views here.

def appmain(request):
	num = random.randint(1,2)
	path = "silhouette/poke" + str(num) + ".png"
	
	f = open('ex/answer.txt', encoding='utf-8')
	for i in range(1,num+1):
		answer = f.readline()
		hint = f.readline()
	f.close
	
	return render(request, 'aaa.html', {
		'path' : path,
		'hint' : hint,
	})
