from django.db import models


class BaseTimeStamp(models.Model):
    """
    Assignee : 훈희
    created_at, updated_at(DateTimeField) deleted_at 필드를
    사용하는 모델을 위한 기본 모델입니다.
    abstract = True 설정을 해서 실제로는 물리적 테이블이 생성않고 이것을 이용한 자식 클래스에서 속성 함수들을 사용할 수 있게 구성.
    """

    created_at = models.DateTimeField("작성시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정시간", auto_now=True)
    deleted_at = models.DateTimeField("삭제시간", default=None, null=True, blank=True)

    class Meta:
        abstract = True
