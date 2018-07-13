# Generated by Django 2.0.7 on 2018-07-13 10:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(blank=True, null=True)),
                ('author', models.CharField(blank=True, default='anonymous', max_length=50)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic')),
            ],
        ),
    ]
