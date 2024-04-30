from rest_framework import serializers
from DRF_App.models import Usage, Zone, ConstructionElement, Batiment


class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = '__all__'


class ConstructionElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionElement
        fields = '__all__'


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


class BatimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batiment
        fields = '__all__'
