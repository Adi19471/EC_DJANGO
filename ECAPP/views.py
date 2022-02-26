from django.shortcuts import render,redirect

from .models import ContactModel
from .forms import ContactModelForm



# Create your views here.


def home(request):
    return render(request,'E/index.html')


def aboutus(request):
    return render(request,'E/aboutus.html')


def payfor(request):
    return render(request,'E/payfor.html')


def contactus(request):

    if request.method == 'POST':
        fm = ContactModelForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            mb = fm.cleaned_data['mobile_no']
            ad = fm.cleaned_data['address']

            reg = ContactModel(name=nm, email=em, mobile_no=mb,address=ad)
            return redirect('home')
            reg.save()
            
    else:
        fm = ContactModelForm()

        
    return render(request,'E/contactus.html',{'form':fm})
    


    
