# Generated by Django 3.2.4 on 2021-07-05 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('percelpicupanddelivery', '0002_auto_20210625_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='PercelPicupIncompleted',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('percelpicupanddelivery.percelpicup',),
        ),
        migrations.AddField(
            model_name='percelpicup',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='percelpicup',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Completed'),
        ),
        migrations.AlterField(
            model_name='perceldelivery',
            name='picup_percel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='percelpicupanddelivery.percelpicupincompleted'),
        ),
    ]
