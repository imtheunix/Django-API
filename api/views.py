from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NotaSerializer
from .models import Nota
from . import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notas/',
            'method': 'GET',
            'body': None,
            'description': 'Retorna todas as notas'
        },
        {
            'Endpoint': '/notas/id',
            'method': 'GET',
            'body': None,
            'description': 'Retorna uma nota em especifico'
        },
        {
            'Endpoint': '/notas/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Cria uma nova nota'
        },
        {
            'Endpoint': '/notas/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Altera uma nota'
        },
        {
            'Endpoint': '/notas/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deleta uma nota'
        }

    ]
    return Response(routes)


@api_view(['GET'])
def getNotas(request):
    notas = Nota.objects.all()
    serializer = NotaSerializer(notas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNota(request, pk):
    nota = Nota.objects.get(id=pk)
    serializer = NotaSerializer(nota, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNota(request):
    data = request.data

    nota = Nota.objects.create(
        body=data['body']
    )
    serializer = NotaSerializer(nota, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNota(request, pk):
    data = request.data

    nota = Nota.objects.get(id=pk)
    serializer = NotaSerializer(nota, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deletarNota(request, pk):
    nota = Nota.objects.get(id=pk)
    nota.delete()

    return Response("Nota deletada.")
