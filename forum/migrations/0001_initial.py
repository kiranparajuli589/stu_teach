# Generated by Django 2.0.1 on 2018-03-10 16:43

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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('votes', models.IntegerField(default=0)),
                ('files', models.FileField(blank=True, upload_to='answer_files')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_set', to=settings.AUTH_USER_MODEL)),
                ('downvoted_by', models.ManyToManyField(related_name='answer_downvoted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('class_avatar', models.ImageField(default='class_image/class_cover.jpg', upload_to='class_image')),
                ('code', models.CharField(blank=True, max_length=12)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_set', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(related_name='class_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('instruction', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('votes', models.IntegerField(default=0)),
                ('files', models.FileField(blank=True, upload_to='question_files')),
                ('class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_set', to='forum.Class')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_set', to=settings.AUTH_USER_MODEL)),
                ('downvoted_by', models.ManyToManyField(related_name='question_downvoted', to=settings.AUTH_USER_MODEL)),
                ('upvoted_by', models.ManyToManyField(related_name='question_upvoted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_set', to='forum.Answer')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_set', to='forum.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvoted_by',
            field=models.ManyToManyField(related_name='answer_upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]
