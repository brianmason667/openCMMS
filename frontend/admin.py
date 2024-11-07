from django.contrib import admin # type: ignore

# Register your models here.

from import_export import resources # type: ignore
from import_export.admin import ImportExportModelAdmin # type: ignore
from django.contrib import admin
from .models import Part  # Adjust the import based on your model's location

class PartResource(resources.ModelResource):
    class Meta:
        model = Part
        fields = ('id', 'item', 'partno', 'altpartno', 'descrip', 'bin_locat', 
                  'location', 'cost', 'stock', 'mfr', 'mfrpartno', 
                  'vpartno', 'onhand', 'onorder', 'supplier', 'active', 
                  'code', 'comment', 'history', 'class', 'lastordr', 
                  'lead', 'note', 'order_st', 'status', 'orderpt', 
                  'orderqty', 'supplierid', 'unitms')  # List all relevant fields

# Register the Part model with import/export functionality
@admin.register(Part)
class PartAdmin(ImportExportModelAdmin):
    resource_class = PartResource
