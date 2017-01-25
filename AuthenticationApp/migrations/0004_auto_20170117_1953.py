# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-17 19:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UniversitiesApp', '0005_auto_20170117_1953'),
        ('CompaniesApp', '0002_remove_company_members'),
        ('AuthenticationApp', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CompaniesApp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('courses', models.ManyToManyField(null=True, to='UniversitiesApp.Course')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(null=True, to='UniversitiesApp.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University'),
        ),
    ]