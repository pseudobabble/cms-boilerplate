# Generated by Django 3.1.1 on 2020-09-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200929_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='soundbite',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='soundbite',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
