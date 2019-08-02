# Generated by Django 2.2.3 on 2019-08-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distillate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('quantity_volume', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('source_from', models.CharField(blank=True, max_length=60)),
                ('strain_type', models.CharField(blank=True, max_length=60)),
                ('date_received', models.DateField(blank=True, null=True)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('purity_source', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('purity_third_party', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('purity_in_house_test', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]