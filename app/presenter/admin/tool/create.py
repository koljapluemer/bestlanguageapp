from django.shortcuts import render, redirect
from app.interactor.tool.create_tool import create_tool

def create_tool(request):
    """
    Create a new tool.
    """
    if request.method == 'POST':
        try:
            create_tool({
                'name': request.POST['name'],
                'description': request.POST['description'],
                'link': request.POST['link']
            })
            return redirect('admin.tool:list')
        except Exception as e:
            return render(request, 'admin/tool/create.html', {
                'error': str(e)
            })
    return render(request, 'admin/tool/create.html') 