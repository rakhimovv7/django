from django.db import models

# Create your models here.
class Base(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name="Логотип сайта"
    )
    banner = models.ImageField(
        upload_to='banner/',
        verbose_name="Фото баннера"
    )
    phone = models.IntegerField(
        verbose_name="Номер телефона",
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank=True, null=True        
    )
    instagram = models.URLField(
        verbose_name="instagram",
        blank=True, null=True        
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"