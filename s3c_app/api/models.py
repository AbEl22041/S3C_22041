from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

class Utilisateur(AbstractBaseUser):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    SPECIALITE_CHOICES = [
        ('DSI', 'DSI'),
        ('RSS', 'RSS'),
        ('CNM', 'CNM'),
    ]
    NIVEAU_ETUDE_CHOICES = [
        ('L2', 'L2'),
        ('L3', 'L3'),
    ]
    session_token = models.CharField(max_length=255, blank=True, null=True)
    niveau_etude = models.CharField(max_length=2, choices=NIVEAU_ETUDE_CHOICES)
    specialite = models.CharField(max_length=3, choices=SPECIALITE_CHOICES)
   
    def __str__(self):
        return self.nom + " " + self.prenom
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Equipe(models.Model):
    nom_equipe = models.CharField(max_length=255)
    lead = models.ForeignKey(Utilisateur, related_name='lead_teams', on_delete=models.CASCADE)
    adjoint = models.ForeignKey(Utilisateur, related_name='adjoint_teams', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_equipe

class MembreEquipe(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    unique_together = [['equipe', 'etudiant']]

    def __str__(self):
        return self.equipe.nom_equipe + ": " + self.etudiant.nom + " " + self.etudiant.prenom

class Defi(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_limite = models.DateField()

    def __str__(self):
        return self.titre

class Soumission(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    defi = models.ForeignKey(Defi, on_delete=models.CASCADE)
    date_soumission = models.DateTimeField()
    fichier_soumis = models.CharField(max_length=255)

    def __str__(self):
        return self.equipe.nom_equipe + " - " + self.defi.titre

class Jury(models.Model):
    membre = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    defi = models.ForeignKey(Defi, on_delete=models.CASCADE)

    def __str__(self):
        return self.membre.nom + " " + self.membre.prenom + " - " + self.defi.titre

class GrilleEvaluation(models.Model):
    defi = models.ForeignKey(Defi, on_delete=models.CASCADE)
    critere = models.CharField(max_length=255)
    coefficient = models.IntegerField()

    def __str__(self):
        return self.defi.titre + ": " + self.critere

class Note(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    defi = models.ForeignKey(Defi, on_delete=models.CASCADE)
    jury = models.ForeignKey(Jury, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.equipe.nom_equipe + " - " + self.defi.titre + " - " + str(self.note)

class Administrateur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)

    def __str__(self):
        return self.nom + " " + self.prenom

class Permission(models.Model):
    admin = models.ForeignKey(Administrateur, on_delete=models.CASCADE)
    module = models.CharField(max_length=255)
    action = models.CharField(max_length=50)

    def __str__(self):
        return self.admin.nom + " " + self.admin.prenom + " - " + self.module + ": " + self.action
