# Generated by Django 3.0.8 on 2020-08-19 21:59

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0003_auto_20200819_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exhibitionindex',
            options={'verbose_name': 'exhibitions'},
        ),
        migrations.AddField(
            model_name='exhibition',
            name='flyer_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='page_stream',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='page_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='strapline',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exhibitionindex',
            name='blurb',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exhibitionindex',
            name='page_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ExhibitionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_images', to='home.Exhibition')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
