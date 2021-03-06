# Generated by Django 3.1.1 on 2020-10-10 11:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_wall'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundbiteimage',
            name='blurb',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exhibitionimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_images', to='home.wall'),
        ),
        migrations.AlterField(
            model_name='exhibitionmedia',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_media', to='home.wall'),
        ),
    ]
