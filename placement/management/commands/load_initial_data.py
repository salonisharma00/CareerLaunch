import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Load CareerLaunch initial data and create the admin user"

    def handle(self, *args, **options):
        # Load CareerLaunch placement data
        call_command("loaddata", "data.json")

        # Create or update the Render admin user
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if username and password:
            User = get_user_model()

            user, _ = User.objects.get_or_create(
                username=username
            )

            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
            user.set_password(password)
            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Admin user '{username}' created/updated successfully!"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                "CareerLaunch initial data loaded successfully!"
            )
        )