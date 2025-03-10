from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.db.models import Q  # Import Q for complex queries

def task_list(request):
    query = request.GET.get('q', '')  # Get search query from the request
    if query:
        tasks = Task.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)  # Search in title and description
        )
    else:
        tasks = Task.objects.all()  # Show all tasks if no search query

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'query': query})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        due_date = request.POST['due_date']
        status = request.POST['status']
        Task.objects.create(title=title, description=description, due_date=due_date, status=status)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.due_date = request.POST['due_date']
        task.status = request.POST['status']
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
