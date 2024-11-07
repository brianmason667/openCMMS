import csv
from django.core.management.base import BaseCommand
from frontend.models import Supplier, Part
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import parts from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='The path to the CSV file to import')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']  # Get the filename argument
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):  # Added index for better error reporting
                    # Attempt to parse the date fields; leave them as None if parsing fails
                    last_order_date = parse_date(row['lastordr']) if row['lastordr'] else None
                    lead_time_value = row['lead'] if row['lead'] else None

                    part = Part(
                        part_number=row['partno'],
                        alt_part_number=row['altpartno'],
                        description=row['descrip'],
                        bin_location=row['bin_locat'],
                        location=row['location'],
                        cost=row['cost'],
                        stock=row['stock'] == 'T',
                        manufacturer=row['mfr'],
                        manufacturer_part_number=row['mfrpartno'],
                        vpart_number=row['vpartno'],
                        on_hand=row['onhand'],
                        on_order=row['onorder'],
                        supplier=Supplier.objects.get(id=row['supplierid']) if row['supplierid'] else None,
                        active=row['active'] == 'T',
                        code=row['code'],
                        comment=row['comment'],
                        history=row['history'],
                        part_class=row['class'],
                        last_order=last_order_date,  # Use the parsed date or None
                        lead_time=lead_time_value,  # Leave as None if empty
                        note=row['note'],
                        order_status=row['order_st'],
                        status=row['status'],
                        order_point=row['orderpt'],
                        order_quantity=row['orderqty'],
                        unit_of_measure=row['unitms'],
                    )
                    part.save()

                    self.stdout.write(self.style.SUCCESS(f'Successfully imported part: {row["partno"]}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing part at index {index + 1} (part number {row["partno"]}): {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Finished importing parts'))
