from django.db import models

# Create your models here.
class bunbase(models.Model):
    title=models.CharField()
    description=models.TextField(blank=True)
    create_ad=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    time=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="bun base"
        verbose_name_plural="bun base"