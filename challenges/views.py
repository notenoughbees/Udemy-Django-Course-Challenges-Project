from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def monthly_challenge(request, month):
    challenge_text = None
    if(month == "january"):
        challenge_text = "Eat no meat for the entire month!"
    elif(month == "february"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "march"):
        challenge_text = "Learn Django for at least 20 minutes every day!"
    elif(month == "april"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "may"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "june"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "july"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "august"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "september"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "october"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "november"):
        challenge_text = "Walk for at least 20 minutes every day!"
    elif(month == "december"):
        challenge_text = "Walk for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
