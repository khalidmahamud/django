from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def monthly_challenge(request, month):
    challenge = None
    if month == 'january':
        challenge = "Eat no vegetables for the entire month!"
    elif month == 'february':
        challenge = "Walk for at least 20 minutes every day!"
    elif month == 'march':
        challenge = "Read one book this month!"
    elif month == 'april':
        challenge = "Learn a new skill!"
    elif month == 'may':
        challenge = "Exercise for at least 30 minutes every day!"
    elif month == 'june':
        challenge = "Drink 8 glasses of water every day!"
    elif month == 'july':
        challenge = "Meditate for 10 minutes every day!"
    elif month == 'august':
        challenge = "Write in a journal every day!"
    elif month == 'september':
        challenge = "Cook a new recipe every week!"
    elif month == 'october':
        challenge = "Limit screen time to 2 hours a day!"
    elif month == 'november':
        challenge = "Practice gratitude every day!"
    elif month == 'december':
        challenge = "Volunteer for a good cause!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge)
