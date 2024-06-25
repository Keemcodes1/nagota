# Generated by Django 5.0.2 on 2024-03-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kampalaBlog', '0008_logo_menuitem_submenuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Logo',
        ),
        migrations.RemoveField(
            model_name='submenuitem',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='single_product',
            name='product',
        ),
        migrations.RenameField(
            model_name='destination',
            old_name='name',
            new_name='Name',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='SubMenuItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='products',
        ),
        migrations.DeleteModel(
            name='Single_product',
        ),
    ]
