from django.shortcuts import render, redirect
from home.models import Contact
from django.shortcuts import render
from supabase import create_client
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Contact


# supabase_client.py
url = "https://drkfkidcjvuqpontqlhw.supabase.co"

# key = "sb_publishable_nTnCDAoUaIpUjrQRbt0f6A_Ylns5oYM"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRya2ZraWRjanZ1cXBvbnRxbGh3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MDIwNTA4NywiZXhwIjoyMDk1NzgxMDg3fQ.TjA-XA6ky1OYrcu0Ih7XCB0CwrQbGEtRZZHZeWpGC8Q"
supabase = create_client(url, key)

# def test_supabase(request):
#     try:
#         result = supabase.table("database").select("*").execute()

#         return JsonResponse({
#             "success": True,
#             "data": result.data
#         })

#     except Exception as e:
#         return JsonResponse({
#             "success": False,
#             "error": str(e)
#         })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def dashboard(request):
    result = supabase.table("database").select("*").execute()
    data = result.data

    return render(request, "dashboard.html", {"userdata": data})


def home(request):
    if request.method == "POST":
        result = supabase.table("database").insert({
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
            "message": request.POST.get("message")
        }).execute()

        print("SUCCESS:", result.data)

        # 🔥 IMPORTANT: redirect after POST (PREVENT CSRF + duplicate submit issues)
        return redirect("home")

    return render(request, "home.html")

# def getyourwebsite(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         print(name)
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         budget_range = request.POST.get("budget")
#         description = request.POST.get("project")

#         data = getyourwebsitedata(name=name, email=email, phone=phone, budget_range=budget_range, description=description)
#         data.save()
#         return redirect("aftersubmit")

#         # if find_data(get_gmail_id) == True:
#         #     return render(request, "userexist.html")

#         # else:
#         #     appden_data(get_gmail_id, analysis_email, app_password, mail_type) 
#         #     return render(request, 'userappended.html')

#         # Print to terminal
#         # print("Gmail ID:", get_gmail_id)
#         # print("Analysis Email:", analysis_email)
#         # print("App Password:", app_password)
#         # print("Mail Type:", mail_type)
        

#     return render(request, 'getyourwebsite.html')

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

#######################################################
#######################################################
#######################################################


def automotive(request):
    return render(request, 'examples/automotive.html')

def business(request):
    return render(request, 'examples/business.html')

def ecommerce(request):
    return render(request, 'examples/ecommerce.html')

def education(request):
    return render(request, 'examples/education.html')

def gym(request):
    return render(request, 'examples/gym.html')

def healthcare(request):
    return render(request, 'examples/healthcare.html')

def portfolio_example(request):
    return render(request, 'examples/portfolio_example.html')

def realestate(request):
    return render(request, 'examples/realestate.html')

def restaurant(request):
    return render(request, 'examples/restaurant.html')

def saas(request):
    return render(request, 'examples/saas.html')



def coffee_shop(request):
    return render(request, 'examples/coffee_shop.html')