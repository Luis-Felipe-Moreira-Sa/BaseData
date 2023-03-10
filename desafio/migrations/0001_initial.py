# Generated by Django 4.1.4 on 2023-01-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_codigo', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=20)),
                ('altura', models.IntegerField()),
                ('peso', models.FloatField()),
                ('nascimento', models.DateField()),
                ('bairro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
            ],
        ),
    ]
