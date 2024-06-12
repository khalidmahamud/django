from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.template.loader import render_to_string

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


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "./challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
