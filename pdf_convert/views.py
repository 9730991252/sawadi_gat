from django.shortcuts import *
from group.models import *
from django.contrib import messages
import time
from django.views.decorators.csrf import *
from datetime import date
from django.db.models import Avg, Sum, Min, Max
from django.http import HttpResponse



def pdf_report_create(request):
    if request.session.has_key('group_mobile'):
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        if group:
            total_member_installment = Member_installment.objects.filter(group_id=group.id).aggregate(Sum('amount'))
            total_member_installment = total_member_installment['amount__sum']
            if total_member_installment is None:
                total_member_installment = 0 
            total_interest = Member_loan_installment.objects.filter(group_id=group.id).aggregate(Sum('interest_amount'))
            total_interest = total_interest['interest_amount__sum']
            if total_interest is None:
                total_interest = 0 
            if group.starting_total_interest_amount:
                total_interest += group.starting_total_interest_amount
            total_pending_loan = Member_loan.objects.filter(group_id=group.id).aggregate(Sum('loan_amount'))
            total_pending_loan = total_pending_loan['loan_amount__sum']
            if total_pending_loan is None:
                total_pending_loan = 0 
            else:
                member_loan_installment = Member_loan_installment.objects.filter(group_id=group.id).aggregate(Sum('installment_amount'))
                member_loan_installment = member_loan_installment['installment_amount__sum']
                if member_loan_installment is None:
                    member_loan_installment = 0
                else:
                    total_pending_loan -= member_loan_installment
            context={
                'group':group,
                'member':Member.objects.filter(group_id=group.id),
                'total_member_installment':total_member_installment,
                'total_interest':total_interest,
                'total_pending_loan':total_pending_loan
            }
            return render(request, 'pdf_convert/report.html', context)
        else:
            del request.session['group_mobile']
            return redirect('login')
    else:
        return redirect('login')
    
    
def member_pdf_report_create(request, id):
    if request.session.has_key('member_mobile'):
        m = request.session['member_mobile']
        member = Member.objects.filter(mobile=m).first()
        if member:
            total_member_installment = Member_installment.objects.filter(group_id=member.group.id).aggregate(Sum('amount'))
            total_member_installment = total_member_installment['amount__sum']
            if total_member_installment is None:
                total_member_installment = 0 
            total_interest = Member_loan_installment.objects.filter(group_id=member.group.id).aggregate(Sum('interest_amount'))
            total_interest = total_interest['interest_amount__sum']
            if total_interest is None:
                total_interest = 0 
            group = Group.objects.filter(id=member.group_id).first()
            if group.starting_total_interest_amount:
                total_interest += group.starting_total_interest_amount
            total_pending_loan = Member_loan.objects.filter(group_id=member.group.id).aggregate(Sum('loan_amount'))
            total_pending_loan = total_pending_loan['loan_amount__sum']
            if total_pending_loan is None:
                total_pending_loan = 0 
        else:
            del request.session['member_mobile']
            return redirect('login')
        context={
            'member':member,
            'members':Member.objects.filter(group_id=member.group.id),
            'total_member_installment':total_member_installment,
            'total_interest':total_interest,
            'total_pending_loan':total_pending_loan,
        }
        return render(request, 'pdf_convert/member_pdf_report_create.html', context)
    else:
        return redirect('login')