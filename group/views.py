from django.shortcuts import *
from .models import *
from django.contrib import messages
import time
from django.views.decorators.csrf import *
from datetime import date
from django.db.models import Avg, Sum, Min, Max
# Create your views here.
def group_home(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            pass
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'member':Member.objects.all()
        }
        return render(request, 'group/group_home.html', context)
    else:
        return redirect('login')
    
@csrf_exempt
def loan(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            if 'add_loan_member'in request.POST:
                member_id = request.POST.get('member_id')
                loan_amount = request.POST.get('loan_amount')
                minimum_loan_installment = request.POST.get('minimum_loan_installment')
                if Member_loan.objects.filter(member_id=member_id,loan_status=1).exists():
                    pass
                else:
                    Member_loan(
                        member_id = member_id,
                        group_id=group.id,
                        loan_amount = loan_amount,
                        minimum_loan_installment = minimum_loan_installment,
                    ).save()
                    loan_demand = Loan_demand.objects.filter(member_id=member_id).first()
                    if loan_demand:
                        loan_demand.delete()
                time.sleep(1)        
                return redirect('loan')
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'members':Member.objects.filter(status=1)
        }
        return render(request, 'group/loan.html', context)
    else:
        return redirect('login')
    
@csrf_exempt
def collection(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            d = f'{date.today().year}-{date.today().month}'
            if 'add_amount'in request.POST:
                member_id = request.POST.get('member_id')
                amount = request.POST.get('amount')
                loan_installment = request.POST.get('loan_installment')
                loan_interest = request.POST.get('loan_interest')
                loan_amount = request.POST.get('loan_amount')
                if Member_installment.objects.filter(date__icontains=d, member_id=member_id).exists():
                    messages.warning(request,f"Member already Added")   
                else:
                    if Member_loan.objects.filter(member_id=member_id,loan_status=0).exists():
                        l = Member_loan.objects.filter(member_id=member_id, loan_status=1).last()
                        Member_installment(
                            member_id=member_id,
                            group_id=group.id,
                            amount=loan_installment,
                        ).save()
                        Member_loan_installment(
                            loan_id=l.id,
                            member_id=member_id,
                            group_id=group.id,
                            interest_amount=loan_interest,
                            installment_amount=loan_amount,
                        ).save()
                        g = Member_loan_installment.objects.filter(member_id=member_id, loan_id=l.id).aggregate(Sum('installment_amount'))
                        installment_amount = g['installment_amount__sum']
                        total_pending_amount = (int(l.loan_amount) - int(installment_amount) )
                        if total_pending_amount == 0:
                            l.loan_status = 0
                            l.save()
                    else:
                        Member_installment(
                            member_id=member_id,
                            group_id=group.id,
                            amount=amount,
                        ).save()
                time.sleep(1)
                return redirect('collection')
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'members':Member.objects.filter(status=1)
        }
        return render(request, 'group/collection.html', context)
    else:
        return redirect('login')
    
def members(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            if 'add_member'in request.POST:
                name = request.POST.get('name')
                address = request.POST.get('address')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                if Member.objects.filter(mobile=mobile).exists():
                    messages.warning(request,f"Member already Exists - {mobile}")   
                else:
                    Member(
                        group_id=group.id,
                        name = name,
                        address = address,
                        mobile = mobile,
                        pin = pin,
                    ).save()
                    messages.success(request,f"Member Added successfully - {name} - {mobile}")   
                time.sleep(1)
                return redirect('members')
            if 'edit_member'in request.POST:
                id = request.POST.get('id')
                name = request.POST.get('name')
                address = request.POST.get('address')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                Member(
                    id = id,
                    group_id=group.id,
                    name = name,
                    address = address,
                    mobile = mobile,
                    pin = pin,
                ).save()
                messages.success(request,f"Member Edited successfully - {name} - {mobile}")   
                return redirect('members')
            if 'active'in request.POST:
                id = request.POST.get('id')
                c = Member.objects.filter(group_id=group.id, id=id).first()
                c.status = 0
                c.save()
                return redirect('members')
            if 'deactive'in request.POST:
                id = request.POST.get('id')
                c = Member.objects.filter(group_id=group.id, id=id).first()
                c.status = 1
                c.save()
                return redirect('members')
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'members':Member.objects.filter(group_id=group.id).order_by('name')
        }
        return render(request, 'group/members.html', context)
    else:
        return redirect('login')
    

def profile(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            if request.method == "POST":
                id = request.POST.get('id')
                name = request.POST.get('name')
                address = request.POST.get('address')
                member_installment_limit = request.POST.get('member_installment_limit')
                maximum_loan = request.POST.get('maximum_loan')
                loan_interest = request.POST.get('loan_interest')
                pin = request.POST.get('pin')
                group = Group.objects.filter(id=id).first()
                group.group_name = name
                group.pin = pin
                group.address = address
                group.member_installment_limit = member_installment_limit
                group.maximum_loan = maximum_loan
                group.loan_interest = loan_interest
                group.save()
                    
        else:
            del request.session['office_mobile']
            return redirect('login')
        context={
            'group':group,
            'group':Group.objects.all().last()
        }
        return render(request, 'group/profile.html', context)
    else:
        return redirect('login')