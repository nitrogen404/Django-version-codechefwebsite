# Generated by Django 3.2 on 2021-04-26 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codechef_management_app', '0006_alter_user_role_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='event_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='codechef_management_app.events'),
        ),
    ]
