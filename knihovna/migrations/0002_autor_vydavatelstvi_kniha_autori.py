# Generated by Django 4.0.2 on 2022-03-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(error_messages={'blank': 'Jméno autora musí být vyplněno'}, help_text='Zadejte jméno autora', max_length=80, verbose_name='Jméno autora')),
                ('prijmeni', models.CharField(error_messages={'blank': 'Příjmení autora musí být vyplněno'}, help_text='Zadejte příjmení autora', max_length=50, verbose_name='Příjmení autora')),
                ('narozeni', models.DateField(blank=True, verbose_name='Datum narození')),
                ('umrti', models.DateField(blank=True, verbose_name='Datum úmrtí')),
                ('biografie', models.TextField(blank=True, verbose_name='Životopis')),
                ('fotografie', models.ImageField(upload_to='autori', verbose_name='Fotografie')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autoři',
                'ordering': ['prijmeni', 'jmeno'],
            },
        ),
        migrations.CreateModel(
            name='Vydavatelstvi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(error_messages={'blank': 'Název vydavatelství je povinný údaj'}, help_text='Zadejte název vydavatelství', max_length=100, verbose_name='Název vydavatelství')),
                ('adresa', models.CharField(blank=True, max_length=200, verbose_name='Adresa')),
            ],
            options={
                'verbose_name': 'Vydavatelství',
                'verbose_name_plural': 'Vydavatelství',
                'ordering': ['nazev'],
            },
        ),
        migrations.AddField(
            model_name='kniha',
            name='autori',
            field=models.ManyToManyField(to='knihovna.Autor'),
        ),
    ]
