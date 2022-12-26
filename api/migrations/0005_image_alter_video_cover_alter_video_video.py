# Generated by Django 4.1.4 on 2022-12-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_video_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default='Description...', max_length=400)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.ImageField(upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos'),
        ),
    ]