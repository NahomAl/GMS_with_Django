from django.db import models

# Create your models here.
class Customer(models.Model):
    """Model definition for Customer."""
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['name', 'phone', 'email', 'address']
    
class Car(models.Model):
    """Model definition for Car."""
    plate_number = models.TextField(unique=True)
    model = models.TextField()
    make = models.TextField()
    vin = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plate_number
    class Meta:
        ordering = ['plate_number']

class Service(models.Model):
    """Model definition for Service."""
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Employee(models.Model):
    """Model definition for Employee."""
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Department(models.Model):
    """Model definition for Department."""
    name = models.TextField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class History(models.Model):
    """Model definition for History."""
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car} - {self.service}'
    class Meta:
        ordering = ['date_created']
