# Generated by Django 4.0.6 on 2022-07-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_grupo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
