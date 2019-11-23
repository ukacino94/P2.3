from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
	"""
	The index page, '/', renders the main_menu.html file
	which determines whether the user is signed in or not
	then either takes the user to the Main Menu or redirects
	the user to the sign in page.
	"""
	return render(request, 'main_menu.html', {

	})