# Generated by Django 4.0.6 on 2022-07-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='makale',
            name='aktif',
            field=models.BooleanField(default=True),
        ),
    ]
