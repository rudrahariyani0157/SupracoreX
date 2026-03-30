from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def getyourwebsite(request):
    if request.method == "POST":
        get_gmail_id = request.POST.get("get_gmail_id")
        analysis_email = request.POST.get("analysis_email")
        app_password = request.POST.get("app_password")
        mail_type = request.POST.get("mail_type")

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