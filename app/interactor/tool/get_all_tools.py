from typing import Optional, List
from django.db.models import QuerySet, Q
from app.entity.tool import Tool

def get_all_tools(
    search: Optional[str] = None,
    order_by: Optional[List[str]] = None
) -> QuerySet[Tool]:
    """
    Get all tools with optional filtering and ordering.
    
    Args:
        search: Optional search term to filter tools by name or description
        order_by: Optional list of fields to order by (e.g., ['-created_at', 'name'])
    
    Returns:
        QuerySet of Tool objects
    """
    queryset = Tool.objects.all()
    
    if search:
        queryset = queryset.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )
    
    if order_by:
        queryset = queryset.order_by(*order_by)
    
    return queryset
