from django import forms
from . import models
from django.contrib.auth.models import User

class GameForm(forms.Form):
    game_name = forms.CharField(label='Game Name', max_length=100)
    team_name = forms.CharField(label='Team Name', max_length=100)
    category = forms.ModelChoiceField(queryset=models.Category.objects.all(), label='Category', to_field_name="name")


    SCORE_CHOICES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10)
        )

    class ScoreForm(forms.Form):
      game = forms.ModelChoiceField(queryset=models.Game.objects.all(), label='Game', to_field_name="id")
      metric = forms.ModelChoiceField(queryset=models.Metric.objects.all(), label='Metric', to_field_name="id")
      judge = forms.ModelChoiceField(queryset=User.objects.all(), label='User', to_field_name="id")
      value = forms.ChoiceField(choices=SCORE_CHOICES)