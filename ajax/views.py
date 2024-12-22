from django.http import *
from django.shortcuts import *
from django.template.loader import *
from django.db.models import Q
from group.models import *
# Create your views here.
def check_backend_mobile(request):
    if request.method == 'GET':
        mobile = request.GET['mobile']
        m_id = request.GET['m_id']
        status = 0
        member_id = 0
        if mobile:
            m = Member.objects.filter(mobile=mobile).first()
            if m:
                member_id = m.id
                status = 1
            else:
                status = 0
    return JsonResponse({'status': status, 'm_id':member_id})

def member_details(request):
    if request.method == 'GET':
        id = request.GET['id']

        m = Member.objects.filter(id=id).first()
        group_name = Group.objects.filter(id=m.group.id).first()
        context1={
            'm':m,
            'group_name':group_name,
        }
        t = render_to_string('ajax/office/member_details.html', context1)
    return JsonResponse({'t': t})
 
def member_details_loan(request):
    if request.method == 'GET':
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        c = ''
        id = request.GET['id']
        m = Member.objects.filter(id=id).first()
        context={
            'm':m,
            'group':group,
        }
        t = render_to_string('ajax/office/member_details_loan.html', context)
    return JsonResponse({'t': t})

def member_details_bank_loan(request):
    if request.method == 'GET':
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        c = ''
        id = request.GET['id']
        m = Member.objects.filter(id=id).first()
        print('t')
        context={
            'm':m,
            'group':group,
        }
        t = render_to_string('ajax/office/member_details_bank_loan.html', context)
    return JsonResponse({'t': t})

def member_sangh_loan_details(request):
    if request.method == 'GET':
        m = request.session['group_mobile']
        group = Group.objects.filter(mobile=m).first()
        c = ''
        id = request.GET['id']
        m = Member.objects.filter(id=id).first()
        print('t')
        context={
            'm':m,
            'group':group,
        }
        t = render_to_string('ajax/office/member_sangh_loan_details.html', context)
    return JsonResponse({'t': t})




















