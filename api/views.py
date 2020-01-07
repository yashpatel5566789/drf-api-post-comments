#from rest_framework import viewsets
from rest_framework import generics, mixins
from .models import Post ,Comment ,PostId , CommentId
from .serializers import PostSerializer, CommentIdSerializer, PostIdSerializer
#from rest_framework import status
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404



# ViewSets define the post behavior.

class PostAllViewSet(APIView):
    permission_classes        = []
    authentication_classes    = []


    def get(self, request, format=None):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)
    

class PostViewSet(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes        = []
    authentication_classes    = []
    serializer_class = PostSerializer
    
    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('a')
        if query is not None:
           qs =qs.filter(query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj=None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(request,*args, **kwargs )
        return super().get(request,*args, **kwargs )

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)

class PostIdViewSet(generics.ListAPIView):
    permission_classes        = []
    authentication_classes    = []
    queryset = Post.objects.all()
    serializer_class = PostIdSerializer
    lookup_field = 'id'

#class CommentIdViewSet(generics.ListAPIView):
#    permission_classes        = []
#    authentication_classes    = []
#    queryset = Comment.objects.all()
#    serializer_class = CommentIdSerializer
#    lookup_field = 'id'



class CommentIdViewSet(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes        = []
    authentication_classes    = []
    serializer_class = CommentIdSerializer
    
    def get_queryset(self):
        qs = Comment.objects.all()
        query = self.request.GET.get('a')
        if query is not None:
           qs =qs.filter(query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj=None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(request,*args, **kwargs )
        return super().get(request,*args, **kwargs )

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)
    #def get_queryset(self):
   #     qs = PostId.objects.all()
    #    query = self.request.GET.get('a')
    #    if query is not None:
    #       qs = qs.filter(query)
    #    return qs

#class PostCreateViewSet(generics.CreateAPIView):
#    permission_classes        = []
#    authentication_classes    = []
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer
    


#class PostDetailViewSet(generics.RetrieveAPIView):
#    permission_classes        = []
#    authentication_classes    = []
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer
#    lookup_field = 'id'




# ViewSets define the comment behavior.
#class CommentViewSet(viewsets.ModelViewSet):
#    queryset = Comment.objects.all()
#    serializer_class = CommentSerializer
#
#@api_view(['GET', 'POST'])
#def post_list(request):
#    if request.method == 'GET':
#        posts = Post.objects.all()
#        serializer = PostSerializer(posts, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = PostSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
