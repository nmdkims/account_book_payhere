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
        context 딕셔너리로 로그인된 유저 객체를 보내주어서
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
