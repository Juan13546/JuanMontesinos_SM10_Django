
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default='null', upload_to=''),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=110),
        ),
    ]
