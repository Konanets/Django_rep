from django.core.management import BaseCommand
from django.db import connection, OperationalError
from django.db.backends.base.base import BaseDatabaseWrapper

import time

connection: BaseDatabaseWrapper = connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_con = False

        while not db_con:
            try:
                connection.ensure_connection()
                db_con = True
            except OperationalError:
                self.stdout.write('Db Error')
                time.sleep(1)
