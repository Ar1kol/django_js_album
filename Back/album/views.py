from django.http import JsonResponse
from django.shortcuts import render
from .serializers import ImageSerializer
from .models import Image
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    return JsonResponse({'server':'work'})

# get all images from DB to user
@api_view(['GET'])
def getImages(request):
    res = []  # create an empty list
    for img in Image.objects.all():
        # if img.type == type: # run on every row in the table...
        print(img)
        res.append({"title": img.title,
                    "content": img.content,
                    "type": img.type,
                    "image": str(img.image)
                    })  # append row by to row to res list
    return JsonResponse(res, safe=False)  # return array as json response


@api_view(['GET'])
def getImagesByType(request, get_type):
    res = []  # create an empty list
    for img in Image.objects.all().filter(type = get_type):
        res.append({"title": img.title,
                    "content": img.content,
                    "type": img.type,
                    "image": str(img.image)
                    })  # append row by to row to res list
    return JsonResponse(res, safe=False)  # return array as json response

class ImagesViews(APIView):
    parser_class = (MultiPartParser, FormParser)
   
    def post(self, request, *args, **kwargs):
        img_serializer = ImageSerializer(data=request.data)
        if img_serializer.is_valid():  # the serializer check our data
            img_serializer.save()  # save to DB (path,str) and save the actual file to directory
            return Response(img_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', img_serializer.errors)
            return Response(img_serializer.errors, status=status.HTTP_400_BAD_REQUEST)