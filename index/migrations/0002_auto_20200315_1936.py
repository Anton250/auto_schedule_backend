# Generated by Django 2.0.5 on 2020-03-15 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='constraintcollection',
            unique_together={('projector', 'big_blackboard')},
        ),
    ]