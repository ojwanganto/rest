from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(HealthCareWorker)
admin.site.register(DonorOrganization)
admin.site.register(DiseaseClassifcation)
admin.site.register(LinkageStatus)
admin.site.register(ExitStatus)
admin.site.register(EligibilityCriteria)
admin.site.register(Patient)
admin.site.register(PatientDonorLinkage)