# Generated by Django 5.1.1 on 2024-12-19 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_member_bank_loan_member_sangh_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_bank_loan_installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment_amount', models.FloatField()),
                ('interest_amount', models.FloatField(null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='group.group')),
                ('loan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='group.member_bank_loan')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='group.member')),
            ],
        ),
    ]
