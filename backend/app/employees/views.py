import re

from django.db.models import Q

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from employees.serializers import AreaSerializer, SubAreaSerializer, \
    DocumentSerializer, EmployeeSerializer
from employees.models import Area, SubArea, Document, Employee


class SmallPagination(PageNumberPagination):
    page_size = 10


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()


class SubAreaViewSet(viewsets.ModelViewSet):
    serializer_class = SubAreaSerializer
    queryset = SubArea.objects.all()

    def get_queryset(self):
        area = self.request.query_params.get('area', None)
        if area:
            return self.queryset.filter(area=area)
        return self.queryset


class EmployeeVewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    pagination_class = SmallPagination

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        queryset = self.queryset

        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(document__contains=query)
            )
        return queryset

    def perform_create(self, serializer):
        document = Document.objects.get(id=self.request.data['document_type'])
        pattern = re.compile(document.doc_format)
        if not pattern.match(self.request.data['document']):
            return Response(
                {'error': 'Document type pattern does not match'},
                status=status.HTTP_400_BAD_REQUEST
            )
        sub_area = SubArea.objects.get(id=self.request.data['sub_area'])
        serialized_data = self.get_serializer(data=self.request.data)
        if serialized_data.is_valid():
            serialized_data.save(area=sub_area.area)
