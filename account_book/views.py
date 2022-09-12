from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AccountBook
from .permissions import IsOwner
from .serializers import AccountBooksModelSerializer


# url : GET, POST api/v1/accountbooks
class AccountBooksAPIView(APIView):
    """
    Assignee : 훈희
    permission = 작성자 본인과 관리자가 접근 가능
    Http method = GET, POST
    GET : 가계부 목록 조회
    POST : 가계부 생성
    """

    permission_classes = [IsOwner]

    def get(self, request):
        """
        Assignee : 훈희
        가계부 리스트 정보를 response 하는 메서드입니다.
        로그인한 유저가 생성한 가계부 리스트에서 삭제가 되지 않은 것을 불러오는 것을 기본으로 하여
        쿼리 파라미터로 "request_status" 키의 값이 "delete"가 들어오는 경우 삭제된 데이터를 보여줍니다.
        """

        data_request_status = request.GET.get("request_status", None)
        if data_request_status == "delete":
            account_books = AccountBook.objects.filter(user=request.user, is_deleted=True)

        else:
            account_books = AccountBook.objects.filter(user=request.user, is_deleted=False)
        serializer = AccountBooksModelSerializer(account_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Assignee : 훈희
        가계부 데이터를 생성하는 메서드입니다.
        context 딕셔너리로 로그인된 유저 객체를 보내주어서 유저의 정보를 저장할수 있게합니다.
        {
        "book_title": "10월 가계부","balance": "100000"
        }
        """
        context = {"user": request.user}
        serializer = AccountBooksModelSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# url : GET, PUT, PATCH api/v1/accountbooks/<accountbook_id>
class AccountBooksDetailAPIView(APIView):
    """
    Assignee : 훈희
    permission = 작성자 본인만 가능
    Http method = GET, PUT, PATCH
    GET : 가계부 단일조회
    PUT : 가계부 수정
    PATCH : 가계부 삭제
    """

    permission_classes = [IsOwner]

    def get_object_and_check_permission(self, obj_id):
        """
        Assignee : 훈희
        obj_id : int
        input 인자로 단일 오브젝트를 가져오고, 퍼미션 검사를 하는 메서드입니다.
        DoesNotExist 에러 발생 시 None을 리턴합니다.
        """
        try:
            object = AccountBook.objects.get(id=obj_id)
        except AccountBook.DoesNotExist:
            return

        self.check_object_permissions(self.request, object)
        return object

    def get(self, request, accountbook_id):
        """
        Assignee : 훈희
        obj_id : int
        가계부 단일 조회를 하기 위한 메서드입니다.
        """
        account_book = self.get_object_and_check_permission(accountbook_id)
        if not account_book:
            return Response({"error": "가계부가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        return Response(AccountBooksModelSerializer(account_book).data, status=status.HTTP_200_OK)

    def put(self, request, accountbook_id):
        """
        Assignee : 훈희
        accountbook_id : int
        가계부 단일 객체 수정을 위한 메서드입니다. partial 옵션을 사용해 일부분만 수정이 가능합니다.
        """
        account_book = self.get_object_and_check_permission(accountbook_id)
        if not account_book:
            return Response({"error": "가계부가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        try:
            if request.data["is_deleted"] is not None:
                return Response({"error": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)

        except KeyError:
            pass

        serializer = AccountBooksModelSerializer(account_book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "가계부 수정 성공!!"}, status=status.HTTP_200_OK)

    def patch(self, request, accountbook_id):
        """
        Assignee : 훈희

        accountbook_id : int
        가계부 단일 객체 삭제를 위한 메서드입니다.
        is_deleted 필드의 값을 False에서 True로 변경하는 로직으로 구성됩니다.
        is_deleted가 False or None인 경우 400에러를 리턴합니다.
        """
        account_book = self.get_object_and_check_permission(accountbook_id)
        if not account_book:
            return Response({"error": "가계부가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        try:
            if request.data["is_deleted"] == True:
                account_book.is_deleted = True
                account_book.deleted_at = timezone.now()
                account_book.save()
                return Response({"message": "가계부 삭제 성공!!."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)

        except KeyError:
            return Response({"error": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)
