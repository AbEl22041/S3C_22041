from rest_framework import viewsets
from .models import (Utilisateur, Equipe, MembreEquipe, Defi, Soumission, Jury, GrilleEvaluation, Note, Administrateur, Permission)
from .serializers import (UtilisateurSerializer, EquipeSerializer, MembreEquipeSerializer, DefiSerializer, SoumissionSerializer, JurySerializer, GrilleEvaluationSerializer, NoteSerializer, AdministrateurSerializer, PermissionSerializer)
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UtilisateurSerializer
from .models import Utilisateur
from .managers import CustomUserManager





class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class MembreEquipeViewSet(viewsets.ModelViewSet):
    queryset = MembreEquipe.objects.all()
    serializer_class = MembreEquipeSerializer

class DefiViewSet(viewsets.ModelViewSet):
    queryset = Defi.objects.all()
    serializer_class = DefiSerializer

class SoumissionViewSet(viewsets.ModelViewSet):
    queryset = Soumission.objects.all()
    serializer_class = SoumissionSerializer

class JuryViewSet(viewsets.ModelViewSet):
    queryset = Jury.objects.all()
    serializer_class = JurySerializer

class GrilleEvaluationViewSet(viewsets.ModelViewSet):
    queryset = GrilleEvaluation.objects.all()
    serializer_class = GrilleEvaluationSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class AdministrateurViewSet(viewsets.ModelViewSet):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer



@api_view(['POST'])
def register(request):
    serializer = UtilisateurSerializer(data=request.data)
    if serializer.is_valid():
        Utilisateur.objects.create_user(**serializer.validated_data)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    if user:
        return Response({"status": "success", "message": "Login successful"})
    else:
        return Response({"status": "error", "message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
