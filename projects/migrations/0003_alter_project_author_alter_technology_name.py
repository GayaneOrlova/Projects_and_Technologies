# Generated by Django 4.1.2 on 2023-07-13 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_rename_categories_project_technologies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Technology title'),
        ),
    ]