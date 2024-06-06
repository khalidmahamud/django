from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

monthly_challenges = {
    'january': "Eat no vegetables for the entire month!",
    'february': "Walk for at least 20 minutes every day!",
    'march': "Read one book this month!",
    'april': "Learn a new skill!",
    'may': "Exercise for at least 30 minutes every day!",
    'june': "Drink 8 glasses of water every day!",
    'july': "Meditate for 10 minutes every day!",
    'august': "Write in a journal every day!",
    'september': "Cook a new recipe every week!",
    'october': "Limit screen time to 2 hours a day!",
    'november': "Practice gratitude every day!",
    'december': "Volunteer for a good cause!"
}

# Create your views here.


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge)


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]

    return HttpResponseRedirect(f"/challenges/{redirect_month}")
