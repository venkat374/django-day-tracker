# task/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Task

# Helper function to get days of week for consistent display
def get_days_data():
    return [{'day': choice[1], 'slug': choice[0]} for choice in Task.DAYS_OF_WEEK]

# View for the index page, displaying all days of the week
def landing_page(request):
    days_data = get_days_data()
    return render(request, 'index.html', {'days': days_data})

# View for a day-specific task page
def day_view(request, day):
    day_lower = day.lower()

    valid_days_slugs = [choice[0] for choice in Task.DAYS_OF_WEEK]
    if day_lower not in valid_days_slugs:
        raise Http404(f"'{day}' is not a valid day of the week.")

    if request.method == 'POST':
        # --- Handle adding a new task ---
        if 'task' in request.POST:
            task_text = request.POST['task'].strip()
            if task_text:
                Task.objects.create(day=day_lower, task_text=task_text)
            return redirect('day', day=day_lower)

        # --- Handle toggling task done status (checkbox) ---
        if 'toggle_done' in request.POST and 'task_id' in request.POST:
            try:
                task_id = request.POST['task_id']
                task_to_toggle = get_object_or_404(Task, id=task_id, day=day_lower)
                task_to_toggle.done = (request.POST['toggle_done'] == 'on') # 'on' if checked, else not in POST
                task_to_toggle.save()
            except ValueError:
                # Handle cases where task_id might not be an integer
                pass
            return redirect('day', day=day_lower)

        # --- Handle deleting a task ---
        if 'delete_task_id' in request.POST:
            try:
                task_id = request.POST['delete_task_id']
                task_to_delete = get_object_or_404(Task, id=task_id, day=day_lower)
                task_to_delete.delete()
            except ValueError:
                # Handle cases where task_id might not be an integer
                pass
            return redirect('day', day=day_lower)

    # Handle GET request (displaying tasks for the day)
    tasks = Task.objects.filter(day=day_lower).order_by('created_at')
    context = {
        'day': day.capitalize(),
        'tasks': tasks,
    }
    return render(request, 'day.html', context)