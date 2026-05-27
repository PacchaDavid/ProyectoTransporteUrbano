from django.core.management.base import BaseCommand
from django.conf import settings
from azure.cosmos import CosmosClient
from appSITUweb.models import Pasajero, Tarjeta, Bus, Viaje, SimularAccesoPago


MODELS = [
    (Pasajero, 'Pasajero', lambda p: {
        'id': f'pasajero_{p.id}',
        'tipo': 'Pasajero',
        'modelo_id': p.id,
        'cedula': p.cedula,
        'nombre': p.nombre,
        'apellido': p.apellido,
        'email': p.email,
        'imagen_url': p.imagen.url if p.imagen else None,
    }),
    (Tarjeta, 'Tarjeta', lambda t: {
        'id': f'tarjeta_{t.id}',
        'tipo': 'Tarjeta',
        'modelo_id': t.id,
        'codigo': t.codigo,
        'monto': t.monto,
        'pasajero_id': t.idPasajero_id,
        'pasajero_cedula': t.idPasajero.cedula,
    }),
    (Bus, 'Bus', lambda b: {
        'id': f'bus_{b.id}',
        'tipo': 'Bus',
        'modelo_id': b.id,
        'placa': b.placa,
        'cooperativa': b.cooperativa,
        'numero': str(b.numero),
    }),
    (Viaje, 'Viaje', lambda v: {
        'id': f'viaje_{v.id}',
        'tipo': 'Viaje',
        'modelo_id': v.id,
        'pasajero_id': v.pasajero_id,
        'pasajero_cedula': v.pasajero.cedula,
        'bus_id': v.bus_id,
        'bus_placa': v.bus.placa,
        'costo': str(v.costo),
        'cantidad': v.cantidad,
        'fecha_viaje': v.fecha_viaje.isoformat(),
        'efectivo': v.efectivo,
        'tipo_viaje': v.tipo,
    }),
    (SimularAccesoPago, 'SimularAccesoPago', lambda s: {
        'id': f'simularpago_{s.id}',
        'tipo': 'SimularAccesoPago',
        'modelo_id': s.id,
        'numero': s.numero,
        'fecha_viaje': s.fecha_viaje.isoformat(),
        'viaje_id': s.viaje_id,
        'tarjeta_id': s.tarjeta_id,
        'tarjeta_codigo': s.tarjeta.codigo,
    }),
]


class Command(BaseCommand):
    help = 'Backup all models from PostgreSQL to Azure Cosmos DB'

    def handle(self, *args, **options):
        cosmos_uri = settings.COSMOS_URI
        cosmos_key = settings.COSMOS_KEY
        database_name = settings.COSMOS_DATABASE
        container_name = settings.COSMOS_CONTAINER

        if not cosmos_uri or not cosmos_key:
            self.stdout.write(self.style.ERROR(
                'COSMOS_URI and COSMOS_KEY must be set in environment'
            ))
            return

        client = CosmosClient(cosmos_uri, credential=cosmos_key)
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        total_ok = 0
        total_errors = 0

        for queryset, label, serializer in MODELS:
            items = queryset.objects.all()
            count = items.count()
            self.stdout.write(f'[{label}] {count} records found...')

            ok = 0
            errors = 0
            for item in items:
                try:
                    doc = serializer(item)
                    container.upsert_item(doc)
                    ok += 1
                except Exception as e:
                    self.stdout.write(self.style.WARNING(
                        f'  Error backing up {label} id={item.id}: {e}'
                    ))
                    errors += 1

            self.stdout.write(self.style.SUCCESS(
                f'  [{label}] {ok} synced, {errors} errors'
            ))
            total_ok += ok
            total_errors += errors

        self.stdout.write(self.style.SUCCESS(
            f'Backup complete: {total_ok} total synced, {total_errors} total errors'
        ))
