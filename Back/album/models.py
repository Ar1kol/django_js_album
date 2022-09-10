from django.db import models

# Create your models here.

class MetaModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        abstract = True

class Image(MetaModel):
    title=models.CharField(max_length=100, blank=True, null=True)
    content=models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10)
    image=models.ImageField(upload_to='Images')

    class Meta:
        db_table = 'Images'
 
    def __str__(self):
        return f"{self.title} {self.type}"