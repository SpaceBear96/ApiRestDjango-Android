from django.db import models

# Create your models here.
class Usuario (models.Model):

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    correo=models.CharField(max_length=250)
    imagen=models.FileField(upload_to='storage/images/', max_length=250, null=True)
    tipo=models.CharField(max_length=100)
    
    class Meta:
        db_table = "usuario"
        
    def __str__(self):
        return self.nombre 

