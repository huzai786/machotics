# Generated by Django 4.0.4 on 2022-05-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluetec', '0016_alter_ourteamintro_options_homepagefront_top_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerIntro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Career Intro Section (Career PAGE)',
                'verbose_name_plural': 'Career Intro Section (Career PAGE)',
            },
        ),
    ]