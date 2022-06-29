# Generated by Django 4.0.5 on 2022-06-28 03:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gradebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.PositiveIntegerField(unique=True)),
                ('first_Name', models.CharField(max_length=50)),
                ('last_Name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dateOfBirth', models.DateField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('enrollTime', models.DateTimeField(auto_now_add=True)),
                ('gradeTime', models.DateTimeField(blank=True, null=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook.class')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook.student')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('semester', models.CharField(choices=[('S1', 'S1'), ('S2', 'S2')], default='S1', max_length=2)),
                ('courses', models.ManyToManyField(blank=True, to='gradebook.course')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffID', models.PositiveIntegerField(unique=True)),
                ('first_Name', models.CharField(max_length=50)),
                ('last_Name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dateOfBirth', models.DateField()),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gradebook.course')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gradebook.lecturer'),
        ),
        migrations.AddField(
            model_name='class',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebook.semester'),
        ),
    ]