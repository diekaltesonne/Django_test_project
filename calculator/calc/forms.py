from rest_framework import serializers

class TruckDataSerializer(serializers.Serializer):
    truck_id = serializers.IntegerField(required=True, min_value=0)
    coordinate_x = serializers.IntegerField(required=True, min_value=0)
    coordinate_y = serializers.IntegerField(required=True, min_value=0)

class ValidateFormSerializer(serializers.Serializer):
    trucks = serializers.ListField(child=TruckDataSerializer())