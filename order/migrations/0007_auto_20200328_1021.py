# Generated by Django 3.0.3 on 2020-03-28 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0006_auto_20200315_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subs_platters',
            name='type',
            field=models.CharField(choices=[('platters', 'Dinner Platters'), ('sub', 'sub')], default='platters', max_length=64),
        ),
        migrations.CreateModel(
            name='order_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('pizza_topping', models.CharField(max_length=64)),
                ('dinner_platters', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='platters', to='order.subs_platters')),
                ('pasta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasta', to='order.pasta_salads')),
                ('pizza_ord', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_order', to='order.pizza')),
                ('salads', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salads', to='order.pasta_salads')),
                ('subs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='order.subs_platters')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
