from django.db import models
from maintenancemanagement.models import *
# ^^^ Import API models

# Create your frontend models here.

class Supplier(models.Model):
    """Define a supplier."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Part(models.Model):
    """Define a part inventory item."""
    part_number = models.CharField(max_length=50, blank=True, help_text="Part number of the item.")
    alt_part_number = models.CharField(max_length=50, blank=True, null=True, help_text="Alternate part number.")
    description = models.CharField(max_length=255, help_text="Description of the part.")
    bin_location = models.CharField(max_length=50, help_text="Bin location for storage.")
    location = models.CharField(max_length=50, help_text="General location of the part.")
    cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cost of the part.")
    stock = models.BooleanField(default=True, help_text="Indicates if the part is in stock.")
    manufacturer = models.CharField(max_length=100, help_text="Name of the manufacturer.")
    manufacturer_part_number = models.CharField(max_length=50, blank=True, null=True, help_text="Manufacturer's part number.")
    vpart_number = models.CharField(max_length=50, blank=True, null=True, help_text="Vendor part number.")
    on_hand = models.FloatField(help_text="Quantity on hand.")
    on_order = models.FloatField(help_text="Quantity on order.")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True, help_text="Indicates if the part is active.")
    code = models.CharField(max_length=50, blank=True, null=True, help_text="Code for the part.")
    comment = models.TextField(blank=True, null=True, help_text="Additional comments.")
    history = models.TextField(blank=True, null=True, help_text="History of the part.")
    part_class = models.CharField(max_length=50, help_text="Class of the part.")
    last_order = models.DateField(null=True, blank=True, help_text="Date of the last order.")
    lead_time = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Lead time for orders.")
    note = models.TextField(blank=True, null=True, help_text="Additional notes.")
    order_status = models.CharField(max_length=50, blank=True, null=True, help_text="Order status.")
    status = models.CharField(max_length=50, blank=True, null=True, help_text="Current status of the part.")
    order_point = models.FloatField(null=True, blank=True, help_text="Minimum quantity before reordering.")
    order_quantity = models.FloatField(null=True, blank=True, help_text="Quantity to order.")
    unit_of_measure = models.CharField(max_length=50, help_text="Unit of measure for the part.")

    def __str__(self):
        return f"{self.description} ({self.part_number})"

    def __repr__(self):
        return f"<Part: id={self.id}, part_number={self.part_number}, description={self.description}>"
