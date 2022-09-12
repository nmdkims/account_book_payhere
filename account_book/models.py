from django.db import models

from config.models import BaseTimeStamp as BaseTimeStampModel
from user.models import User as UserModel

"""Create your models here."""


class AccountBook(BaseTimeStampModel):
    """
    Assignee : 훈희
    사업장 별 가계부를 만들 수 있는 가계부 모델입니다.
    """

    user = models.ForeignKey(to=UserModel, verbose_name="사용자", on_delete=models.CASCADE, related_name="account_book")
    book_name = models.CharField("가계부 제목", max_length=20)
    balance = models.IntegerField("가계부 시작 금액", default=0)
    is_deleted = models.BooleanField("삭제 여부", default=False)

    def __str__(self):
        return f"id : {self.id} / {self.book_name}의 가계부"


class AccountBookCategory(BaseTimeStampModel):
    """
    Assignee : 훈희
    사업장 별 가계부를 만들 수 있는 가계부 카테고리 모델입니다.
    """

    category_name = models.CharField("카테고리 명", max_length=20)
    description = models.CharField("카테고리 설명", max_length=100)

    def __str__(self):
        return f"id : {self.id} / {self.category_name}"


class AccountBookRecord(BaseTimeStampModel):
    """
    Assignee : 훈희
    가계부별 수입 or 지출 기록을 남길 수 있는 모델입니다.
    수입은 양수 지출을 음수를 받습니다.
    """

    account_book = models.ForeignKey(
        to=AccountBook, verbose_name="가계부", on_delete=models.CASCADE, related_name="account_book_record"
    )
    account_book_category = models.ForeignKey(
        to=AccountBookCategory,
        verbose_name="가계부 카테고리",
        on_delete=models.CASCADE,
        related_name="account_book_record_category",
    )
    date = models.DateField("날짜")
    price = models.IntegerField("금액")
    memo = models.CharField("메모", max_length=100)
    is_deleted = models.BooleanField("삭제 여부", default=False)

    def __str__(self):
        return f"id : {self.id} / {self.price} : {self.memo}"
