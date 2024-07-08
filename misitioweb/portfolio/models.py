from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    description = RichTextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")
    url = models.URLField(verbose_name="URL", null=True, blank=True)

class Meta:
    verbose_name = "proyecto"
    verbose_name_plural = "proyectos"
    ordering = ["-created"]
def __str__(self):
        return self.title