# Generated by Django 3.2.4 on 2021-07-05 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percels', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PercelComplete',
        ),
        migrations.DeleteModel(
            name='PercelProssesing',
        ),
        migrations.CreateModel(
            name='IncompletePercelPicupManager',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('percels.percel',),
        ),
    ]
