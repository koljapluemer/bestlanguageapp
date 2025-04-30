from django.core.exceptions import ObjectDoesNotExist
from app.entity.tool import Tool

def get_tool_by_id(tool_id: int) -> Tool:
    """
    Get a tool by ID.
    
    Args:
        tool_id: ID of the tool to get
    
    Returns:
        Tool object
    
    Raises:
        ObjectDoesNotExist: If the tool doesn't exist
    """
    try:
        return Tool.objects.get(id=tool_id)
    except Tool.DoesNotExist:
        raise ObjectDoesNotExist(f"Tool with id {tool_id} does not exist")
