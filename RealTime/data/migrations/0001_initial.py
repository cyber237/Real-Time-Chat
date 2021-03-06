# Generated by Django 3.1 on 2020-10-15 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('numOfStud', models.IntegerField()),
                ('timetable', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=10)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.level')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.speciality')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.speciality'),
        ),
        migrations.CreateModel(
            name='courseOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeAllow', models.IntegerField()),
                ('timeLeft', models.IntegerField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.level')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.speciality')),
            ],
        ),
    ]
