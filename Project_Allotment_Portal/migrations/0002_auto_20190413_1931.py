# Generated by Django 2.1.7 on 2019-04-13 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project_Allotment_Portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_details',
            name='team_leader',
        ),
        migrations.RemoveField(
            model_name='team_details',
            name='team_member_2',
        ),
        migrations.RemoveField(
            model_name='team_details',
            name='team_member_3',
        ),
        migrations.RemoveField(
            model_name='team_details',
            name='team_member_4',
        ),
        migrations.DeleteModel(
            name='Team_details',
        ),
    ]
