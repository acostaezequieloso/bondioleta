# Generated by Django 4.2.4 on 2023-09-10 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_options_and_more'),
        ('empleado', '0002_empleado_delete_prueba'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-nombre', 'apellido'], 'verbose_name': 'Mi empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('nombre', 'departamento')},
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades de empleado',
                'ordering': ['habilidad'],
                'unique_together': {('habilidad',)},
            },
        ),
    ]