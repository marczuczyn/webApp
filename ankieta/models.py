from django.db import models


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
    wiek = models.PositiveSmallIntegerField()
    wzrost = models.PositiveSmallIntegerField()
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES)
    kolor = models.CharField(max_length=1, choices=KOLOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ankiety'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.wiek} lat - {self.wzrost}cm - {self.plec}"
