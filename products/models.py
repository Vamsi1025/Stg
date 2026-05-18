from django.db import models
from django.conf import settings
from urllib.parse import quote

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('vitrified', 'Vitrified Tiles'),
        ('bathroom', 'Bathroom Tiles'),
        ('sanitaryware', 'Sanitaryware'),
        ('granite', 'Granite'),
    ]

    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def whatsapp_url(self):
        text = f"Hi, I am interested in {self.name} ({self.get_category_display()}). Please share more details."
        return f"https://wa.me/{settings.WHATSAPP_NUMBER}?text={quote(text)}"
