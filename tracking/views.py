from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

import pdb

from .models import Tickets, Comments
from .forms import TicketForm, CommentForm
# Create your views here.

def ticket_index(request):
    tickets_list = Tickets.objects.all()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_title = form.cleaned_data['ticket_title']
            ticket_description = form.cleaned_data['ticket_description']
            ticket = Tickets(ticket_title=ticket_title, ticket_description = ticket_description, ticket_time_stamp=timezone.now())
            ticket.save()
            helper_info = "Your ticket is submitted"
            form = TicketForm()
        return render(request, 'ticket_index.html', { 'form': form, 'tickets_list':tickets_list, 'helper_info': helper_info} )
    else:
        form = TicketForm()

    helper_info = " "
    return render(request, 'ticket_index.html', { 'form': form, 'tickets_list':tickets_list, 'helper_info': helper_info} )

def ticket_show(request, ticket_id):
    ticket = Tickets.objects.get(pk=ticket_id)
    comments = ticket.comments_set.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            ticket_comment = comment_form.cleaned_data['ticket_comment']
            ticket.comments_set.create(ticket_comment=ticket_comment)
            comment_form = CommentForm()
            return render(request, 'ticket_show.html',{ 'ticket':ticket ,'comment_form':comment_form , 'comments': comments })
    else:
        comment_form = CommentForm()
    return render(request, 'ticket_show.html',{ 'ticket':ticket, 'comment_form':comment_form })
