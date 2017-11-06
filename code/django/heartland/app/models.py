# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
	class Meta:
		verbose_name_plural = "Categories"
		name = models.CharField("name", max_length=100)
		def __str__(self):
			return self.name

			class Metric(models.Model):
				name = models.CharField("name", max_length=100)
				category = models.ForeignKey(
					Category,
					on_delete=models.CASCADE,
					)
				def __str__(self):
					return self.name + " - " + self.category.name

					class Game(models.Model):
						name = models.CharField("name", max_length=100)
						team = models.CharField("team", max_length=100)
						category = models.ForeignKey(
							Category,
							on_delete=models.CASCADE,
							)
						def __str__(self):
							return self.name + " - " + self.team + " - " + self.category.name

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

							class Score(models.Model):
								def __str__(self):
									return self.game.name + " - " + self.judge.username + " - " + self.metric.name + ": " + str(self.value)
									game = models.ForeignKey(
										Game,
										on_delete=models.CASCADE,
										)
									metric = models.ForeignKey(
										Metric,
										on_delete=models.CASCADE,
										)
									judge = models.ForeignKey(
										User,
										on_delete=models.CASCADE,
										)
									value = models.IntegerField()