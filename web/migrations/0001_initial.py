# Generated by Django 3.1.7 on 2021-02-27 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.item'), verbose_name='Image')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.item')),
            ],
        ),
    ]
