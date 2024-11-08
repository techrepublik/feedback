# Generated by Django 4.2.16 on 2024-10-28 01:29

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=10, unique=True)),
                ('question_question', models.CharField(max_length=254)),
                ('question_type', models.CharField(choices=[('General', 'General'), ('Admin', 'Admin'), ('Teaching', 'Teaching'), ('Research', 'Research'), ('Production', 'Support'), ('Production', 'Production')], default='General', max_length=20)),
            ],
            options={
                'ordering': ['question_id'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('client_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.CharField(blank=True, max_length=254, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('client_type', models.CharField(blank=True, choices=[('Faculty', 'Faculty'), ('Staff', 'Staff'), ('Student', 'Student'), ('Alumni', 'Alumni'), ('Parent', 'Parent'), ('Guardian', 'Guardian'), ('Supplier', 'Supplier'), ('Service Provider', 'Service Provider'), ('Visitor', 'Visitor')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=100)),
                ('unit_short_name', models.CharField(blank=True, max_length=100, null=True)),
                ('unit_type', models.CharField(choices=[('Academic', 'Academic'), ('Support', 'Support'), ('Administration', 'Administration'), ('Research', 'Research'), ('Production', 'Production'), ('Others', 'Others')], default='Academic', max_length=50)),
            ],
            options={
                'ordering': ['unit_short_name'],
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=50)),
                ('question_id', models.CharField(max_length=10)),
                ('response', models.IntegerField(blank=True, null=True)),
                ('question_pk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='home.question')),
                ('transaction_pk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='home.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('department_short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='home.unit')),
            ],
            options={
                'ordering': ['department_name'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('user_id', models.CharField(max_length=36, unique=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=50, null=True)),
                ('registered_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qrcodes/')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
