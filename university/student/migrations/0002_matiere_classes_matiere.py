# Generated by Django 4.1.5 on 2023-02-08 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
                ('note_ds', models.FloatField()),
                ('note_ex', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='matiere',
            field=models.ManyToManyField(to='student.matiere'),
        ),
    ]
