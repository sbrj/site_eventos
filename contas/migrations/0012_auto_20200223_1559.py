# Generated by Django 3.0.3 on 2020-02-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0011_auto_20200222_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='img_evento'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='img_post'),
        ),
    ]
