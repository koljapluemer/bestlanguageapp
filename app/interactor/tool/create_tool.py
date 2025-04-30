from typing import Dict, Optional
from django.core.exceptions import ValidationError
from app.entity.tool import Tool

# Use the model's fields to create the type
ToolInputData = type('ToolInputData', (), {
    field.name: field.__class__
    for field in Tool._meta.fields
    if field.name not in ['id', 'created_at', 'updated_at']
})

def create_tool(data: ToolInputData) -> Tool:
    """
    Create a new tool.
    
    Args:
        data: Dictionary containing tool data (name, description, link)
    
    Returns:
        Created Tool object
    
    Raises:
        ValidationError: If the data is invalid
    """
    try:
        tool = Tool.objects.create(
            name=data['name'],
            description=data['description'],
            link=data['link']
        )
        return tool
    except Exception as e:
        raise ValidationError(f"Failed to create tool: {str(e)}")
