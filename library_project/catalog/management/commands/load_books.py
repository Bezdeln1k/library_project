import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from catalog.models import Book

class Command(BaseCommand):
    help = 'Load books from an XML file'

    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str, help='The XML file to load books from')

    def handle(self, *args, **options):
        xml_file = options['xml_file']
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for record in root.findall('.//record[@format="IRBIS"]'):
            title = None
            author = None
            publication_year = None

            for field in record.findall('field'):
                if field.get('tag') == '200':
                    for subfield in field.findall('subfield'):
                        if subfield.get('code') == 'A':
                            title = subfield.text
                        elif subfield.get('code') == 'F':
                            author = subfield.text
                elif field.get('tag') == '210':
                    for subfield in field.findall('subfield'):
                        if subfield.get('code') == 'D':
                            publication_year = subfield.text

            if title and author and publication_year:
                Book.objects.create(
                    title=title,
                    author=author,
                    publication_year=publication_year,
                    is_available=True
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {title} by {author}'))

        self.stdout.write(self.style.SUCCESS('Finished loading books'))
