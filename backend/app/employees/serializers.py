from rest_framework import serializers

from employees.models import Area, SubArea, Document, Employee


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'name', 'doc_format')
        read_only_fields = ('id',)


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('id', 'name')
        read_only_fields = ('id',)


class SubAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubArea
        fields = ('id', 'name', 'area')
        read_only_fields = ('id',)


class EmployeeSerializer(serializers.ModelSerializer):
    area = serializers.CharField(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('id', 'documento', 'area')
