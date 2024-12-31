# Generated by Django 5.0.3 on 2024-03-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0003_alter_leaverequest_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='reason',
            field=models.TextField(choices=[('Medical reasons', 'Medical reasons'), ('Vacation/holiday', 'Vacation/holiday'), ('Bereavement/funeral', 'Bereavement/funeral'), ('Maternity/paternity leave', 'Maternity/paternity leave'), ('Relocation/moving', 'Relocation/moving'), ('Wedding/planned event', 'Wedding/planned event'), ('Religious observance', 'Religious observance')], default='Medical reasons', max_length=100),
        ),
    ]
