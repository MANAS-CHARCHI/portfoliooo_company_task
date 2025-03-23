from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Portfolio, Education, Projects
from .serializers import PortfolioSerializer, EducationSerializer, ProjectsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status


# Create your views here.

class PortfolioView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        if Portfolio.objects.filter(user=user).exists():
            return Response({"error": "Portfolio already exists."}, status=status.HTTP_400_BAD_REQUEST)
        portfolio = Portfolio.objects.create(user=user)
        serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            education_ids = request.data.get('education', [])
            project_ids = request.data.get('projects', [])

            portfolio.education.set(Education.objects.filter(id__in=education_ids))
            portfolio.projects.set(Projects.objects.filter(id__in=project_ids))

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        portfolio = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolio, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        portfolio = get_object_or_404(Portfolio, user=request.user)
        if Portfolio.objects.filter(user=user).exists():
            serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                education_ids = request.data.get('education', [])
                project_ids = request.data.get('projects', [])

                portfolio.education.set(Education.objects.filter(id__in=education_ids))
                portfolio.projects.set(Projects.objects.filter(id__in=project_ids))
                
                return Response(serializer.data)
        else:
            return Response({"error": "Portfolio does not exist."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        portfolio = get_object_or_404(Portfolio, user=request.user)
        portfolio.delete()
        return Response({"message": "Portfolio deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class EducationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                education = serializer.save(user=request.user) 
                portfolio, created = Portfolio.objects.get_or_create(user=request.user)
                portfolio.education.add(education)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        education = Education.objects.filter(user=request.user)
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        education = get_object_or_404(Education, pk=pk, user=request.user)
        serializer = EducationSerializer(education, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        education = get_object_or_404(Education, pk=pk, user=request.user)
        education.delete()
        return Response({"message": "Education deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ProjectsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            try:
                project=serializer.save(user=request.user)
                portfolio, created = Portfolio.objects.get_or_create(user=request.user)
                portfolio.projects.add(project)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        projects = Projects.objects.filter(user=request.user)
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = get_object_or_404(Projects, pk=pk, user=request.user)
        serializer = ProjectsSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project = get_object_or_404(Projects, pk=pk, user=request.user)
        project.delete()
        return Response({"message": "Project deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

