# Application de Calcul des Taux d'Impact Carbone

Cette application utilise Django REST Framework pour calculer les taux d'impact carbone à partir des données fournies.

## Fonctionnalités

- Calcule les taux d'impact carbone à partir de données textuelles.
- Interface API REST pour intégration facile dans d'autres applications.
  
## Installation et Exécution

### Prérequis

- Python 3.x
- Docker (en option, pour une exécution avec conteneurisation)

### Installation locale

1. Clonez ce dépôt
2.  Lancez l'application avec Docker :
   ```
   docker build -t drfapp .
   docker run -p 8000:8000 drfapp
```
   
L'application sera disponible à l'adresse `http://localhost:8000/`.


## Utilisation

Une fois le serveur lancé, accédez à l'interface API à l'adresse `http://localhost:8000/` pour utiliser les fonctionnalités de calcul des taux d'impact carbone.
Listes des URLs:

1. admin/
2. batiment/<int:id>/surface/ [name='batiment-surface']
3. batiment/<int:id>/usage/ [name='usage']
4. batiment/<int:id>/impact/ [name='impact_batiment']


Pour la documentation j'aurai utiliser un outil tel que Swagger


