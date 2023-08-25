from django.urls import path
from . import views

urlpatterns = [
    path('palettes/public/', views.get_public_palettes),
    path('addtofav/', views.add_to_favorite),
    path('createpalette/', views.create_color_pallete, name='createpalette')

]