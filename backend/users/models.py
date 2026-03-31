from django.db import models# pour créer des modèles de données
from django.contrib.auth.models import AbstractUser# pour créer un modèle d'utilisateur personnalisé

class CustomUser(AbstractUser):# hérite du modèle d'utilisateur de Django
        
    pass
