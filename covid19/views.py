from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request,"covid19/index.html")

def loginUser(request):
    return render(request,"covid19/login.html")

def symptomAnalysis(request):
    return render(request, "covid19/symptom_analaysis.html")