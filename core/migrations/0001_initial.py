# Generated by Django 4.2 on 2023-04-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('political_party', models.CharField(max_length=50, verbose_name='partido')),
                ('number', models.IntegerField(verbose_name='numero')),
                ('quantity_votes', models.IntegerField(verbose_name='votos totais')),
            ],
        ),
    ]
