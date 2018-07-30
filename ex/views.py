from django.shortcuts import render
import random

# Create your views here.

def appmain(request):
	num = random.randint(1,100)
	path1 = "silhouette/poke" + str(num) + ".png"
	path2 = "answer/poke" + str(num) + ".png"
	
	f = open('ex/static/answer.txt', encoding='utf-8')
	for i in range(1,num+1):
		answer = f.readline()
		hint = f.readline()
	f.close
	
	return render(request, 'poke.html', {
		'path1' : path1,
		'path2' : path2,
		'hint' : hint,
		'answer' : answer,
	})
