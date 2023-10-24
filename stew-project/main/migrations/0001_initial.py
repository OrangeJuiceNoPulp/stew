# Generated by Django 4.2.6 on 2023-10-24 15:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('join_code', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('memo', models.TextField(blank=True, max_length=500)),
                ('meeting_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Meeting Time')),
                ('meeting_end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ends at')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=5000)),
                ('attached', models.FileField(blank=True, null=True, upload_to='main/task_attachments/')),
                ('due_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Due Date')),
                ('assigned_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Assigned')),
                ('isTeamTask', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=5000)),
                ('attached', models.FileField(blank=True, null=True, upload_to='main/task_submissions/')),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Submitted')),
                ('grade', models.FloatField(blank=True, default=100.0, null=True)),
                ('grading_comments', models.TextField(blank=True, max_length=5000)),
                ('grading_attached', models.FileField(blank=True, null=True, upload_to='main/task_grading/')),
                ('grade_visible', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='main.course')),
            ],
        ),
    ]