from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Batiment, Zone, Usage, ConstructionElement


class BatimentSurface(APIView):
    def get(self, request, id):
        batiment = Batiment.objects.get(id=id)
        zones = Zone.objects.filter(id__in=batiment.zoneIds)
        total_surface = sum(zone.surface for zone in zones)
        return Response({'id': batiment.id, 'surface': total_surface})

class BatimentUsage(APIView):
    def get(self, request, id):
        try:
            batiment = Batiment.objects.get(id=id)
            zones = Zone.objects.filter(id__in=batiment.zoneIds)
            if zones:
                largest_zone = max(zones, key=lambda zone: zone.surface)
                usage_id = largest_zone.usage
                usage = Usage.objects.get(id=usage_id)
                return Response({'label': usage.label})
            else:
                return Response({'error': 'No zones found for this building'}, status=404)
        except Batiment.DoesNotExist:
            return Response({'error': 'Building not found'}, status=404)
        except Usage.DoesNotExist:
            return Response({'error': 'Usage not found'}, status=404)


class ImpactCarbone(APIView):
    def get(self, request, id):
        impact_batiment = self.impact_total(id)
        return Response({'impact batiment': impact_batiment})

    def impact_total(self, batiment_id):
        # Batiment.json
        batiment = Batiment.objects.get(id=batiment_id)
        periodeDeReference = batiment.periodeDeReference

        # liste de Zone des ids du batiment
        zones = Zone.objects.filter(id__in=batiment.zoneIds)
        impact_zone = []

        for zone in zones:
            # Récupérer les éléments de construction de la zone
            elements_construction = zone.constructionElements

            # Calculer l'impact carbone pour chaque élément
            for element in elements_construction:
                element_id = element['id']
                quantite = element['quantite']
                construction_element = ConstructionElement.objects.get(id=element_id)

                # Obtenir les impact unitaire pour toutes les phases
                impact_unitaire_production = construction_element.impactUnitaireRechauffementClimatique['production']
                impact_unitaire_construction = construction_element.impactUnitaireRechauffementClimatique['construction']
                impact_unitaire_exploitation = construction_element.impactUnitaireRechauffementClimatique['exploitation']
                rp = max(1, periodeDeReference / construction_element.dureeVieTypique)

                impact_exploitation = ((rp * impact_unitaire_exploitation +
                                        (rp - 1) * (impact_unitaire_construction + impact_unitaire_production
                                                    + impact_unitaire_exploitation))
                                       * quantite)

                fin_de_vie = construction_element.impactUnitaireRechauffementClimatique['finDeVie']
                impact_zone.append(
                    impact_unitaire_production + impact_exploitation + impact_unitaire_construction + fin_de_vie)

        return sum(impact_zone)
