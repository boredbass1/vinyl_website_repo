# Generated by Django 2.2.5 on 2020-03-06 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordName', models.CharField(max_length=865)),
                ('record_cover', stdimage.models.StdImageField(upload_to='images/')),
                ('record_format', models.CharField(choices=[('vinyl', 'Vinyl'), ('cd', 'CD'), ('cassete', 'Cassete')], default='vinyl', max_length=7)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('label', models.CharField(blank=True, max_length=50)),
                ('add_date', models.DateTimeField(verbose_name='record added')),
                ('month_puchased', models.CharField(blank=True, choices=[('0', 'January'), ('1', 'Febuary'), ('2', 'March'), ('3', 'April'), ('4', 'May'), ('5', 'June'), ('6', 'July'), ('7', 'August'), ('8', 'September'), ('9', 'October'), ('10', 'November'), ('11', 'December')], default='', max_length=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avg_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Record')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('userID', 'recordID')},
            },
        ),
    ]
