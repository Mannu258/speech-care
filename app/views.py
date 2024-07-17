from django.shortcuts import render
from .models import Details,Email

# Create your views here.

def index(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        email = request.POST.get('email')
        Mobile = request.POST.get('mobile')
        Message = request.POST.get('msg')
        if Name and Email and Mobile and Message:
            Details.objects.get_or_create(Name=Name,Email=email,Mobile=Mobile,Message=Message)
            return render(request,'Thank-You.html')
        if email:
            Email.objects.get_or_create(Email=email)
            return render(request,"index.html")
    return render(request,"index.html")