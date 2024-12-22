# Generated by Django 5.1.1 on 2024-12-19 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_loan_demand_member_installment_member_loan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_bank_loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.FloatField()),
                ('minimum_loan_installment', models.FloatField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('loan_status', models.IntegerField(default=1)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='group.group')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='group.member')),
            ],
        ),
        migrations.CreateModel(
            name='Member_sangh_loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.FloatField()),
                ('minimum_loan_installment', models.FloatField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('loan_status', models.IntegerField(default=1)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='group.group')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='group.member')),
            ],
        ),
    ]
