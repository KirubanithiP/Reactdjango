from rest_framework import fields, serializers
from backend.models import Students
from .models import Websites
from backend.models import Barcode
# serializers.py in backend app
from .models import ExcelFile


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Students
		fields = ('studentId',
			      'Firstname',
			       'Lastname',
			       'Email',
			       'Course')
        
		


class WebsitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Websites
        fields = '__all__'




class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ('id', 'code', 'image')

class ExcelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = '__all__'

