# Generated by Django 4.1.4 on 2023-01-02 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'permissions': (('can_add', 'Can Add Question'),)},
        ),
    ]
