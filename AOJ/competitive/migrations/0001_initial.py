# Generated by Django 2.0.7 on 2020-11-20 11:05

import competitive.models
from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '__first__'),
        ('problem', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('compile_command', models.CharField(help_text='use @ to represent file_name with extension and # with out extension', max_length=300)),
                ('run_command', models.CharField(help_text='use @ to represent file_name with extension and # with out extension', max_length=300)),
                ('extension', models.CharField(blank=True, max_length=200)),
                ('editor_mode', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RankcacheJury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('punish_time', models.PositiveIntegerField(default=0)),
                ('contest', models.ForeignKey(limit_choices_to={'enable': True}, on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('user', models.ForeignKey(limit_choices_to={'role__short_name': 'contestant'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RankcachePublic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('punish_time', models.PositiveIntegerField(default=0)),
                ('contest', models.ForeignKey(limit_choices_to={'enable': True}, on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('user', models.ForeignKey(limit_choices_to={'role__short_name': 'contestant'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScorecacheJury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.PositiveSmallIntegerField(default=0)),
                ('punish', models.PositiveSmallIntegerField(default=0)),
                ('correct_submit_time', models.DateTimeField(blank=True, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
                ('rank_cache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitive.RankcacheJury')),
            ],
        ),
        migrations.CreateModel(
            name='ScorecachePublic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.PositiveSmallIntegerField(default=0)),
                ('punish', models.PositiveSmallIntegerField(default=0)),
                ('pending', models.PositiveSmallIntegerField(default=0)),
                ('correct_submit_time', models.DateTimeField(blank=True, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
                ('rank_cache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitive.RankcachePublic')),
            ],
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('Correct', 'Correct'), ('Time Limit Exceeded', 'Time Limit Exceeded'), ('Wrong Answer', 'Wrong Answer'), ('Compiler Error', 'Compiler Error'), ('Memory Limit Exceeded', 'Memory Limit Exceeded'), ('Run Time Error', 'Run Time Error'), ('No Output', 'No Output')], max_length=200)),
                ('submit_file', models.FileField(upload_to=competitive.models.submit_file_directory_upload)),
                ('submit_time', models.DateTimeField()),
                ('contest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitive.Language')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestcaseOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_file', models.FileField(upload_to=competitive.models.testcase_output_directory_upload)),
                ('result', models.CharField(choices=[('Correct', 'Correct'), ('Time Limit Exceeded', 'Time Limit Exceeded'), ('Wrong Answer', 'Wrong Answer'), ('Compiler Error', 'Compiler Error'), ('Memory Limit Exceeded', 'Memory Limit Exceeded'), ('Run Time Error', 'Run Time Error'), ('No Output', 'No Output')], max_length=200)),
                ('execution_time', models.DecimalField(decimal_places=8, default=0.0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('memory_usage', models.DecimalField(decimal_places=8, default=0.0, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('submit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitive.Submit')),
                ('test_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.TestCase')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='testcaseoutput',
            unique_together={('test_case', 'output_file')},
        ),
        migrations.AlterUniqueTogether(
            name='scorecachepublic',
            unique_together={('rank_cache', 'problem')},
        ),
        migrations.AlterUniqueTogether(
            name='scorecachejury',
            unique_together={('rank_cache', 'problem')},
        ),
        migrations.AlterUniqueTogether(
            name='rankcachepublic',
            unique_together={('contest', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='rankcachejury',
            unique_together={('contest', 'user')},
        ),
    ]