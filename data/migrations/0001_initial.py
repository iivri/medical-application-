# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_date_and_time', models.DateTimeField(blank=True, null=True, verbose_name='visitation date and time')),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(default='', max_length=80, verbose_name='Name of disease')),
                ('description', models.TextField(default='', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('NIS', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=80, null=True)),
                ('last_name', models.CharField(max_length=80, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('The patient is', 'I am'), ('M', 'Male'), ('F', 'Female')], default='The patient is', max_length=2)),
                ('born', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(default='', max_length=80, verbose_name='Name of symptom')),
                ('description', models.TextField(default='', max_length=1000)),
                ('patient', models.ManyToManyField(through='data.Consultation', to='data.Identity')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(default='', max_length=80, verbose_name='Name of treatment')),
                ('description', models.TextField(default='', max_length=5000)),
                ('disease', models.ManyToManyField(through='data.Consultation', to='data.Disease')),
            ],
        ),
        migrations.AddField(
            model_name='disease',
            name='symptom',
            field=models.ManyToManyField(to='data.Symptom'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='patient_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Symptom'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='patient_disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Disease'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='patient_identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Identity'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='patient_treatment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Treatment'),
        ),
    ]
