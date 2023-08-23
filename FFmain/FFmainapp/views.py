from django.shortcuts import render


def home(request):
	return render(request, 'FFmainapp/Main_Logic/start_page.html')
