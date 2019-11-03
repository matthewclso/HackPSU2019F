# Generated by Django 2.2.6 on 2019-11-03 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0003_auto_20191103_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helprequest',
            name='item',
            field=models.CharField(choices=[('s', 'Shelter'), ('f', 'Food'), ('w', 'Water'), ('t', 'Toiletries'), ('c', 'Clothes')], max_length=1),
        ),
        migrations.CreateModel(
            name='AskerReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('flag', models.BooleanField(default=False)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]