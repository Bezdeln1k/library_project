import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from catalog.models import Book

class Command(BaseCommand):
    help = 'Импорт книг из XML-файла'

    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str, help='Путь к XML-файлу')

    def handle(self, *args, **kwargs):
        xml_file = kwargs['xml_file']
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for record in root.findall('record'):
            title = author = publication_year = isbn = ''
            inventory_numbers = []

            for field in record.findall('field'):
                if field.get('tag') == '200':
                    title = field.find('./subfield[@code="A"]').text
                    author = field.find('./subfield[@code="F"]').text if field.find('./subfield[@code="F"]') else ''

                elif field.get('tag') == '210':
                    publication_year = field.find('./subfield[@code="D"]').text if field.find('./subfield[@code="D"]') else ''

                elif field.get('tag') == '10':
                    isbn = field.find('./subfield[@code="A"]').text if field.find('./subfield[@code="A"]') else ''

                elif field.get('tag') == '910':
                    inventory_number = field.find('./subfield[@code="B"]').text if field.find('./subfield[@code="B"]') else ''
                    if inventory_number:
                        inventory_numbers.append(inventory_number)

            if not inventory_numbers:
                inventory_numbers = ['-']

            for inventory_number in inventory_numbers:
                Book.objects.create(
                    title=title,
                    author=author,
                    publication_year=publication_year,
                    isbn=isbn,
                    inventory_number=inventory_number
                )

        self.stdout.write(self.style.SUCCESS('Каталог книг успешно обновлен'))