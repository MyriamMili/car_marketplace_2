from django.urls import path
from .views import *
urlpatterns = [
    path('car_images',Car_ImagesListAPIVieu.as_view(),name="all_car_images"),
    path('get_car_image/<int:car_id>',GetCarImagesView.as_view(),name="get_car_images"),
    path('addvente',VenteaddView.as_view(),name="add_vente"),
    path('addannonce',AnnonceAddView.as_view(),name="add_annoce"),
    path('addcar',CarAddView.as_view(),name="add_car"),
    path('energie', EnergieListAPIVieu.as_view(), name="all_energie"),
    path('carrosserie', CarrosserieListAPIVieu.as_view(), name="all_carrosserie"),
    path('couleurs', CouleursListAPIVieu.as_view(), name="all_couleurs"),
    path('modele', ModeleListAPIVieu.as_view(), name="all_modele"),
    path('marque', MarqueListAPIVieu.as_view(), name="all_marque"),
    path('generation', GenerationListAPIVieu.as_view(), name="all_generation"),
    path('transmission', TransmissionListAPIVieu.as_view(), name="all_transmission"),
    path('sellerie', SellerieListAPIVieu.as_view(), name="all_sellerie"),
    path('voiture', VoitureListAPIVieu.as_view(), name="all_voiture"),
    path('annonce', AnnonceListAPIVieu.as_view(), name="all_annonce"),
]