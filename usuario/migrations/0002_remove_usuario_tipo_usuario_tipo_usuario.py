# Generated by Django 4.2.6 on 2023-10-31 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoria', '0003_rename_tipo_monitoria_tipo_monitoria_and_more'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tipo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='monitoria.tipousuario'),
        ),
    ]
