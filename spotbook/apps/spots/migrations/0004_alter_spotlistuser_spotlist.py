# Generated by Django 4.1.1 on 2024-03-18 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0003_alter_spotlistitem_user_spotlistuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotlistuser',
            name='spotlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spots.spotlist'),
        ),
    ]
