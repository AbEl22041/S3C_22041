from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'utilisateurs', views.UtilisateurViewSet)
router.register(r'equipes', views.EquipeViewSet)
router.register(r'membres_equipe', views.MembreEquipeViewSet)
router.register(r'defis', views.DefiViewSet)
router.register(r'soumissions', views.SoumissionViewSet)
router.register(r'jury', views.JuryViewSet)
router.register(r'grille_evaluation', views.GrilleEvaluationViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'administrateurs', views.AdministrateurViewSet)
router.register(r'permissions', views.PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),  
]
