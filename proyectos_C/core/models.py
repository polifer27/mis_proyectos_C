from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name ="Título")
    description = models.TextField(verbose_name ="Descripción")
    image = models.ImageField(verbose_name ="Imagen", upload_to="projects")
    adminupload = models.FileField(upload_to='media')
    created = models.DateTimeField(auto_now_add=True, verbose_name ="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name ="Fecha de edición")
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        #El menos por delante hace que primero se vean o aparezcan los 
        #proyectos más recientes
        ordering = ["-created"] 

    def __str__(self):
        return self.title   

#class FilesAdmin(models.Model):
#    adminupload = models.FileField(upload_to='media')
#    title=models.CharField(max_length=50)
#    def __str__(self):
#        return self.title     