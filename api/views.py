from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.apps import apps
from .models import Palette, Color, Favorite

@api_view(['GET'])
def get_public_palettes(request):
    #Get all the palletes that has visibility set to public
    palettes = Palette.objects.filter(palette_visibility='public').values('id', 'palette_name')
    idNamePairs = []
    #Get the IDs and Names of the public color palettes
    for palette in palettes:
        idNamePairs.append((palette['id'], palette['palette_name']))
    data = []
    for idNamePair in idNamePairs :
        #Get the all the color that with a particular palette ID
        colors = Color.objects.filter(color_palette_id=idNamePair[0]).values()
        dominant = []
        accent = []
        for color in colors:
            type = color['color_type']
            name = color['color_name']
            #Split color according to type
            if type == 'dominant':
                dominant.append(name)
            else:
                accent.append(name)
        data.append({'palette_id': idNamePair[0], 'palette_name': idNamePair[1],'dominant': dominant, 'accent': accent})
    return Response(data)
	
@api_view(['POST'])
def add_to_favorite(request):
    if request.method == 'POST':
        serializer = Favorite.serialize(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return redirect('home')

# @api_view(['POST'])
def create_color_pallete(request):
    if request.method == 'POST':
        print(request.POST)
        p_name = request.POST['palette_name']
        p_owner = request.user.username
        p_visibility = request.POST['palette_visibility']
        c_name = request.POST['color_name']
        c_type = request.POST['color_type']
        palette = Palette(palette_name=p_name, palette_owner=p_owner, palette_visibility=p_visibility)
        palette.save()
        c_p_id = palette.id
        Color(color_name=c_name, color_type=c_type, color_palette_id=c_p_id).save()
        return redirect('home')
    return render(request, 'createpalette.html')