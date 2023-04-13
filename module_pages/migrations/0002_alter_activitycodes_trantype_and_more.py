# Generated by Django 4.1.8 on 2023-04-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('MAILSIN', 'MAILSIN'), ('BILLABLE', 'BILLABLE')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('PCT Publication Date', 'PCT Publication Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Registration Date', 'RegistrationDate'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Publication Date', 'PublicationDate'), ('Renewal Date', 'Renewal Date'), ('Document Date', 'Document Date'), ('Priority Date', 'Priority Date'), ('Application Date', 'Application Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='inboxmessage',
            name='status',
            field=models.CharField(blank=True, choices=[('UNREAD', 'UNREAD'), ('READ', 'READ')], default='UNREAD', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ip_matters',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('REGISTERED', 'REGISTERED'), ('TRANSFERRED', 'TRANSFERRED'), ('RENEWAL', 'RENEWAL'), ('ABANDONED', 'ABANDONED'), ('CANCELLED', 'CANCELLED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mailsin',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Email', 'Email'), ('Personal', 'Personal'), ('Mail', 'Mail')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Outgoing', 'Outgoing'), ('Others', 'Others'), ('Incoming', 'Incoming')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Mail', 'Mail'), ('Personal', 'Personal'), ('Court', 'Court'), ('Email', 'Email'), ('IPO', 'IPO')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
    ]
