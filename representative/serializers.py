from rest_framework import serializers
from representative.models import Representative

class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        fields = ['representative_id', 'representative_name', 'is_active_working', 'start_date']