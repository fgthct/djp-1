# Generated by Django 4.1.5 on 2023-01-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='accounts/no_image.jpg', upload_to='image_profile'),
        ),
    ]