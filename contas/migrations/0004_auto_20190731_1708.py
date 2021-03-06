# Generated by Django 2.2.3 on 2019-07-31 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20190731_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('data', models.DateTimeField()),
                ('descricao', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.DeleteModel(
            name='Transacao',
        ),
    ]
