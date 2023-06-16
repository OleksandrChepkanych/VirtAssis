# Generated by Django 4.2.2 on 2023-06-15 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "app",
                    models.CharField(
                        db_index=True, max_length=20, verbose_name="Application"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=15, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "Application",
                "verbose_name_plural": "Applications",
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("birthdate", models.DateTimeField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=6
                    ),
                ),
                (
                    "address",
                    models.TextField(blank=True, null=True, verbose_name="Address"),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="photos/%Y/%m/%d/"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=55, unique=True, verbose_name="URL"),
                ),
                (
                    "time_create",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "time_update",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
                "ordering": ["first_name", "last_name", "time_create"],
            },
        ),
        migrations.CreateModel(
            name="DataType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data_type",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=10,
                        null=True,
                        verbose_name="Type",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone", models.CharField(max_length=20)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="phones",
                        to="contacts.contact",
                    ),
                ),
                (
                    "field_type",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contacts.datatype",
                        verbose_name="Type",
                    ),
                ),
            ],
            options={
                "ordering": ["phone"],
            },
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=30)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emails",
                        to="contacts.contact",
                    ),
                ),
                (
                    "field_type",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contacts.datatype",
                        verbose_name="Type",
                    ),
                ),
            ],
            options={
                "ordering": ["email"],
            },
        ),
    ]
