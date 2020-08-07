# Generated by Django 2.2.2 on 2020-08-07 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_remove_questions_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('response', models.TextField(max_length=64)),
                ('user_name', models.TextField(max_length=64)),
                ('survey_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='survey.SurveyQuestions', verbose_name='Survey')),
            ],
            options={
                'db_table': 'responses',
            },
        ),
    ]
