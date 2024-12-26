from django.db import models

# Create your models here.
class Group(models.Model):
    group_name=models.CharField(max_length=100)
    mobile = models.IntegerField()
    pin = models.IntegerField()
    address = models.CharField(max_length=1000, default='')
    member_installment_limit = models.FloatField(default=0)
    maximum_loan = models.FloatField(default=0)
    loan_interest = models.FloatField(default=0)
    loan_bank_interest = models.FloatField(default=0)
    loan_sangh_interest = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True,null=True)
    starting_total_interest_amount = models.FloatField(null=True)

class Member(models.Model):
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    mobile = models.IntegerField()
    pin = models.IntegerField()
    status = models.IntegerField(default=1)
    
class Member_loan(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    loan_amount = models.FloatField()
    minimum_loan_installment = models.FloatField(default=0) 
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    loan_status = models.IntegerField(default=1)
    
class Member_bank_loan(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    loan_amount = models.FloatField()
    minimum_loan_installment = models.FloatField(default=0) 
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    loan_status = models.IntegerField(default=1)
    
class Member_sangh_loan(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    loan_amount = models.FloatField()
    minimum_loan_installment = models.FloatField(default=0) 
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    loan_status = models.IntegerField(default=1)
    
class Member_installment(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
class Member_bank_loan_installment(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    loan = models.ForeignKey(Member_bank_loan,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    installment_amount = models.FloatField()
    interest_amount = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
class Member_sangh_loan_installment(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    loan = models.ForeignKey(Member_sangh_loan,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    installment_amount = models.FloatField()
    interest_amount = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
class Member_loan_installment(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    loan = models.ForeignKey(Member_loan,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    installment_amount = models.FloatField()
    interest_amount = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    

    
class Member_bank_loan_installment(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    loan = models.ForeignKey(Member_bank_loan,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    installment_amount = models.FloatField()
    interest_amount = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
class Member_sangh_loan_installment(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    loan = models.ForeignKey(Member_sangh_loan,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    installment_amount = models.FloatField()
    interest_amount = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
class Loan_demand(models.Model):
    member = models.ForeignKey(Member,on_delete=models.PROTECT,null=True)
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    demand_amount = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    