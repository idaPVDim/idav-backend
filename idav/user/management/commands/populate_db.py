from django.core.management.base import BaseCommand
from user.models import (
    CustomUser, ProfilCommercant, TypeEquipement,
    Equipement
)
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Création des types d'équipement
        type_panneau, created = TypeEquipement.objects.get_or_create(
            nom='Panneau Solaire',
            defaults={'description': 'Panneau photovoltaïque',
                      }
        )
        type_batterie, created = TypeEquipement.objects.get_or_create(
            nom='Batterie',
            defaults={'description': 'Batterie de stockage d\'énergie'}
        )
        type_onduleur, created = TypeEquipement.objects.get_or_create(
            nom='Onduleur',
            defaults={'description': 'Convertisseur DC-AC'}
        )

        self.stdout.write(self.style.SUCCESS('Types d\'équipement créés.'))

        # Création d'un profil commerçant
        commercant_user, created = CustomUser.objects.get_or_create(
            email='commercant@example.com',
            defaults={
                'role': 'commercant',
                'is_staff': True,
                'is_active': True,
            }
        )
        commercant_user.set_password('password')  # Définir un mot de passe
        commercant_user.save()

        profil_commercant, created = ProfilCommercant.objects.get_or_create(
            user=commercant_user,
            nom_boutique='Boutique Solaire',
            adresse_boutique='123 Rue du Soleil'
        )

        self.stdout.write(self.style.SUCCESS('Profil commerçant créé.'))

        # Création d'équipements
        equipement1, created = Equipement.objects.get_or_create(
            commercant=profil_commercant,
            type_equipement=type_panneau,
            nom='Panneau Solaire XYZ 300W',
            defaults={
                'description': 'Panneau solaire polycristallin 300W',
                'prix': 150.00,
                'stock': 50,
                'caracteristiques': {'puissance': 300, 'tension': 24, 'courant': 8.5}
            }
        )

        equipement2, created = Equipement.objects.get_or_create(
            commercant=profil_commercant,
            type_equipement=type_batterie,
            nom='Batterie 12V 100Ah',
            defaults={
                'description': 'Batterie AGM 12V 100Ah',
                'prix': 200.00,
                'stock': 30,
                'caracteristiques': {'tension': 12, 'capacite': 100, 'type': 'AGM'}
            }
        )

        self.stdout.write(self.style.SUCCESS('Équipements créés.'))

        # Ajouter d'autres données ici
        self.stdout.write(self.style.SUCCESS('Database population complete.'))
