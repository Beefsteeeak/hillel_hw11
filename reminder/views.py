import datetime as datetime1

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ReminderForm
from .tasks import send_email as celery_send_email


def reminder(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            datetime = form.cleaned_data['datetime'] - datetime1.timedelta(hours=3)
            celery_send_email.apply_async(('reminder', text, email), eta=datetime)
            messages.add_message(request, messages.SUCCESS, 'Done')
            return redirect('reminder:reminder')
    else:
        form = ReminderForm()
    return render(
        request,
        'reminder/reminder.html',
        context={
            'form': form,
        }
    )
