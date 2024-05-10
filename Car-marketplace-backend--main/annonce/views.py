from rest_framework import generics, response, status
from rest_framework.decorators import api_view
from .models import *
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from .renderers import *
from .serializers import *
class EnergieListAPIVieu(generics.ListAPIView):
    serializer_class=EnergieSerializers
    def get_queryset(self):
        return Energie.objects.all()
class CarrosserieListAPIVieu(generics.ListAPIView):
    serializer_class=CarrosserieSerializers
    def get_queryset(self):
        return Carrosserie.objects.all()

class CouleursListAPIVieu(generics.ListAPIView):
    serializer_class=CouleursSerializers
    def get_queryset(self):
        return Couleurs.objects.all()
class ModeleListAPIVieu(generics.ListAPIView):
    serializer_class=ModeleSerializers
    def get_queryset(self):
        return Modele.objects.all()
class MarqueListAPIVieu(generics.ListAPIView):
    serializer_class=MarqueSerializers
    def get_queryset(self):
        return Marque.objects.all()
class GenerationListAPIVieu(generics.ListAPIView):
    serializer_class=GenerationSerializers
    def get_queryset(self):
        return Generation.objects.all()
class TransmissionListAPIVieu(generics.ListAPIView):
    serializer_class=TransmissionSerializers
    def get_queryset(self):
        return Transmission.objects.all()
class SellerieListAPIVieu(generics.ListAPIView):
    serializer_class=SellerieSerializers
    def get_queryset(self):
        return Sellerie.objects.all()
class VoitureListAPIVieu(generics.ListAPIView):
    serializer_class=VoitureSerializers
    def get_queryset(self):
        return Voiture.objects.all()
class AnnonceListAPIVieu(generics.ListAPIView):
    serializer_class=AnnonceSerializers
    def get_queryset(self):
        return Annonce.objects.all()
class Car_ImagesListAPIVieu(generics.ListAPIView):
    serializer_class=Car_imagesSerializers
    def get_queryset(self):
        return Car_images.objects.all()
class CarAddView(APIView):
    renderer_classes = [ModelsRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=VoitureCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data,status=status.HTTP_200_OK)
class VenteaddView(APIView):
    renderer_classes = [ModelsRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=VenteSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data,status.HTTP_200_OK)
class AnnonceAddView(APIView):
    renderer_classes = [ModelsRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer=AnnonceCreateSerializers(data=request.data,context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data,status=status.HTTP_200_OK)
class GetCarImagesView(generics.GenericAPIView):
    serializer_class = Car_imagesSerializers
    queryset = None
    def get(self,request,car_id):
        self.queryset=Car_images.objects.filter(voiture__id=car_id)
        if self.queryset:
            return response.Response(self.serializer_class(self.queryset,many=True).data)
        else:
            return response.Response({"msg":"no images availeblase for this car"},status=status.HTTP_404_NOT_FOUND)
