# Generated by Django 5.0.2 on 2024-03-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kampalaBlog', '0009_message_delete_about_remove_comment_blog_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender_name',
            new_name='author',
        ),
        migrations.AddField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
