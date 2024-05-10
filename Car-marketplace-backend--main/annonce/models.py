from django.db import models

# Create your models here.
from django.db import models
from django.core.files.uploadedfile import UploadedFile
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from users.models import CustomUser
# For testing model validation
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10  # 10mb
def file_validation(file):
    if not file:
        raise ValidationError("No file selected.")

    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError("File shouldn't be larger than 10MB.")
# Create your models here.
class Energie(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Carrosserie(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Couleurs(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Marque(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self):
        return self.name
class Modele(models.Model):
    marque=models.ForeignKey(Marque,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Generation(models.Model):
    modele=models.ForeignKey(Modele,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Transmission(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name
class Sellerie(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Car_images(models.Model):
    voiture = models.ForeignKey('Voiture', related_name='images', on_delete=models.CASCADE)
    image=CloudinaryField("Image",format="jpg",overwrite=True,validators=[file_validation],null=True)
    def __str__(self):
        return f"image for {self.voiture.__str__()}"

class Voiture(models.Model):
    BOITE_CHOICES = [
        ('Manuelle', 'Manuelle'),
        ('Automatique', 'Automatique')
    ]
    fenitions=models.TextField(max_length=150,null=True,blank=True)
    about=models.TextField(blank=True)
    marque=models.ForeignKey(Marque,on_delete=models.SET_NULL,null=True)
    modele=models.ForeignKey(Modele,on_delete=models.SET_NULL,null=True)
    kilometrage = models.IntegerField()
    mise_en_circulation = models.DateField()
    energie = models.ForeignKey(Energie, on_delete=models.SET_NULL, null=True)
    carrosserie = models.ForeignKey(Carrosserie, on_delete=models.SET_NULL, null=True)
    boite = models.CharField(max_length=50,choices=BOITE_CHOICES)
    transmission = models.ForeignKey(Transmission,on_delete=models.SET_NULL, null=True)
    couleur_externe = models.ForeignKey(Couleurs, on_delete=models.SET_NULL, null=True, related_name='exterieur_voitures')
    couleur_interieur = models.ForeignKey(Couleurs, on_delete=models.SET_NULL, null=True, related_name='interieur_voitures')
    nombre_de_portes=models.IntegerField()
    nombre_de_places=models.IntegerField()
    cylidre_cm3=models.IntegerField()
    sellerie=models.ForeignKey(Sellerie,on_delete=models.SET_NULL,null=True)
    generation=models.ForeignKey(Generation,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f" marque {self.marque.__str__()} modele {self.modele.name} mise en circulation {str(self.mise_en_circulation)}"
class Vente(models.Model):
    ANNONCE_TYPES = (
        ('regulier', 'Prix régulier'),
        ('leasing', 'Sous leasing'),
        ('non_dedouiane', 'Non dédouiane'),
    )

    vente_type = models.CharField(max_length=20, choices=ANNONCE_TYPES)
    prix = models.IntegerField()

    # For 'sous leasing'
    CESSION_PRICE = models.IntegerField(blank=True, null=True)
    LOYER_PRIX = models.IntegerField(blank=True, null=True)
    MENSUALITES = models.IntegerField(blank=True, null=True)

    # For 'non dedouiane'
    FRAIS_DE_DOUANE = models.IntegerField(blank=True, null=True)
    CESSION_PRIX = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f"{self.vente_type} prix {self.prix}"

    @property
    def calculated_prix(self):
        if self.vente_type == 'leasing':
            return self.CESSION_PRICE + (self.LOYER_PRIX * self.MENSUALITES)
        elif self.vente_type == 'non_dedouiane':
            return self.FRAIS_DE_DOUANE + self.CESSION_PRIX
        else:
            return self.prix
class Gouvernorat(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Annonce(models.Model):
    verified=models.BooleanField(default=False)
    voitures=models.ForeignKey(Voiture,on_delete=models.CASCADE)
    GOUVERNORAT_CHOICES = [
        ("Ariana", "Ariana"),
        ("Béja", "Béja"),
        ("Ben Arous", "Ben Arous"),
        ("Bizerte", "Bizerte"),
        ("Gabès", "Gabès"),
        ("Gafsa", "Gafsa"),
        ("Jendouba", "Jendouba"),
        ("Kairouan", "Kairouan"),
        ("Kasserine", "Kasserine"),
        ("Kébili", "Kébili"),
        ("La Manouba", "La Manouba"),
        ("Le Kef", "Le Kef"),
        ("Mahdia", "Mahdia"),
        ("Médenine", "Médenine"),
        ("Monastir", "Monastir"),
        ("Nabeul", "Nabeul"),
        ("Sfax", "Sfax"),
        ("Sidi Bouzid", "Sidi Bouzid"),
        ("Siliana", "Siliana"),
        ("Sousse", "Sousse"),
        ("Tataouine", "Tataouine"),
        ("Tozeur", "Tozeur"),
        ("Tunis", "Tunis"),
        ("Zaghouan", "Zaghouan")
    ]

    adresss = models.TextField()
    telephone = models.IntegerField()
    gouvernoment = models.ForeignKey(Gouvernorat,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    vente=models.OneToOneField(Vente,on_delete=models.CASCADE)
    def __str__(self):
        return f"adress {self.adresss} user {self.user.email} voiture {self.voitures.__str__()}"


