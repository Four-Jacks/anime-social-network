# Generated by Django 2.2.7 on 2019-11-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0009_auto_20191115_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.CharField(choices=[('WINTER', 'Winter'), ('SUMMER', 'Summer'), ('SPRING', 'Spring'), ('FALL', 'Fall'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=6),
        ),
    ]