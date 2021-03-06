# Generated by Django 4.0.3 on 2022-05-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluetec', '0004_aboutusstarting_companystat_datasecuritysection_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopTeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_pic', models.ImageField(upload_to='')),
                ('member_name', models.CharField(blank=True, max_length=300, null=True)),
                ('member_role', models.CharField(blank=True, max_length=300, null=True)),
                ('gmail', models.CharField(blank=True, max_length=300, null=True)),
                ('facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('twitter', models.CharField(blank=True, max_length=300, null=True)),
                ('linkdin', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='whatmakeusdifferent1',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='whatmakeusdifferent1',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='whatmakeusdifferent1',
            name='linkdin',
        ),
        migrations.RemoveField(
            model_name='whatmakeusdifferent1',
            name='member_name',
        ),
        migrations.RemoveField(
            model_name='whatmakeusdifferent1',
            name='member_pic',
        ),
        migrations.RemoveField(
            model_name='whatmakeusdifferent1',
            name='member_role',
        ),
        migrations.RemoveField(
            model_name='whatmakeusdifferent1',
            name='twitter',
        ),
    ]
