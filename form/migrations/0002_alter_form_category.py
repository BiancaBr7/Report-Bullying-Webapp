# Generated by Django 4.1.7 on 2024-03-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='category',
            field=models.CharField(choices=[('racial', 'Racial Discrimination'), ('sexism', 'Sexism'), ('lgbtq', 'Lgbtq Discrimination'), ('bullying', 'Bullying')], max_length=100),
        ),
    ]
