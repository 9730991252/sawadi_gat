from django.contrib import messages
from django.shortcuts import redirect, render
from group.models import *
import time
# Create your views here.
def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["number"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 11000 :
            request.session['sunil_mobile'] = s
            return redirect('sunil_home')
        else:
            return redirect('sunil_login')
    return render(request, 'home/login.html')



def sunil_home(request):
    if request.session.has_key('sunil_mobile'):
        if 'add_group'in request.POST:
            group_name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            address = request.POST.get('address')
            member_installment_limit = request.POST.get('member_installment_limit')
            maximum_loan = request.POST.get('maximum_loan')
            loan_interest = request.POST.get('loan_interest')
            if Group.objects.filter(mobile=mobile).exists():
                pass
            else:
                Group(
                    group_name = group_name,
                    mobile = mobile,
                    pin = pin,
                    address = address,
                    member_installment_limit = member_installment_limit,
                    maximum_loan = maximum_loan,
                    loan_interest = loan_interest,
                ).save()
            time.sleep(1)
            return redirect('sunil_home')

        context={
            'group':Group.objects.all()
        }
        return render(request, 'sunil/sunil_home.html', context)
    else:
        return redirect('sunil')

