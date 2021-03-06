# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseClassifcation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
                ('voided', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Disease Classification',
                'verbose_name_plural': 'Disease Classification',
            },
        ),
        migrations.CreateModel(
            name='DonorOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('contact_phone_number', models.CharField(max_length=15)),
                ('contact_email_address', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=15)),
                ('sub_county', models.CharField(max_length=20)),
                ('ward', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Donor Organization',
                'verbose_name_plural': 'Donor Organizations',
            },
        ),
        migrations.CreateModel(
            name='EligibilityCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
                ('voided', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Eligibility Criterion',
                'verbose_name_plural': 'Eligibility Criteria',
            },
        ),
        migrations.CreateModel(
            name='ExitStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
                ('voided', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Exit Status',
                'verbose_name_plural': 'Exit Status',
            },
        ),
        migrations.CreateModel(
            name='HealthCareWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('email_address', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=15)),
                ('sub_county', models.CharField(max_length=20)),
                ('ward', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Health Care Worker',
                'verbose_name_plural': 'Health Care Workers',
            },
        ),
        migrations.CreateModel(
            name='LinkageStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
                ('voided', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Linkage Status',
                'verbose_name_plural': 'Linkage Status',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('email_address', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=15)),
                ('sub_county', models.CharField(max_length=20)),
                ('ward', models.CharField(max_length=20)),
                ('treatment_supporter_name', models.CharField(max_length=50)),
                ('treatment_supporter_phone_contact', models.CharField(max_length=50)),
                ('treatment_supporter_email_address', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='PatientDonorLinkage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_linked', models.DateField()),
                ('date_completed', models.DateField()),
                ('comment', models.CharField(max_length=250)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkageApp.DonorOrganization')),
                ('exit_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkageApp.ExitStatus')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkageApp.Patient')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkageApp.LinkageStatus')),
            ],
            options={
                'verbose_name': 'Linkage',
                'verbose_name_plural': 'Linkage',
            },
        ),
        migrations.AddField(
            model_name='donororganization',
            name='preferred_eligibility',
            field=models.ManyToManyField(to='linkageApp.EligibilityCriteria', verbose_name='Preferred Eligibility'),
        ),
    ]
