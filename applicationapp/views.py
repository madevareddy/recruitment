from django.shortcuts import render
from .forms import ApplicationForm
from django.contrib.auth import authenticate, login, logout
from .models import ApplicationInfo
from django.contrib.auth.decorators import login_required


def applicationHome(request):
     """
	Functionality for home page 
	For getting home page
	Saving the application details using django Form
     """
     if request.method == "GET":
	 return render(request, 'application_home.html')
     else:
         form = ApplicationForm(request.POST)
	 if form.is_valid():
		form.save()
		return render(request, 'application_home.html', {"message": "Application submitted successfully"})
	 return render(request, 'application_home.html', {"message": form.errors})


def adminLogin(request):
    """
	Going to the admin login page
	Validating the username and password and getting all the applications info after login
    """
    if request.method == "GET":
        return render(request, 'adminlogin.html')
    else:
	username= request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
	    applications = ApplicationInfo.objects.all()
            return render(request, "user_applications.html", {"applications": applications})
        else:
 	    return render(request, 'adminlogin.html', {"error": "Incorrect Username o Password"})


@login_required(login_url='/login/')
def applicationDetails(request, application_id):
    """
	Getting the application details for the admin for a given application id
    """
    application_info = ApplicationInfo.objects.get(id=application_id)
    return render(request, "user_applications_info.html", {"application_info": application_info})


@login_required(login_url='/login/')
def applicationStatusUpdate(request, app_id, status):
	"""
	Updating the status of the application after approving or rejecting
	"""
	app_obj = ApplicationInfo.objects.get(id=app_id)
	app_obj.status = status
	app_obj.save()
	applications = ApplicationInfo.objects.all()
        return render(request, "user_applications.html", {"applications": applications})

