from django.core.management.base import BaseCommand
from myapp.models import Vertex, Edge

class Command(BaseCommand):
    help = 'Clear the Vertex and Edge tables'

    def handle(self, *args, **kwargs):
        Vertex.objects.all().delete()
        Edge.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared the database.'))
