from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('category', models.CharField(choices=[('vitrified','Vitrified Tiles'),('bathroom','Bathroom Tiles'),('sanitaryware','Sanitaryware'),('granite','Granite')], max_length=20)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
