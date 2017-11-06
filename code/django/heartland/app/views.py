# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django import forms
from .forms import *
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def login_success(request):
    if request.user.groups.filter(name="Registrar").exists():
        # user is an admin
        return redirect("registrar")
    elif request.user.is_superuser:
    	return redirect('/admin/')
    else:
        return redirect("judging")

def register_success(request):
	return TemplateResponse(request, 'register_success.html')

def registrar(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	    # create a form instance and populate it with data from the request:
	    form = GameForm(request.POST)
	    # check whether it's valid:
	    if form.is_valid():
	        # process the data in form.cleaned_data as required
	        # ...
	        # redirect to a new URL:
	        game = Game()
	        game.name = form.cleaned_data['game_name']
	        game.team = form.cleaned_data['team_name']
	        game.category = form.cleaned_data['category']
	        game.save()
	        return HttpResponseRedirect('/register_success/')

	# if a GET (or any other method) we'll create a blank form
	else:
	    form = GameForm()

	return render(request, 'registrar.html', {'form': form})

def judging(request):
    scoredgames = []
    for score in Score.objects.all().filter(judge = request.user):
        scoredgames.append(score.game.id)
    return TemplateResponse(request, 'judging.html', {'games_list': Game.objects.all(), 'games_scored': scoredgames})


def judge_game(request):
	if request.method == 'POST':
		#print(request.POST)
		game_id = request.POST['game_name']
		game = Game.objects.get(pk=game_id)
		metrics = list(Metric.objects.all().filter(category = game.category))
		scores = list(Score.objects.all().filter(judge = request.user, game = game))

		forms = []
		for metric in metrics:
			form = ScoreForm({'game' : game, 'metric' : metric, 'judge' : request.user})
			score = Score.objects.filter(judge=request.user, game=game, metric=metric)
			if score:
				if score.first().metric == metric:
					form = ScoreForm({'game' : game, 'metric' : metric, 'judge' : request.user, 'value': score.first().value})
			forms.append(form)
			#print(form)

		return TemplateResponse(request, 'judge_game.html', {'game': game, 'metrics': metrics, 'judge': request.user, 'scores': scores, 'forms': forms})

	else:
		return HttpResponse("Please use a post request instead of: " + request.method)

def store_score(request):
	if request.method == 'POST':
		metrics = request.POST.getlist('metric')
		values = request.POST.getlist('value')
		judge_id = request.POST['judge']
		game_id = request.POST['game']

		#print("Game ID: " + game_id)
		game = Game.objects.get(pk=game_id)
		#print("Game Name: " + game.name)

		#print("Judge ID: " + judge_id)
		judge = User.objects.get(pk=judge_id)
		#print("Judge Name: " + judge.username)

		for idx,metric_id in enumerate(metrics):
			#print("Metric_id: " + metric_id)
			metric = Metric.objects.get(pk=metric_id)
			#print("Metric: " + metric.name)
			score = Score()
			score.game = game
			score.judge = judge
			score.metric = metric
			score.value = values[idx]
			Score.objects.filter(judge=judge, game=game, metric=metric).delete()
			score.save()

		return TemplateResponse(request, 'store_score.html', {'game': game})

	else:
		return HttpResponse("Please use a post request")
