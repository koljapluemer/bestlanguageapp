from django.shortcuts import render
from app.interactor.tool.get_all_tools import get_all_tools

def list_tools(request):
    """
    List all tools.
    """
    tools = get_all_tools()
    return render(request, 'admin/tool/list.html', {'tools': tools})
