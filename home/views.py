from django.shortcuts import redirect, render
from django.contrib import * 
from group.models import *
from datetime import date
# Create your views here.
def index(request):
    Member_installment.objects.filter(member_id=4).delete()
    return render(request, 'home/index.html')


def login(request):
    if request.session.has_key('group_mobile'):
        return redirect('group_home')
    if request.session.has_key('member_mobile'):
        return redirect('member_home')
    else:
        if request.method == "POST":
            number=request.POST ['number']
            pin=request.POST ['pin']
            o = Group.objects.filter(status=1, mobile=number, pin=pin).first()
            if o:
                request.session['group_mobile'] = request.POST["number"]
                return redirect('group_home')
            m = Member.objects.filter(status=1, mobile=number, pin=pin).first()
            if m:
                request.session['member_mobile'] = request.POST["number"]
                return redirect('member_home')
    return render(request, 'home/login.html')

def logout(request):
    if request.session.has_key('group_mobile'):
        del request.session['group_mobile']
    if request.session.has_key('member_mobile'):
        del request.session['member_mobile']
    return redirect('/')