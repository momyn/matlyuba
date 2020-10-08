# Generated by Django 3.1.1 on 2020-10-03 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('menu', models.BooleanField(blank=True, default=False, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategory', to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Lookbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='product/%Y/%m/%d', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'NEW'), ('Sold OUT', 'SOLD OUT'), ('coming soon', 'COMING SOON'), ('Bestseller', 'BESTSELLER')], max_length=25, verbose_name='Статус')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Имя')),
                ('slug', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, upload_to='product/%Y/%m/%d', verbose_name='Первая картинка')),
                ('item_image_2', models.ImageField(upload_to='product/%Y/%m/%d', verbose_name='Вторая картинка')),
                ('item_image_3', models.ImageField(upload_to='product/%Y/%m/%d', verbose_name='Третья картинка')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Описания')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('sku', models.CharField(blank=True, help_text='Если оставить поле пустым, по умолчанию используется ярлык', max_length=255, null=True, verbose_name='Артикул')),
                ('available', models.BooleanField(default=True, verbose_name='Доступный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('uploaded', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Look',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='product/%Y/%m/%d', verbose_name='Картинка')),
                ('slug', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='Ссылка')),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lookbook')),
            ],
        ),
    ]