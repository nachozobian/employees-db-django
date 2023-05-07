# Generated by Django 4.0.5 on 2022-06-22 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_alter_departamento_shor_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[(0, 'CONTADOR'), (2, 'ECONOMISTA'), (1, 'ADMINISTRADOR'), (3, 'OTRO')], max_length=50, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]