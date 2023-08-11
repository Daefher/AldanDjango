# Generated by Django 4.2.3 on 2023-08-04 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_alter_company_companyid'),
        ('part', '0003_delete_partqty'),
    ]

    operations = [
        migrations.CreateModel(
            name='partQty',
            fields=[
                ('partQtyId', models.AutoField(primary_key=True, serialize=False)),
                ('onHandQty', models.DecimalField(decimal_places=2, max_digits=18)),
                ('canceledBy', models.IntegerField(null=True)),
                ('canceledDateTime', models.DateTimeField(null=True)),
                ('canceled', models.BooleanField(default=False)),
                ('cancelable', models.BooleanField()),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('partId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part.part')),
            ],
        ),
    ]
