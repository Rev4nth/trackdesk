from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length = 40)
    user_role = models.CharField(max_length = 40)

class Tickets(models.Model):
    ticket_creator = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    ticket_title = models.CharField(max_length = 90)
    ticket_description = models.TextField()
    ticket_time_stamp = models.DateTimeField()

    def __str__(self):
        return self.ticket_title + " : " + self.ticket_description

class Comments(models.Model):
    ticket_id = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    ticket_comment = models.TextField()
