# Generated by Django 4.0.4 on 2022-05-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluetec', '0012_alter_companystat_data_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecard',
            name='card_class',
            field=models.CharField(blank=True, choices=[('fa fa-laptop', 'laptop'), ('fa fa-paper-plane-o', 'paper plane'), ('fa fa-line-chart', 'line chart'), ('fa fa-object-group', 'visual box'), ('fa fa-hdd-o', 'hard drive'), ('fa fa-comments-o', 'comment')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ourworkslide',
            name='card_class',
            field=models.CharField(blank=True, choices=[('fa fa-laptop', 'laptop'), ('fa fa-paper-plane-o', 'paper plane'), ('fa fa-line-chart', 'line chart'), ('fa fa-object-group', 'visual box'), ('fa fa-hdd-o', 'hard drive'), ('fa fa-comments-o', 'comment')], max_length=300, null=True),
        ),
    ]
