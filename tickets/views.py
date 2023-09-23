from django.shortcuts import render
from .models import Ticket


def tickets(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tickets/tickets-all.html', context)

def project(request, pk):
    ticketObj = Ticket.objects.get(id=pk)
    return render(request, 'tickets/ticket-single.html', {'ticket': ticketObj})