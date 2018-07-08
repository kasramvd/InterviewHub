# Generated by Django 2.0.5 on 2018-07-08 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_auto_20180708_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryrequest',
            name='candidate',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='calendarapp.CandidateModel'),
        ),
        migrations.AlterField(
            model_name='queryrequest',
            name='interviewer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='calendarapp.InterviewerModel'),
        ),
    ]