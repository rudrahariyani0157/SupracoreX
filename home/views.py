from django.shortcuts import render, redirect
from home.models import getyourwebsitedata
from home.models import getyourwebsitedata
from django.shortcuts import render

def home(request):
    data = getyourwebsitedata.objects.all()
    print(data)   # 👈 prints in terminal
    return render(request, 'home.html', {"data": data})

def getyourwebsite(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        budget_range = request.POST.get("budget")
        description = request.POST.get("project")

        data = getyourwebsitedata(name=name, email=email, phone=phone, budget_range=budget_range, description=description)
        data.save()
        return redirect("aftersubmit")

        # if find_data(get_gmail_id) == True:
        #     return render(request, "userexist.html")

        # else:
        #     appden_data(get_gmail_id, analysis_email, app_password, mail_type) 
        #     return render(request, 'userappended.html')

        # Print to terminal
        # print("Gmail ID:", get_gmail_id)
        # print("Analysis Email:", analysis_email)
        # print("App Password:", app_password)
        # print("Mail Type:", mail_type)
        

    return render(request, 'getyourwebsite.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')
def pricing(request):
    return render(request, 'pricing.html')
def service(request):
    return render(request, 'service.html')
def workedwith(request):
    return render(request, 'workedwith.html')
def aftersubmit(request):
    return render(request, 'aftersubmit.html')