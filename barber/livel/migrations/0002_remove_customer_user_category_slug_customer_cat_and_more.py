# Generated by Django 4.1.7 on 2023-04-02 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, max_length=260, unique=True, verbose_name='Url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='cat',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='livel.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(default=1, max_length=260, unique=True, verbose_name='Url'),
            preserve_default=False,
        ),
    ]