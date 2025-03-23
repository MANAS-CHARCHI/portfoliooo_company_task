# Generated by Django 5.1.6 on 2025-03-23 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Portfolio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='education',
            field=models.ManyToManyField(related_name='portfolios', to='Portfolio.education'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='projects',
            field=models.ManyToManyField(related_name='portfolios', to='Portfolio.projects'),
        ),
        migrations.AlterUniqueTogether(
            name='education',
            unique_together={('user', 'degree')},
        ),
        migrations.AlterUniqueTogether(
            name='projects',
            unique_together={('user', 'title')},
        ),
    ]
