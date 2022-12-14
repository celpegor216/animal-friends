# Generated by Django 3.2.12 on 2022-09-14 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField()),
                ('is_rare', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Decoration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_located', models.BooleanField()),
                ('location', models.IntegerField(blank=True, null=True)),
                ('angle', models.IntegerField(blank=True, null=True)),
                ('decoration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.decoration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cnt', models.IntegerField(default=1)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.color')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
