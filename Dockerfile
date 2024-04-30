# Utiliser une image de base Python
FROM python:3.12

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt.txt contenant les dépendances de l'application
COPY requirements.txt .

# Installer les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application Django s'exécute (par défaut : 8000)
EXPOSE 8000

# Commande par défaut pour exécuter l'application Django avec collecte statique des fichiers
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]