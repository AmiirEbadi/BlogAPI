from .models import Article
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from serializer.serializers import (
    UserSerializer,
    PostSerializer
)
from permission.permissions import (
    IsOwnerOrAdminOrReadonly,
    IsAuthorOrAdminOrReadonly,
    IsWriterOrAdminOrReadonly
)
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response
from .filters import ProductFilter
from rest_framework import status

class ArticleList(ListAPIView):
    serializer_class = PostSerializer
    queryset = Article.objects.all()
    permission_classes = [IsWriterOrAdminOrReadonly]
    filterset_class = ProductFilter

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            obj = serializer.save(author = request.user)
            return Response({
                    "info" : "Your Post is Created Succesfully"
                },
                status= status.HTTP_201_CREATED
                )
        
        return Response({
                    "info" : "There is Something wrong with your Post" ,
                    "errors" : f"{serializer.errors}"    
                },
                status= status.HTTP_400_BAD_REQUEST
            )

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Article.objects.all()
    permission_classes = [IsAuthorOrAdminOrReadonly]
    