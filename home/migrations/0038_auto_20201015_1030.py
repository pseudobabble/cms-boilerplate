# Generated by Django 3.1.1 on 2020-10-15 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_custommedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundbiteimage',
            name='soundbite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.custommedia'),
        ),
    ]
