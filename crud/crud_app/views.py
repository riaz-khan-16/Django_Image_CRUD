from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from crud_app.models import Intro
from crud_app.serializers import CrudSerializer




@api_view(['GET', 'POST'])
def crud_list(request):
   
    if request.method == 'GET':
        snippets = Intro.objects.all()
        serializer = CrudSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CrudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def crud_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        person = Intro.objects.get(id=id)
    except Intro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CrudSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CrudSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

# @api_view(['GET', 'POST'])
# def crud_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         cruds = Intro.objects.all()
#         serializer = CrudSerializer(cruds, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CrudSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# def crud_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         crud = Intro.objects.get(pk=pk)
#     except Intro.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = CrudSerializer(crud)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = CrudSerializer(crud, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         crud.delete()
#         return HttpResponse(status=204)        