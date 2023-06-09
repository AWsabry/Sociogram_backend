# Generated by Django 3.2.3 on 2023-03-29 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('last_name', models.CharField(blank=True, max_length=500, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Organization', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Notification_token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=2500, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Notification Tokens',
            },
        ),
        migrations.CreateModel(
            name='Push_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Notification')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Push Notifications',
            },
        ),
        migrations.CreateModel(
            name='Restaurant_Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=250, unique=True)),
                ('city', models.CharField(blank=True, max_length=500, null=True)),
                ('restaurant_name', models.CharField(blank=True, max_length=500, null=True)),
                ('reason', models.TextField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='Team')),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('Facebook_Link', models.CharField(blank=True, max_length=500, null=True)),
                ('LinkedInLink', models.CharField(blank=True, max_length=500, null=True)),
                ('nu_id', models.CharField(blank=True, max_length=60, null=True)),
                ('school', models.CharField(blank=True, max_length=60, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Team members',
            },
        ),
        migrations.CreateModel(
            name='TopCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Feedback', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='customers')),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('feedback_rate', models.FloatField(blank=True, null=True)),
                ('Facebook_Link', models.CharField(blank=True, max_length=500, null=True)),
                ('LinkedInLink', models.CharField(blank=True, max_length=500, null=True)),
                ('nu_id', models.CharField(blank=True, max_length=60, null=True)),
                ('school', models.CharField(blank=True, max_length=60, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Top Customers',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_delivery', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('nu_id', models.CharField(blank=True, max_length=60, null=True)),
                ('school', models.CharField(blank=True, max_length=60, null=True)),
                ('PhoneNumber', models.CharField(max_length=20, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_operation', models.BooleanField(default=False)),
                ('Wallet', models.FloatField(blank=True, default=0, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=500)),
                ('expires', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
