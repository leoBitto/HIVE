# Generated by Django 4.1.7 on 2023-09-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_gallery_image_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_image',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
