# Generated by Django 3.0.5 on 2020-05-29 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('catalog', '0009_auto_20200529_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoa'),
        ),
    ]
