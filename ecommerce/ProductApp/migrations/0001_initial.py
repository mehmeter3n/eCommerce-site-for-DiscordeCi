# Generated by Django 4.1.3 on 2022-12-04 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategori',
            fields=[
                ('AltKategoriID', models.AutoField(primary_key=True, serialize=False)),
                ('AltKategoriADI', models.CharField(max_length=50)),
                ('AltKategoriTARIH', models.DateTimeField(auto_now_add=True)),
                ('AltKategoriDURUM', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'AltKategori',
                'db_table': 'AltKategori',
            },
        ),
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('FirmaID', models.AutoField(primary_key=True, serialize=False)),
                ('FirmaADI', models.CharField(max_length=50)),
                ('FirmaEMAIL', models.CharField(max_length=50)),
                ('FirmaPASSWD', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Firma',
                'db_table': 'Firma',
            },
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('KategoriID', models.AutoField(primary_key=True, serialize=False)),
                ('KategoriADI', models.CharField(max_length=50)),
                ('KategoriTARIH', models.DateTimeField(auto_now_add=True)),
                ('KategoriDURUM', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Kategori',
                'db_table': 'Kategori',
            },
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('MarkaID', models.AutoField(primary_key=True, serialize=False)),
                ('MarkaADI', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Marka',
                'db_table': 'Marka',
            },
        ),
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('UrunID', models.AutoField(primary_key=True, serialize=False)),
                ('UrunKODU', models.CharField(max_length=50)),
                ('UrunADI', models.CharField(max_length=100)),
                ('UrunFIYAT', models.DecimalField(decimal_places=2, max_digits=15)),
                ('UrunACIKLAMA', models.TextField(max_length=500)),
                ('UrunRENK', models.CharField(max_length=20)),
                ('UrunTARIH', models.DateTimeField(auto_now_add=True)),
                ('UrunDURUM', models.BooleanField(default=False)),
                ('UrunSTOK', models.BigIntegerField()),
                ('AltKategoriID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.altkategori')),
                ('FirmaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.firma')),
                ('KategoriID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.kategori')),
                ('MarkaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.marka')),
            ],
            options={
                'verbose_name': 'Urun',
                'db_table': 'Urun',
            },
        ),
        migrations.CreateModel(
            name='UrunImg',
            fields=[
                ('UrunImgID', models.AutoField(primary_key=True, serialize=False)),
                ('UrunImgUrl', models.CharField(max_length=200)),
                ('UrunID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.urun')),
            ],
            options={
                'verbose_name': 'UrunImg',
                'db_table': 'UrunImg',
            },
        ),
        migrations.AddField(
            model_name='altkategori',
            name='KategoriID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.kategori'),
        ),
    ]
