# Generated by Django 4.1.3 on 2023-01-02 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0009_rename_kategoriid_altkategori_kategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnerilenUrunler',
            fields=[
                ('OuID', models.AutoField(primary_key=True, serialize=False)),
                ('UrunDURUM', models.BooleanField(default=True)),
                ('UrunTARIH', models.DateTimeField(auto_now_add=True)),
                ('OnerilenUrun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OnerilenUrun', to='ProductApp.urun')),
            ],
            options={
                'verbose_name': 'OnerilenUrunler',
                'db_table': 'OnerilenUrunler',
            },
        ),
    ]
