from rest_framework import serializers
from restful_api.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Device model.
    """

    class Meta:
        model = Device
        fields = '__all__'  # Include all fields from the Device model