from rest_framework import serializers
from .models import Utilisateur, Equipe, MembreEquipe, Defi, Soumission, Jury, GrilleEvaluation, Note, Administrateur, Permission
from django.contrib.auth.models import User  


def validate_email_domain(value):
    if not value.endswith('@supnum.mr'):
        raise serializers.ValidationError("Email domain must be supnum.mr")
    return value

class UtilisateurSerializer(serializers.ModelSerializer):
    mot_de_passe = serializers.CharField(write_only=True)

    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'email', 'mot_de_passe', 'niveau_etude', 'specialite' ]
         
    email = serializers.EmailField(validators=[validate_email_domain])

    def create(self, validated_data):
        # Create user with email as username
        user = User.objects.create_user(username=validated_data['email'], **validated_data)
        return user
    
class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class MembreEquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembreEquipe
        fields = '__all__'

class DefiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defi
        fields = '__all__'

class SoumissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soumission
        fields = '__all__'

class JurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jury
        fields = '__all__'

class GrilleEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrilleEvaluation
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
