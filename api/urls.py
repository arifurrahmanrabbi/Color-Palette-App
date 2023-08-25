from django.urls import path
from . import views

urlpatterns = [
    #Returns all palettes that has visibilty set to public
    path('palettes/public/', views.get_public_palettes),
    path('addtofav/', views.add_to_favorite)

]