import argparse
from typing import Any

from django.core.management.base import BaseCommand
from django.utils import timezone

from ninjas.models import Ninja


class Command(BaseCommand):
    help = "Mark ninjas as graduated"

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("ninjas", nargs="+", type=int)

    def handle(self, *args: Any, **options: Any) -> None:
        ninjas = Ninja.objects.filter(id__in=options["ninjas"])
        if ninjas.count() != len(options["ninjas"]):
            msg = self.style.WARNING("Some of the ids supplied do not exist")
            self.stdout.write(msg)

        ninjas.update(graduated_at=timezone.now().date())
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully updated {len(options['ninjas'])} ninja(s)"
            )
        )
