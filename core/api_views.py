from django.urls.conf import path
from rest_framework.views import APIView
from .serializers import AnswerSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Questions, Answer
from rest_framework.permissions import IsAuthenticated
from A.permissions import IsOwnerOrReadOnly


class QuestionListView(APIView):

    def get(self, request):
        questions = Questions.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)              


class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = QuestionSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST) 


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, pk):
        question = Questions.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        else:         
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)     


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly],

    def delete(self, request, pk):
        question = Questions.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnawerCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = AnswerSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.data, status=status.HTTP_400_BAD_REQUEST)


class AnswerUpdateview(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, pk):
        answer = Answer.objects.get(pk=pk)
        self.check_object_permissions(request, answer)
        srz_data = AnswerSerializer(instance=answer, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        else:         
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)     


class AnswerDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly],

    def delete(self, request, pk):
        answer = Answer.objects.get(pk=pk)
        self.check_object_permissions(request, answer)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)