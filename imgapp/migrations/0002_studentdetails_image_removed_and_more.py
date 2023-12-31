# Generated by Django 4.2.3 on 2023-08-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='image_removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
