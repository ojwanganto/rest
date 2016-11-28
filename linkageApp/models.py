from __future__ import unicode_literals

from django.db import models

# Create your models here.


class HealthCareWorker(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    email_address = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=15, blank=False)
    sub_county = models.CharField(max_length=20, blank=False)
    ward = models.CharField(max_length=20, blank=False)
    profession = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.full_name)

    class Meta(object):
        verbose_name = 'Health Care Worker'
        verbose_name_plural = 'Health Care Workers'


class EligibilityCriteria(models.Model):
    name = models.CharField(max_length=20, blank=False)
    code = models.IntegerField(blank=False)
    voided = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta(object):
        verbose_name = 'Eligibility Criterion'
        verbose_name_plural = 'Eligibility Criteria'


class DonorOrganization(models.Model):
    organization_name = models.CharField(max_length=50, blank=False)
    contact_person = models.CharField(max_length=50, blank=False)
    contact_phone_number = models.CharField(max_length=15, blank=False)
    contact_email_address = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=15, blank=False)
    sub_county = models.CharField(max_length=20, blank=False)
    ward = models.CharField(max_length=20, blank=False)
    preferred_eligibility = models.ManyToManyField(EligibilityCriteria, verbose_name="Preferred Eligibility")

    def __str__(self):
        return '{}'.format(self.organization_name)

    class Meta(object):
        verbose_name = 'Donor Organization'
        verbose_name_plural = 'Donor Organizations'


class DiseaseClassifcation(models.Model):
    name = models.CharField(max_length=20, blank=False)
    code = models.IntegerField(blank=False)
    voided = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta(object):
        verbose_name = 'Disease Classification'
        verbose_name_plural = 'Disease Classification'


class LinkageStatus(models.Model):
    name = models.CharField(max_length=20, blank=False)
    code = models.IntegerField(blank=False)
    voided = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta(object):
        verbose_name = 'Linkage Status'
        verbose_name_plural = 'Linkage Status'


class ExitStatus(models.Model):
    name = models.CharField(max_length=20, blank=False)
    code = models.IntegerField(blank=False)
    voided = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta(object):
        verbose_name = 'Exit Status'
        verbose_name_plural = 'Exit Status'


class Patient(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    email_address = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=15, blank=False)
    sub_county = models.CharField(max_length=20, blank=False)
    ward = models.CharField(max_length=20, blank=False)
    treatment_supporter_name = models.CharField(max_length=50)
    treatment_supporter_phone_contact = models.CharField(max_length=50)
    treatment_supporter_email_address = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.full_name)

    class Meta(object):
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class PatientDonorLinkage(models.Model):
    patient = models.ForeignKey(Patient)
    donor = models.ForeignKey(DonorOrganization, related_name='donor')
    status = models.ForeignKey(LinkageStatus, blank=True, null=True, related_name='linkage_status')
    date_linked = models.DateField()
    date_completed = models.DateField(blank=True, null=True)
    exit_status = models.ForeignKey(ExitStatus, blank=True, null=True)
    comment = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.patient)

    class Meta(object):
        verbose_name = 'Linkage'
        verbose_name_plural = 'Linkage'

