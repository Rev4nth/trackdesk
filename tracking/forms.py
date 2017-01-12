from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=40)
    user_role = forms.CharField(max_length=40)

class TicketForm(forms.Form):
    ticket_title = forms.CharField(max_length=90)
    ticket_description =  forms.CharField( widget=forms.Textarea)

class CommentForm(forms.Form):
    ticket_comment =  forms.CharField(widget=forms.Textarea)
