# Generated by Django 4.2.6 on 2023-10-24 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', through='main.Membership', to=settings.AUTH_USER_MODEL, verbose_name='Members'),
        ),
        migrations.AddField(
            model_name='team',
            name='parent_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='main.team'),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='grader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_task', to='main.task'),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submitting_team', to='main.team'),
        ),
        migrations.AddField(
            model_name='task',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_course', to='main.course'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_level', to='main.team'),
        ),
        migrations.AddField(
            model_name='membership',
            name='Team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_of_team', to='main.team'),
        ),
        migrations.AddField(
            model_name='membership',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_course', to='main.course'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_host', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_team', to='main.team'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_course', to='main.course'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='students', through='main.Enrollment', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
        migrations.AddField(
            model_name='course',
            name='tas',
            field=models.ManyToManyField(related_name='tas', through='main.Assistance', to=settings.AUTH_USER_MODEL, verbose_name='Teaching Assistants'),
        ),
        migrations.AddField(
            model_name='assistance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assisting_course', to='main.course'),
        ),
        migrations.AddField(
            model_name='assistance',
            name='ta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assisting_student', to=settings.AUTH_USER_MODEL),
        ),
    ]
