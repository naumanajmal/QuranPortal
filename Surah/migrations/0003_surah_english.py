# Generated by Django 4.2.2 on 2023-07-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Surah", "0002_ayat_number_surah_number_word_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="surah",
            name="english",
            field=models.TextField(blank=True, null=True),
        ),
    ]