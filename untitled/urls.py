"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from linkageApp.models import *


# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class DiseaseClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseClassifcation
        fields = ('name', 'code')


class PatientDonorLinkageSerializer(serializers.ModelSerializer):
    # patient = PatientSerializer()
    # donor = DonorOrganizationSerializer()
    # status = LinkageStatusSerializer()

    class Meta:
        model = PatientDonorLinkage
        fields = ('patient', 'donor', 'status', 'date_linked', 'date_completed')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('full_name', 'phone_number', 'email_address', 'country', 'county', 'sub_county', 'ward',
                  'treatment_supporter_name', 'treatment_supporter_phone_contact', 'treatment_supporter_email_address')


class DonorOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorOrganization
        fields = ('organization_name', 'contact_person', 'contact_phone_number', 'contact_email_address', 'country', 'county', 'sub_county', 'ward', 'preferred_eligibility' )


class LinkageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkageStatus
        fields = ('name', 'code')


class ExitStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExitStatus
        fields = ('name', 'code')




# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DiseaseClassificationViewSet(viewsets.ModelViewSet):
    queryset = DiseaseClassifcation.objects.all()
    serializer_class = DiseaseClassificationSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDonorLinkageViewSet(viewsets.ModelViewSet):
    queryset = PatientDonorLinkage.objects.all()
    serializer_class = PatientDonorLinkageSerializer


class DonorOrganizationViewSet(viewsets.ModelViewSet):
    queryset = PatientDonorLinkage.objects.all()
    serializer_class = DonorOrganizationSerializer


class LinkageStatusViewSet(viewsets.ModelViewSet):
    queryset = PatientDonorLinkage.objects.all()
    serializer_class = LinkageStatusSerializer


class ExitStatusViewSet(viewsets.ModelViewSet):
    queryset = ExitStatus.objects.all()
    serializer_class = ExitStatusSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'disease_classification', DiseaseClassificationViewSet)
router.register(r'patients', PatientsViewSet)
router.register(r'linkages', PatientDonorLinkageViewSet)
router.register(r'exit-status', ExitStatusViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
