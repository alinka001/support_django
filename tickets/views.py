from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TicketForm
from .models import Ticket


@login_required(login_url='login')
def tickets(request):
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
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets-all')
    context = {'form': form}
    return render(request, 'tickets/new-ticket.html', context)


@login_required(login_url='login')
def updateTicket(request, pk):
    ticketObj = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticketObj)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticketObj)
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
