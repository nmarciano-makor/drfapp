import json
from django.core.management.base import BaseCommand
from DRF_App.models import Usage, Zone, ConstructionElement, Batiment


class Command(BaseCommand):
    help = 'Importe les données JSON dans la base de données'

    def handle(self, *args, **options):
        with open('data/usages.json', 'r') as file:
            usages = json.load(file)
            for key, value in usages.items():
                usage = Usage(id=int(key), label=value)
                usage.save()

        # Import des éléments de construction
        with open('data/construction_elements.json', 'r') as file:
            elements = json.load(file)
            for item in elements:
                construction_element = ConstructionElement(
                    id=item['id'],
                    nom=item['nom'],
                    unite=item['unite'],
                    impactUnitaireRechauffementClimatique=item['impactUnitaireRechauffementClimatique'],
                    dureeVieTypique=item['dureeVieTypique']
                )
                construction_element.save()

        # Import des bâtiments
        with open('data/batiments.json', 'r') as file:
            batiments = json.load(file)
            for item in batiments:
                batiment = Batiment(
                    id=item['id'],
                    nom=item['nom'],
                    surface=item['surface'],
                    zoneIds=item['zoneIds'],
                    usage=item['usage'],
                    periodeDeReference=item['periodeDeReference']
                )
                batiment.save()

        # Import des zones
        with open('data/zones.json', 'r') as file:
            zones = json.load(file)
            for item in zones:
                zone = Zone(
                    id=item['id'],
                    nom=item['nom'],
                    surface=item['surface'],
                    usage=item['usage'],
                    constructionElements=item['constructionElements'],
                )
                zone.save()

        self.stdout.write(self.style.SUCCESS('Données importées avec succès !'))
