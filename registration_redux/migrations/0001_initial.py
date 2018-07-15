# Generated by Django 2.0.1 on 2018-03-09 07:49

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
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
                ('activated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'registration_redux profile',
                'verbose_name_plural': 'registration_redux profiles',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, upload_to='profile_image')),
                ('socio_auth_avatar', models.URLField(blank=True, default='https://www.gravatar.com/avatar/4309fdf1236a9cf2cd87f90a87cee8a9?d=mm&s=256', max_length=400)),
                ('user_type', models.CharField(choices=[('STUDENT', 'Student'), ('TEACHER', 'Teacher')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupervisedRegistrationProfile',
            fields=[
                ('registrationprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration_redux.RegistrationProfile')),
            ],
            bases=('registration_redux.registrationprofile',),
        ),
        migrations.AddField(
            model_name='registrationprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]