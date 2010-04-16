from django.views.generic.date_based import archive_today, archive_day
from django.shortcuts import redirect
from secretary.helpers.shortcuts import render_error
from secretary.tasks.models import Task
from secretary.tasks.forms import TaskForm
from datetime import date

def task_archive(request, year, month, day):
    todays_date = date.today()
    try:
        request_date = date(int(year), int(month), int(day))
    except ValueError:
        return render_error(request, {'title': "Uh...", 'message': "That date isn't possible."})

    if request_date == todays_date:
        return redirect('/')
    if request_date > todays_date:
        return render_error(request, {'title': "Slow down!", 'message': "That date is in the future."})
    return archive_day(request,
        queryset=Task.objects.all(),
        year=year,
        month=month,
        day=day,
        date_field='timestamp',
        template_name='archive.html',
        extra_context={'form': TaskForm},
        month_format="%m",
        allow_empty=True,
    )


def tasks(request):
    return archive_today(request,
        queryset=Task.objects.all(),
        date_field='timestamp',
        template_name='archive.html',
        extra_context={'form': TaskForm},
        allow_empty=True,
    )


def submit_task(request):
    f = TaskForm(request.POST)
    new_task = f.save()

    return redirect('/')
