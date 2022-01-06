from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Groupe(models.Model):

    class Genre(models.TextChoices):
        CLASSIQUE = 'CLSQ', _('Classique')
        MODERNE = 'MDRN' , _('Moderne')
        JAZZ = 'Jazz', _('Jazz')
        POPULAIRE = 'POPU', _('Populaire')
        WORLD = 'WRLD', _('World musique')
        INDETERMINE ='INDT', _('Indéterminé')

    nom = models.fields.CharField(max_length = 100)
    annee_crea = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    actif = models.fields.BooleanField()
    genre = models.fields.CharField(max_length = 4, choices = Genre.choices, default= Genre.INDETERMINE)                                
    biographie = models.fields.TextField(blank=True)
    add_site = models.fields.URLField()
    add_mail = models.fields.EmailField()

    def __str__(self):
        return f'{self.nom}'

class Fetiche(models.Model):

    class Support(models.TextChoices):
        AFFICHE = 'AFFCH', _('Affiche')
        SCULPTURE = 'SCULP', _('Sculpture')
        VINYL = 'VINYL', _('Disque vinyl')
        TEXTILE = 'TXTIL', _('Textile, vetement, Tshirt')
        INDETERMINE = 'INDT', _('Indetermine')
    
    class FormatAffiche(models.TextChoices):
        RAISIN = 'RAI', _('Format raisin')
        DEMIRAISIN = 'A00', _('Demi raisin A0')
        AFFICHETTE = 'A01', _('Affichette MJC')
        MENU = 'A05', _('Format menu')
        FLYER = 'A06',_('Demi menu')
        INDETERMINE = 'IND', _('Indetermine')

    nom = models.fields.CharField(max_length = 100)
    annee_crea = annee_crea = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    form_aff = models.fields.CharField(max_length = 3, choices = FormatAffiche.choices, default= FormatAffiche.INDETERMINE)
    type_support = models.fields.CharField(max_length = 5, choices = Support.choices, default= Support.INDETERMINE)

    groupe = models.ForeignKey('Groupe', null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return f'{self.nom}'





