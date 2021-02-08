# Generated by Django 3.1.5 on 2021-02-06 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0002_distros_ver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('DateBirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('Write_date', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to='Media/Images/')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Polls.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='category',
        ),
        migrations.DeleteModel(
            name='Distros',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.AddField(
            model_name='books',
            name='Genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Polls.genre'),
        ),
        migrations.AddField(
            model_name='author',
            name='Genre',
            field=models.ManyToManyField(to='Polls.Genre'),
        ),
    ]