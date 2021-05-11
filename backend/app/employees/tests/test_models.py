from django.test import TestCase

from employees.models import Document, Area, SubArea, Employee


class DocumentTypeTests(TestCase):

    def test_document_string_representation(self):
        document = Document.objects.create(
            name='DUI',
            doc_format=r'^([0-9]{8})-[0-9]$'
        )
        self.assertEqual(str(document), document.name)


class AreaTests(TestCase):

    def test_area_string_representation(self):
        area = Area.objects.create(name="Area 1")
        self.assertEqual(str(area), area.name)


class SubAreaTests(TestCase):

    def test_sub_area_string_representation(self):
        area = Area.objects.create(name="Area 1")
        sub_area = SubArea.objects.create(name="Sub Area 1", area=area)
        self.assertEqual(str(sub_area), sub_area.name)


class EmployeeTests(TestCase):

    def setUp(self):
        self.area = Area.objects.create(name="Area 1")
        self.sub_area = SubArea.objects.create(
            name="Sub Area 1", area=self.area)
        self.document = Document.objects.create(
            name='DUI', doc_format=r'^([0-9]{8})-[0-9]$')

    def test_employee_string_representation(self):
        employee = Employee.objects.create(
            document_type=self.document,
            document='12345678-9',
            first_name="First Name",
            last_name="Last Name",
            area=self.area,
            sub_area=self.sub_area
        )
        self.assertEqual(
            str(employee), f'{employee.first_name} {employee.last_name}'
        )
