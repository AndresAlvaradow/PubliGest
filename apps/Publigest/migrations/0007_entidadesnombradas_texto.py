# Generated by Django 3.2.8 on 2023-03-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publigest', '0006_palabrasclaves'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntidadesNombradas_texto',
            fields=[
                ('id_ent_text', models.AutoField(primary_key=True, serialize=False)),
                ('entidad', models.CharField(blank=True, max_length=850, null=True)),
                ('texto', models.CharField(blank=True, max_length=850, null=True)),
            ],
        ),
    ]