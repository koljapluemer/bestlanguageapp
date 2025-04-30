from django.shortcuts import redirect
from django.contrib import messages
from app.interactor.tool.get_tool_by_id import get_tool_by_id

def delete_tool(request, tool_id):
    """
    Delete a tool.
    """
    try:
        tool = get_tool_by_id(tool_id)
        tool_name = tool.name
        tool.delete()
        messages.success(request, f'Tool "{tool_name}" deleted successfully.')
    except Exception as e:
        messages.error(request, str(e))
    
    return redirect('admin:tool:list')
