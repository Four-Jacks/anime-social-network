# Generated by Django 2.2.7 on 2019-11-14 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_auto_20191113_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.CharField(choices=[('SPRING', 'Spring'), ('UNKNOWN', 'Unknown'), ('WINTER', 'Winter'), ('SUMMER', 'Summer'), ('FALL', 'Fall')], default='UNKNOWN', max_length=6),
        ),
    ]