# Generated by Django 5.1 on 2024-09-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0003_alter_messagedata_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagedata',
            name='email_from',
            field=models.CharField(null=True, verbose_name='Отправитель'),
        ),
    ]
