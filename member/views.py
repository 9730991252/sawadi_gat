from django.shortcuts import redirect, render
from group.models import *
from django.db.models import Avg, Sum, Min, Max
import time
# Create your views here.
def member_home(request):
    if request.session.has_key('member_mobile'):
        m = request.session['member_mobile']
        member = Member.objects.filter(mobile=m).first()
        if member:
            total_member_installment = Member_installment.objects.filter(member_id=member.id).aggregate(Sum('amount'))
            
            loan_ststus = 0
            if Member_loan.objects.filter(member_id=member.id, loan_status=1).exists():
                loan_ststus = 1
            if Loan_demand.objects.filter(member_id=member.id).exists():
                loan_ststus = 1
            if 'add_demand'in request.POST:
                demand_amount = request.POST.get('demand_amount')
                if Loan_demand.objects.filter(member_id=member.id).exists():
                    pass
                else:
                    Loan_demand(
                        group_id=member.group_id,
                        member_id=member.id, 
                        demand_amount=demand_amount
                    ).save()
                time.sleep(1)
                return redirect('member_home')
            
        else:
            del request.session['member_mobile']
            return redirect('login')
        context={
            'member':member,
            'member_installment':Member_installment.objects.filter(member_id=member.id).order_by('-id'),
            'total_member_installment':total_member_installment['amount__sum'],
            'member_loan':Member_loan.objects.filter(member_id=member.id).order_by("-id"),
            'loan_ststus':loan_ststus
        }
        return render(request, 'member/member_home.html', context)
    else:
        return redirect('login')
    
def profile(request):
    if request.session.has_key('member_mobile'):
        m = request.session['member_mobile']
        member = Member.objects.filter(mobile=m).first()
        if member:
            if 'edit'in request.POST:
                pin = request.POST.get('pin')
                member.pin = pin
                member.save()
                return redirect('/member/profile/')
        else:
            del request.session['member_mobile']
            return redirect('login')
        context={
            'member':member,
        }
        return render(request, 'member/profile.html', context)
    else:
        return redirect('login')
    
def member_report(request):
    if request.session.has_key('member_mobile'):
        m = request.session['member_mobile']
        member = Member.objects.filter(mobile=m).first()
        if member:
            pass
        else:
            del request.session['member_mobile']
            return redirect('login')
        context={
            'member':member,
        }
        return render(request, 'member/member_report.html', context)
    else:
        return redirect('login')