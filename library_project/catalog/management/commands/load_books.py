import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from catalog.models import Book

class Command(BaseCommand):
    help = 'Загрузка книг из XML-файла'

    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str, help='XML-файл, из которого будут загружены книги')

    def handle(self, *args, **kwargs):
        xml_file = kwargs['xml_file']
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        for record in root.findall('record'):
            title = record.find("./field[@tag='200']/subfield[@code='A']").text
            author = record.find("./field[@tag='200']/subfield[@code='F']").text
            publication_year = record.find("./field[@tag='210']/subfield[@code='D']").text
            inventory_number = record.find("./field[@tag='910']/subfield[@code='B']")
            inventory_number = inventory_number.text if inventory_number is not None else "-"
            isbn = record.find("./field[@tag='10']/subfield[@code='A']")
            isbn = isbn.text if isbn is not None else "-"
            
            book, created = Book.objects.get_or_create(
                title=title,
                author=author,
                defaults={'publication_year': publication_year, 'inventory_number': inventory_number, 'isbn': isbn}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Book "{title}" by {author} added.'))
            else:
                self.stdout.write(self.style.WARNING(f'Book "{title}" by {author} already exists.'))

    # def handle(self, *args, **options):
    #     xml_file = options['xml_file']
    #     tree = ET.parse(xml_file)
    #     root = tree.getroot()

    #     for record in root.findall('.//record[@format="IRBIS"]'):
    #         title = None
    #         author = None
    #         publication_year = None

    #         for field in record.findall('field'):
    #             if field.get('tag') == '200':
    #                 for subfield in field.findall('subfield'):
    #                     if subfield.get('code') == 'A':
    #                         title = subfield.text
    #                     elif subfield.get('code') == 'F':
    #                         author = subfield.text
    #             elif field.get('tag') == '210':
    #                 for subfield in field.findall('subfield'):
    #                     if subfield.get('code') == 'D':
    #                         publication_year = subfield.text

    #         if title and author and publication_year:
    #             Book.objects.create(
    #                 title=title,
    #                 author=author,
    #                 publication_year=publication_year,
    #                 is_available=True
    #             )
    #             self.stdout.write(self.style.SUCCESS(f'Successfully added book: {title} by {author}'))

    #     self.stdout.write(self.style.SUCCESS('Finished loading books'))
