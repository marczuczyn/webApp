from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse_lazy, reverse


class Ankieta(models.Model):
    PLEC_CHOICES = (
        ('K', 'Kobieta'),
        ('M', 'Mężczyzna')
    )
    KOLOR_CHOICES = (
        ('Z', 'Zielony'),
        ('N', 'Niebieski'),
        ('C', 'Czerwony')
    )
    wiek = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    wzrost = models.PositiveSmallIntegerField(validators=[MinValueValidator(50), MaxValueValidator(250)])
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES)
    kolor = models.CharField(max_length=1, choices=KOLOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ankiety'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.wiek} lat - {self.wzrost}cm - {self.plec}"

    def get_url(self):
        return reverse_lazy('ankieta_detail', args={'pk': self.pk})

    def serialize(self):
        return {
            'wiek': self.wiek,
            'wzrost': self.wzrost,
            'plec': self.get_plec_display(),
            'kolor': self.get_kolor_display(),
            'view': f'''<a href="/detail/{self.id}"><button type="button" class="btn btn-primary btn-sm">Detail</button></a>'''
        }
