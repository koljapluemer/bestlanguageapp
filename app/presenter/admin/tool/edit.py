from django.shortcuts import render, redirect
from django.contrib import messages
from app.interactor.tool.patch_tool import patch_tool
from app.interactor.tool.get_tool_by_id import get_tool_by_id

def edit_tool(request, tool_id):
    """
    Edit an existing tool.
    """
    if request.method == 'POST':
        try:
            data = {
                'name': request.POST.get('name'),
                'description': request.POST.get('description'),
                'link': request.POST.get('link'),
            }
            tool = patch_tool(tool_id, data)
            messages.success(request, f'Tool "{tool.name}" updated successfully.')
            return redirect('admin:tool:list')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('admin:tool:edit', tool_id=tool_id)
    
    # GET request - show edit form
    try:
        tool = get_tool_by_id(tool_id)
        return render(request, 'admin/tool/edit.html', {'tool': tool})
    except Exception as e:
        messages.error(request, str(e))
        return redirect('admin:tool:list')
