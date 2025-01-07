from django.shortcuts import *
from .models import *
from django.contrib import messages
import time
from django.views.decorators.csrf import *
from datetime import date
from django.db.models import Avg, Sum, Min, Max

# Create your views here.

@csrf_exempt
def group_loan(request):
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
                return redirect('group_loan')
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'members':Member.objects.filter(group_id=group.id,status=1)
        }
        return render(request, 'group/group_loan.html', context)
    else:
        return redirect('login')
    
@csrf_exempt
def bank_loan(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            if 'add_loan_member'in request.POST:
                member_id = request.POST.get('member_id')
                loan_amount = request.POST.get('loan_amount')
                minimum_loan_installment = request.POST.get('minimum_loan_installment')
                if Member_bank_loan.objects.filter(member_id=member_id,loan_status=1).exists():
                    pass
                else:
                    Member_bank_loan(
                        member_id = member_id,
                        group_id=group.id,
                        loan_amount = loan_amount,
                        minimum_loan_installment = minimum_loan_installment,
                    ).save()
                time.sleep(1)        
                return redirect('bank_loan')        
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'members':Member.objects.filter(group_id=group.id, status=1)
        }
        return render(request, 'group/bank_loan.html', context)
    else:
        return redirect('login')

@csrf_exempt
def sangh_loan(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            if 'add_loan_member'in request.POST:
                member_id = request.POST.get('member_id')
                loan_amount = request.POST.get('loan_amount')
                minimum_loan_installment = request.POST.get('minimum_loan_installment')
                if Member_sangh_loan.objects.filter(member_id=member_id,loan_status=1).exists():
                    pass
                else:
                    Member_sangh_loan(
                        member_id = member_id,
                        group_id=group.id,
                        loan_amount = loan_amount,
                        minimum_loan_installment = minimum_loan_installment,
                    ).save()
                time.sleep(1)        
                return redirect('sangh_loan')        
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'members':Member.objects.filter(group_id=group.id,status=1)
        }
        return render(request, 'group/sangh_loan.html', context)
    else:
        return redirect('login')






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
            'member':Member.objects.filter(group_id=group.id)
        }
        return render(request, 'group/group_home.html', context)
    else:
        return redirect('login')
    
def report(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            total_member_installment = Member_installment.objects.filter().aggregate(Sum('amount'))
            total_member_installment = total_member_installment['amount__sum']
            if total_member_installment is None:
                total_member_installment = 0 
            total_interest = Member_loan_installment.objects.filter().aggregate(Sum('interest_amount'))
            total_interest = total_interest['interest_amount__sum']
            if total_interest is None:
                total_interest = 0 
            total_pending_loan = Member_loan.objects.filter().aggregate(Sum('loan_amount'))
            total_pending_loan = total_pending_loan['loan_amount__sum']
            if total_pending_loan is None:
                total_pending_loan = 0 
            else:
                member_loan_installment = Member_loan_installment.objects.filter().aggregate(Sum('installment_amount'))
                member_loan_installment = member_loan_installment['installment_amount__sum']
                if member_loan_installment is None:
                    member_loan_installment = 0
                else:
                    total_pending_loan -= member_loan_installment
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'member':Member.objects.filter(group_id=group.id),
            'total_member_installment':total_member_installment,
            'total_interest':total_interest,
            'total_pending_loan':total_pending_loan
        }
        return render(request, 'group/report.html', context)
    else:
        return redirect('login')
    
    
@csrf_exempt
def edit_collection(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            if 'check_pin'in request.POST:
                member_id = request.POST.get('member_id')
                pin = request.POST.get('pin')
                if int(group.pin) == int(pin):
                    return redirect(f'/group/edit_member_collection/{member_id}')
                else:
                    return redirect('edit_collection')
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'member':Member.objects.filter(group_id=group.id, status=1)
        }
        return render(request, 'group/edit_collection.html', context)
    else:
        return redirect('login')
    
@csrf_exempt
def loan(request):
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
            'members':Member.objects.filter(group_id=group.id, status=1)
        }
        return render(request, 'group/loan.html', context)
    else:
        return redirect('login')
    
@csrf_exempt
def edit_member_collection(request, member_id):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            member = Member.objects.filter(id=member_id, group_id=group.id).first()
            if member:
                m = date.today().month
                if m < 10:
                    m = f'0{date.today().month}'
                d = f'{date.today().year}-{m}'
                group_loan_installment = ''
                member_loan = Member_loan.objects.filter(member_id=member_id, loan_status=1).last()
                if member_loan:
                    g = Member_loan_installment.objects.filter(date__icontains=d,member_id=member_id, loan_id=member_loan.id).last()
                    if g == None:
                        group_loan_installment = 0
                    else:
                        group_loan_installment = g.installment_amount
                    
                if 'save_member_installment'in request.POST:
                    loan_installment = request.POST.get('loan_installment')
                    Member_loan_installment.objects.filter(member_id=member_id, loan_id=member_loan.id).update(installment_amount=loan_installment)
                    
                    amount = member_loan.loan_amount
                    g = Member_loan_installment.objects.filter(member_id=member_id, loan_id=member_loan.id).aggregate(Sum('installment_amount'))
                    installment_amount = g['installment_amount__sum']
                    if installment_amount:
                        amount -= installment_amount
                    if amount == 0:
                        member_loan.loan_status = 0
                        member_loan.save()
                    
                    
                    return redirect('edit_member_collection', member_id=member_id)
                
                context = {
                    'group': group,
                    'member': member,
                    'group_loan_installment':group_loan_installment,
                    'member_loan':member_loan
                }
                return render(request, 'group/edit_member_collection.html', context)
            else:
                messages.error(request, "Member not found")
                return redirect('collection')
        else:
            del request.session['group_mobile']
            return redirect('login')
    else:
        return redirect('login')
    
@csrf_exempt
def collection(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            d = f'{date.today().year}-{date.today().month}'
            if 'check_pin'in request.POST:
                member_id = request.POST.get('member_id')
                pin = request.POST.get('pin')
                if int(group.pin) == int(pin):
                    return redirect(f'/group/edit_member_collection/{member_id}')
                else:
                    return redirect('collection')
                
            if 'add_amount'in request.POST:
                member_id = request.POST.get('member_id')
                amount = request.POST.get('amount')
                loan_installment = request.POST.get('loan_installment') # gat
                loan_interest = request.POST.get('loan_interest') # gat
                loan_amount = request.POST.get('loan_amount') # gat
                
                bank_loan_installment = request.POST.get('loan_installment') # bank
                bank_loan_interest = request.POST.get('bank_loan_interest') # bank
                bank_loan_amount = request.POST.get('bank_loan_amount') # bank
                
                sangh_loan_installment = request.POST.get('loan_installment') # sangh
                sangh_loan_interest = request.POST.get('sangh_loan_interest') # sangh
                sangh_loan_amount = request.POST.get('sangh_loan_amount') # sangh
                
                if Member_installment.objects.filter(date__icontains=d, member_id=member_id).exists():
                    messages.warning(request,f"Member already Added")  
                else:
                    Member_installment(
                        member_id=member_id,
                        group_id=group.id, 
                        amount=loan_installment,
                    ).save()
                    if Member_loan.objects.filter(member_id=member_id,loan_status=1).exists():
                        l = Member_loan.objects.filter(member_id=member_id, loan_status=1).last()
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
                            
                    if Member_bank_loan.objects.filter(member_id=member_id,loan_status=1).exists():
                        l = Member_bank_loan.objects.filter(member_id=member_id, loan_status=1).last()
                        
                        Member_bank_loan_installment(
                            loan_id=l.id,
                            member_id=member_id,
                            group_id=group.id,
                            interest_amount=bank_loan_interest,
                            installment_amount=bank_loan_amount,
                        ).save()
                        g = Member_bank_loan_installment.objects.filter(member_id=member_id, loan_id=l.id).aggregate(Sum('installment_amount'))
                        installment_amount = g['installment_amount__sum']
                        total_pending_amount = (int(l.loan_amount) - int(installment_amount) )
                        if total_pending_amount == 0:
                            l.loan_status = 0
                            l.save()
                            
                    if Member_sangh_loan.objects.filter(member_id=member_id,loan_status=1).exists():
                        l = Member_sangh_loan.objects.filter(member_id=member_id, loan_status=1).last()
                        Member_sangh_loan_installment(
                            loan_id=l.id,
                            member_id=member_id,
                            group_id=group.id,
                            interest_amount=sangh_loan_interest,
                            installment_amount=sangh_loan_amount,
                        ).save()
                        g = Member_sangh_loan_installment.objects.filter(member_id=member_id, loan_id=l.id).aggregate(Sum('installment_amount'))
                        installment_amount = g['installment_amount__sum']
                        total_pending_amount = (int(l.loan_amount) - int(installment_amount) )
                        if total_pending_amount == 0:
                            l.loan_status = 0
                            l.save()
                time.sleep(1)
                return redirect('collection')
            #//?//?//?//?//?//?//?//?//?//?//?//?//?//?//?//?//?//?//?
        else:
            del request.session['group_mobile']
            return redirect('login')
        context={
            'group':group,
            'members':Member.objects.filter(group_id=group.id,status=1)
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
                loan_bank_interest = request.POST.get('loan_bank_interest')
                loan_sangh_interest = request.POST.get('loan_sangh_interest')
                pin = request.POST.get('pin')
                group = Group.objects.filter(id=id).first()
                group.group_name = name
                group.pin = pin
                group.address = address
                group.member_installment_limit = member_installment_limit
                group.maximum_loan = maximum_loan
                group.loan_interest = loan_interest
                group.loan_bank_interest=loan_bank_interest
                group.loan_sangh_interest=loan_sangh_interest
                group.save()
                    
        else:
            del request.session['office_mobile']
            return redirect('login')
        context={
            'group':group,
        }
        return render(request, 'group/profile.html', context)
    else:
        return redirect('login')