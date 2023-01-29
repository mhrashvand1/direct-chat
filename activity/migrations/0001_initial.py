# Generated by Django 4.1.5 on 2023-01-29 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineStatus',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='online_status', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('status', models.IntegerField(choices=[(0, 'online'), (1, 'offline')], default=1)),
            ],
            options={
                'verbose_name': 'online status',
                'verbose_name_plural': 'online status',
                'db_table': 'OnlineStatus',
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks_from', to=settings.AUTH_USER_MODEL, verbose_name='from user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks_to', to=settings.AUTH_USER_MODEL, verbose_name='to user')),
            ],
            options={
                'verbose_name': 'block',
                'verbose_name_plural': 'blocks',
                'db_table': 'Block',
                'unique_together': {('from_user', 'to_user')},
            },
        ),
    ]