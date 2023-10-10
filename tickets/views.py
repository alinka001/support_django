from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TicketForm, AnswerForm, FeedbackForm
from .models import Ticket, User, Answer, Feedback


@login_required(login_url='login')
def tickets(request):

    userobj = User.objects.get(username=request.user)
    print(request.user)
    if not userobj.is_employee:
        tickets = Ticket.objects.filter(author=request.user)
    else:
        tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tickets/tickets-all.html', context)


@login_required(login_url='login')
def ticket(request, pk):
    ticketObj = Ticket.objects.get(id=pk)
    feedbackobj = Feedback.objects.get(id=pk)
    return render(request, 'tickets/single-ticket.html', {'ticket': ticketObj, 'feedback': feedbackobj})


@login_required(login_url='login')
#@permission_required(['tickets.add_ticket'])
def createTicket(request):
    form = TicketForm()
    if request.method == 'POST':
        print("request  ", request.POST)
        form = TicketForm(request.POST)
        if form.is_valid():
            print('form   ', form)
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return redirect('tickets-all')

    context = {'form': form}
    print("Context  ", context)
    return render(request, 'tickets/new-ticket.html', context)


@login_required(login_url='login')
#@permission_required(['tickets.change_ticket'])
def updateTicket(request, pk):
    ticketobj = Ticket.objects.get(id=pk)
    print("ticket", ticketobj)
    form = TicketForm(instance=ticketobj)
    print("req", request)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticketobj)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('tickets-all')
    context = {'form': form}
    return render(request, 'tickets/update.html', context)


@login_required(login_url='login')
#@permission_required(['tickets.delete_ticket'])
def deleteTicket(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('tickets-all')
    context = {'object': ticket}
    return render(request, 'tickets/delete.html', context)


@login_required(login_url='login')
#@permission_required(['ticket.add_answer'])
def createAnswer(request):
    form = AnswerForm()
    if request.method == 'POST':
        print("request  ", request.POST)
        form = AnswerForm(request.POST)
        if form.is_valid():
            print(form)

            ticket = get_object_or_404(Ticket, id=request.POST.get('ticket_id'))
            ticket.status = "done"
            form.save()
            ticket.save()
            return redirect('tickets-all')

    context = {'form': form}
    print("Context  ", context)
    return render(request, 'tickets/answer.html', context)



#@permission_required(['ticket.add_feedback'])
@login_required(login_url='login')
def create_feedback(request):

    form = FeedbackForm()
    if request.method == 'POST':
        print("request  ", request.POST)
        form = FeedbackForm(request.POST)
        if form.is_valid():

            print(form)
            form.save()
            return redirect('tickets-all')

    context = {'form': form}
    print("Context  ", context)
    return render(request, 'tickets/feedback.html', context)

