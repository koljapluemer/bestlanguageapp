from typing import Dict, Optional
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from app.entity.tool import Tool

# Use the model's fields to create the type
ToolPatchData = type('ToolPatchData', (), {
    field.name: field.__class__
    for field in Tool._meta.fields
    if field.name not in ['id', 'created_at', 'updated_at']
})

def patch_tool(tool_id: int, data: ToolPatchData) -> Tool:
    """
    Update an existing tool.
    
    Args:
        tool_id: ID of the tool to update
        data: Dictionary containing fields to update (name, description, link)
    
    Returns:
        Updated Tool object
    
    Raises:
        ValidationError: If the data is invalid
        ObjectDoesNotExist: If the tool doesn't exist
    """
    try:
        tool = Tool.objects.get(id=tool_id)
        
        for field, value in data.items():
            if hasattr(tool, field):
                setattr(tool, field, value)
        
        tool.save()
        return tool
    except Tool.DoesNotExist:
        raise ObjectDoesNotExist(f"Tool with id {tool_id} does not exist")
    except Exception as e:
        raise ValidationError(f"Failed to update tool: {str(e)}")
