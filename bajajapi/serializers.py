from rest_framework import serializers
from .models import Bajaj

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bajaj
        fields = ['is_success', 'user_id', 'numbers', 'odd', 'even']