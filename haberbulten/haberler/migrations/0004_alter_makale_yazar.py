# Generated by Django 4.0.6 on 2022-07-13 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0003_gazeteci_alter_makale_yazar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makale',
            name='yazar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='makaleler', to='haberler.gazeteci'),
        ),
    ]
