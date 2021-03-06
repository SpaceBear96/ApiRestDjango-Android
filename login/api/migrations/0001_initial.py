# Generated by Django 2.0 on 2018-11-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=250)),
                ('imagen', models.FileField(max_length=250, null=True, upload_to='storage/images/')),
                ('tipo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
