# Generated by Django 2.2.3 on 2019-08-06 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(default='', max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassifiedRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classified_region', models.CharField(default='', max_length=5)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classified_regions', to='region.Region')),
            ],
        ),
    ]
