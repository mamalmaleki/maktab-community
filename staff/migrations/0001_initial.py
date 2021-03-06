# Generated by Django 3.0.3 on 2020-03-05 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('code', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('code', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('courses', models.ManyToManyField(blank=True, related_name='students', to='departments.SelectedCourse', verbose_name='courses')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstructorWorkDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(None, '(Unknown)'), (0, 'Saturday'), (1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Instructor', verbose_name='instructor')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Term', verbose_name='term')),
            ],
            options={
                'verbose_name': 'Instructor Work Day',
                'verbose_name_plural': 'Instructor Work Days',
            },
        ),
        migrations.CreateModel(
            name='InstructorExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Course', verbose_name='course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Instructor', verbose_name='instructor')),
            ],
            options={
                'verbose_name': 'Instructor Expertise',
                'verbose_name_plural': 'Instructor Expertise',
            },
        ),
    ]
