# Generated by Django 3.1.1 on 2020-10-15 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20201015_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibitionimage',
            name='soundbite',
        ),
    ]
