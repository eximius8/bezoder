# Generated by Django 3.0.4 on 2020-03-15 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genetics', '0004_auto_20200315_2108'),
        ('person', '0007_remove_genevisitor_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genevisitor',
            name='genomefile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='genevisitor',
            name='genome',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geneuser', to='genetics.UserGenome'),
        ),
    ]