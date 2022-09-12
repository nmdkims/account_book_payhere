from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import AccountBook, AccountBookRecord


class AccountBooksRecordModelSerializer(ModelSerializer):
    """
    Assignee : 훈희
    참조 및 역참조를 통해 AccountBookRecord 모델 객체들의 금액을 for문을 이용하여
    AccountBookRecord 모델 데이터가 생성된 시점까지의 잔액을 계산
    내부에 정의된 create 메소드 override로 AccountBookRecord 모델 객체 생성
    """

    balance = serializers.SerializerMethodField(required=False, read_only=True)

    def get_balance(self, obj):
        balance = obj.account_book.balance
        for record in obj.account_book.account_book_record.order_by("date", "created_at").filter(is_deleted=False):
            if obj.date >= record.date:
                balance += record.amount
        return balance

    def create(self, validated_data):
        account_book = self.context["account_book"]
        account_book_record = AccountBookRecord(account_book=account_book, **validated_data)
        account_book_record.save()
        return account_book_record

    class Meta:
        model = AccountBookRecord
        fields = ("date", "amount", "memo", "balance", "created_at", "is_deleted")
        read_only_fields = ["is_deleted"]


class AccountBooksModelSerializer(ModelSerializer):
    """
    Assignee : 훈희
    View단에서 AccountBook 모델의 객체가 주어졌을 때,
    역참조를 통해 AccountBookRecord 모델의 쿼리셋을 가져오기
    AccountBookRecord 모델 쿼리셋에서 for문을 이용해
    현재까지의 잔액을 계산하는 로직 구성
    내부에 정의된 create 메소드 override로 로그인된 user로 AccountBook 모델 객체 생성
    """

    account_book_number = serializers.IntegerField(source="id", required=False, read_only=True)
    total_balance = serializers.SerializerMethodField(required=False, read_only=True)
    accountbook_record = serializers.SerializerMethodField(required=False, read_only=True)

    def get_total_balance(self, obj):
        account_book_records = obj.account_book_record.order_by("created_at").filter(is_deleted=False)
        total_balance = obj.balance
        for record in account_book_records:
            total_balance += record.amount
        return total_balance

    def get_accountbook_record(self, obj):
        account_book_records = obj.account_book_record.order_by("date", "created_at").filter(is_deleted=False)
        account_book_records_serializer = AccountBooksRecordModelSerializer(account_book_records, many=True)
        return account_book_records_serializer.data

    def create(self, validated_data):
        user = self.context["user"]
        account_book = AccountBook(user=user, **validated_data)
        account_book.save()
        return account_book

    class Meta:
        model = AccountBook
        fields = (
            "user",
            "book_title",
            "balance",
            "account_book_number",
            "total_balance",
            "is_deleted",
            "accountbook_record",
        )
        read_only_fields = ["user", "is_deleted"]
