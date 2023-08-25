from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.apps import apps
from .models import Palette, Color, Favorite

@api_view(['GET'])
def get_public_palettes(request):
    #Get all the palletes that has visibility set to public
    palettes = Palette.objects.filter(visibility='public').values('id')
    ids = []
    #Get the IDs of the public color palettes
    for palette in palettes:
        ids.append(palette['id'])
    data = []
    for id in ids:
        #Get the all the color that with a particular palette ID
        colors = Color.objects.filter(palette_id=id).values()
        dominant = []
        accent = []
        for color in colors:
            type = color['type']
            name = color['name']
            #Split color according to type
            if type == 'dominant':
                dominant.append(name)
            else:
                accent.append(name)
        data.append({'palette_id': id, 'dominant': dominant, 'accent': accent})
    return Response(data)
	
