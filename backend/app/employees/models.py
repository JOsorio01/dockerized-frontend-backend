from django.db import models


class Document(models.Model):
    """Document model"""
    name = models.CharField(max_length=100)
    doc_format = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Area(models.Model):
    """Area model"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubArea(models.Model):
    name = models.CharField(max_length=255)
    area = models.ForeignKey('Area', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    document_type = models.ForeignKey('Document', on_delete=models.DO_NOTHING)
    document = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    area = models.ForeignKey('Area', on_delete=models.DO_NOTHING)
    sub_area = models.ForeignKey('SubArea', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
