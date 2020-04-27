from django.db import models
from django.db.models import FileField

class Equipment(models.Model):
    """
        Define an equipment.
    """
    name = models.CharField(max_length=100)
    equipment_type = models.ForeignKey(EquipmentType,
        verbose_name = "Equipment Type",
        on_delete = models.DELETE_CASCADE,
        null = False,
        related_name = "equipment_set",
        related_query_name="equipment")
    #gestion d'un fichier, voir pour en gérer plusieurs
    #upload = models.FileField(upload_to = 'uploads/equipment/')
