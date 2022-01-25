# Generated by Django 4.0.1 on 2022-01-24 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rest_Code', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Restorant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_name', models.CharField(max_length=100)),
                ('rest_createDate', models.DateField()),
                ('rest_Phone', models.CharField(max_length=12)),
                ('rest_Code', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_Img', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.category')),
                ('restorant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.restorant', to_field='rest_Code')),
            ],
        ),
        migrations.CreateModel(
            name='Deneme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('restorant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.restorant')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='restorant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.restorant', to_field='rest_Code'),
        ),
    ]
