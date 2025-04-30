from django.db.models import QuerySet
from app.entity.tool import Tool

def get_all_tools() -> QuerySet[Tool]:
    """
    Get all tools.
    
    Returns:
        QuerySet of Tool objects
    """
    return Tool.objects.all()
