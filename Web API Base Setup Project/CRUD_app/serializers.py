from rest_framework import serializers 
from .models import patient

 
class patientSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = patient
        fields = (
                  'name',
                  'activity',
                  'age',
                  'time')