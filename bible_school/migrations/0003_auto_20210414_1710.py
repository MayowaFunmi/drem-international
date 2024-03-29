# Generated by Django 3.1.5 on 2021-04-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bible_school', '0002_auto_20210414_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=('Male', 'Male'), max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('In A Relationship', 'In A Relationship'), ('Widow', 'Widow'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Remarried', 'Remarried')], default=('Single', 'Single'), max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(choices=[('Pastor', 'Pastor'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Mr', 'Mr'), ('Chief', 'Chief')], default=('Pastor', 'Pastor'), max_length=20),
        ),
    ]
