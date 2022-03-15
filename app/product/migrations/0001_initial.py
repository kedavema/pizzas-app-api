# Generated by Django 2.1.15 on 2022-03-14 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_pizzaabstract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('pizzaabstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PizzaAbstract')),
            ],
            bases=('core.pizzaabstract',),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('pizzaabstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PizzaAbstract')),
                ('category', models.ManyToManyField(to='product.Category')),
            ],
            bases=('core.pizzaabstract',),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('pizzaabstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PizzaAbstract')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('is_active', models.BooleanField(default=True)),
                ('ingredients', models.ManyToManyField(to='product.Ingredient')),
            ],
            bases=('core.pizzaabstract',),
        ),
    ]
