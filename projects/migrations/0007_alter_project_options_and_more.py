# Generated by Django 4.2.5 on 2024-01-12 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_options_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Vote_total',
            new_name='vote_total',
        ),
    ]