from rest_framework import serializers
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class EnergieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Energie
        fields="__all__"
class CarrosserieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Carrosserie
        fields="__all__"
class CouleursSerializers(serializers.ModelSerializer):
    class Meta:
        model=Couleurs
        fields="__all__"
class MarqueSerializers(serializers.ModelSerializer):
    class Meta:
        model=Marque
        fields="__all__"
class ModeleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Modele
        fields="__all__"
class GenerationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Generation
        fields="__all__"
class TransmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Transmission
        fields="__all__"
class SellerieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Sellerie
        fields="__all__"
class Car_imagesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Car_images
        fields="__all__"
class VoitureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = "__all__"
class AnnonceSerializers(serializers.ModelSerializer):
    class Meta:
        model=Annonce
        fields="__all__"
class AnnonceCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model=Annonce
        fields=["adresss","telephone","gouvernoment","vente","voitures"]
    def create(self, validated_data):
        user=self.context.get("user")
        return Annonce.objects.create(user=user,**validated_data)
class VoitureCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Voiture
        fields="__all__"
    def create(self, validated_data):
        return Voiture.objects.create(**validated_data)
class VenteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vente
        fields="__all__"

# class Annonce_createSerializers(serializers.ModelSerializer):
#


