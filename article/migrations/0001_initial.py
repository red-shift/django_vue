# Generated by Django 3.0.4 on 2020-03-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_heading', models.CharField(max_length=250)),
                ('article_body', models.TextField()),
            ],
        ),
    ]
