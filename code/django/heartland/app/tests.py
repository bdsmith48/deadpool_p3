# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from app.models import *

# Create your tests here.

class GameTestCase(TestCase):
	#Thomas Shaw
	#This tests registration
	#Games have one function, and that is being stored in the database
	def setUp(self):
		Category.objects.create(name="test_cat")
		Game.objects.create(name="test_game", team="test_team", category=Category.objects.get(name="test_cat"))

		def test_game_init_test(self):
		#Test that values initalize correctly for identification
		game = Game.objects.get(name="test_game")
		self.assertEqual(game.name, "test_game")
		self.assertEqual(game.team, "test_team")
		self.assertEqual(game.category.name, "test_cat")

		def test_save_game(self):
		#Test that games can be saved to the database
		game = Game(name="test_game2", team="test_team2", category=Category.objects.get(name="test_cat"))
		game.save()
		self.assertEqual(game, Game.objects.get(name="test_game2"))
		#This shows we have successfully stored the game in the database and can fetch it

