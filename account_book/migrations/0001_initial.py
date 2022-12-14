# Generated by Django 4.1.1 on 2022-09-12 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountBook",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="작성시간")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정시간")),
                ("deleted_at", models.DateTimeField(blank=True, default=None, null=True, verbose_name="삭제시간")),
                ("book_name", models.CharField(max_length=20, verbose_name="가계부 제목")),
                ("balance", models.IntegerField(default=0, verbose_name="가계부 시작 금액")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="삭제 여부")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_book",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="사용자",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AccountBookCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="작성시간")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정시간")),
                ("deleted_at", models.DateTimeField(blank=True, default=None, null=True, verbose_name="삭제시간")),
                ("category_name", models.CharField(max_length=20, verbose_name="카테고리 명")),
                ("description", models.CharField(max_length=100, verbose_name="카테고리 설명")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AccountBookRecord",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="작성시간")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정시간")),
                ("deleted_at", models.DateTimeField(blank=True, default=None, null=True, verbose_name="삭제시간")),
                ("date", models.DateField(verbose_name="날짜")),
                ("price", models.IntegerField(verbose_name="금액")),
                ("memo", models.CharField(max_length=100, verbose_name="메모")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="삭제 여부")),
                (
                    "account_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_book_record",
                        to="account_book.accountbook",
                        verbose_name="가계부",
                    ),
                ),
                (
                    "account_book_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_book_record_category",
                        to="account_book.accountbookcategory",
                        verbose_name="가계부 카테고리",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
