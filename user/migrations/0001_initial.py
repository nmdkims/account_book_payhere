# Generated by Django 4.1.1 on 2022-09-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=20, unique=True, verbose_name="사용자 이메일")),
                ("password", models.CharField(max_length=128, verbose_name="비밀번호")),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="작성시간")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정시간")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]