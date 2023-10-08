from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TicketForm, AnswerForm
from .models import Ticket, User, Answer


@login_required(login_url='login')
def tickets(request):
    if not request.user.is_superuser:
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tickets/tickets-all.html', context)


@login_required(login_url='login')
def ticket(request, pk):
    ticketObj = Ticket.objects.get(id=pk)
    return render(request, 'tickets/single-ticket.html', {'ticket': ticketObj})


@login_required(login_url='login')
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
def deleteTicket(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('tickets-all')
    context = {'object': ticket}
    return render(request, 'tickets/delete.html', context)



@login_required(login_url='login')
def createAnswer(request):
    form = AnswerForm()
    if request.method == 'POST':
        print("request  ", request.POST)
        form = AnswerForm(request.POST)
        if form.is_valid():
            print(form)

            ticket = get_object_or_404(Ticket, id=request.POST.get('ticket_id'))
            ticket.status = "Done"
            form.save()
            ticket.save()
            return redirect('tickets-all')

    context = {'form': form}
    print("Context  ", context)
    return render(request, 'tickets/answer.html', context)

# @login_required(login_url='login')
# def updateTicket(request, pk):
#     ticketobj = get_object_or_404(Ticket, id=pk)
#     form = TicketForm(instance=ticketobj)
#
#     if request.method == 'POST':
#         form = TicketForm(request.POST, instance=ticketobj)
#         if form.is_valid():
#             form.save()
#             return redirect('tickets-all')
#     context = {'form': form}
#     return render(request, 'tickets/update.html', context)
