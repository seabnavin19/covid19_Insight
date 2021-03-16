from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def HomePage(request):
    return render(request,"covid19/index.html")

@login_required(login_url='login')
def symptomAnalysis(request):
    return render(request, "covid19/symptom_analaysis.html")

def loginUser(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'covid19/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')