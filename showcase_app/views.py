from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
import re

@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all().order_by('-created_at')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_project(request):
    data = request.data
    if not data.get('name'):
        return Response({"error": "Project name is required."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ProjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def project_summary(request, id):
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    description = project.description or ""
    techs = project.technologies or ""

    # Simulated AI-like summary
    keywords = re.findall(r'\b[A-Za-z]+\b', description)
    main_topic = ', '.join(keywords[:5]) if keywords else "general software development"

    summary = {
        "summary": f"Based on the description, this project likely focuses on {main_topic}. "
                   f"A generated summary emphasizes its potential impact on user experience using technologies like {techs}."
    }

    return Response(summary)
