from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import  ImageSerializer, PersonDetailSerializer, GETPersonDetailSerializer
from rest_framework.response import Response
from .models import *

class DetailAPIView(APIView):
    def get(self, request):
        queryset = PersonDetailModel.objects.all()
        serializer = GETPersonDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):       
        serializer = PersonDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            image = ImageModel.objects.filter(owner__email=serializer.validated_data['email']).values_list("image")
            data = {
                'name':serializer.validated_data['name'],
                'email':serializer.validated_data['email'],
                'date_of_birth':serializer.validated_data['date_of_birth'],
                'image':image
            }
            return Response(data)

    
     # data = request.data
        
        # name = request.data['name']
        # email = request.data['email']
        # date_of_birth = request.data['date_of_birth']
        # dict1 = {}
        # dict1['name']=name
        # dict1['email']=email
        # dict1['date_of_birth']=date_of_birth
        # resp = []
        # for i in image:
        #     # print("________________________________________",str(i))
        #     # dict1['images']=i
        #     resp.append(str(i))
        # print("_____RESP--------->>>>>_________",resp)
        # dict1['images']=resp
        # print("________DICT-DICT__________",dict1)
        # print("_______________________________________",data)

# class ImageAPIView(APIView):
#     def get(self, request):
#         queryset = ImageModel.objects.all()
#         serializer = ImageSerializer(queryset, many=True)
#         return Response(serializer.data)
