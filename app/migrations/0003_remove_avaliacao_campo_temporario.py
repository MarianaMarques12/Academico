# Generated by Django 5.2.1 on 2025-06-02 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_avaliacao_campo_temporario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='campo_temporario',
        ),
    ]
