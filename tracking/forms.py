from django import forms

class TicketForm(forms.Form):
    ticket_title = forms.CharField(max_length=90)
    ticket_description =  forms.CharField( widget=forms.Textarea)

class CommentForm(forms.Form):
    ticket_comment =  forms.CharField(widget=forms.Textarea)
