# Generated by Django 3.0.4 on 2020-03-14 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trait', '0001_initial'),
        ('person', '0003_auto_20200311_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genevisitor',
            name='height',
        ),
        migrations.AlterField(
            model_name='genevisitor',
            name='onensptrait',
            field=models.ManyToManyField(blank=True, to='trait.OneSNPTrait'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
