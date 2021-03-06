# Generated by Django 3.2.5 on 2021-10-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_auto_20211013_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterModelOptions(
            name='adress',
            options={'verbose_name_plural': 'Address Entries'},
        ),
        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='book_outlet.Country'),
        ),
    ]
