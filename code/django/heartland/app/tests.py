# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
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


class GameDeletion(TestCase):
	#Michael Sun
	#This tests deletion of a registered team
	#Tests if entry exists after creation, then no longer exists after deletion 
	def setUp(self):
		Category.objects.create(name="category_del")
		Game.objects.create(name="game_del", team="team_del", category=Category.objects.get(name="category_del"))

	def test_game_delete(self):
		# assert True
		game = Game.objects.get(name="game_del")
		self.assertTrue(game is not None)
		# assert True
		Game.objects.get(id=game.id).delete()
		self.assertTrue(not Game.objects.filter(id=game.id).exists())
	
class JudgingTestCase(TestCase):
    #AbdulAziz AlMahfoudh
	#Testing Judging
	#Test whether voting and related information submitted by the judge are consistent
	def setUp(self):
		value_1=3
		Category.objects.create(name="random_category")
		Game.objects.create(name="random_game",team="random_team",category=Category.objects.get(name="random_category"))
		Metric.objects.create(name="random_metric",category=Category.objects.get(name="random_category"))
		User.objects.create_user("random_user","abc@abc.com","123456")
	def test_game_judging(self):
		value_1=3
		game_1=Game.objects.get(name="random_game")
		metric_1=Metric.objects.get(name="random_metric")
		judge_1=User.objects.get(username="random_user")
		Score.objects.create(game=game_1,metric=metric_1,judge=judge_1,value=value_1)
		my_score=Score.objects.get(game=game_1,metric=metric_1,judge=judge_1,value=value_1)

		self.assertEqual(game_1,my_score.game)
		self.assertEqual(metric_1,my_score.metric)
		self.assertEqual(judge_1,my_score.judge)
		self.assertEqual(value_1,my_score.value)
			
class LogInTest(TestCase):
    #Cheng zhou
    #This tests login
    #Tests if putting valid account number and password, it will be logined in successfully
    	def setUp(self):
        	self.credentials = {'username': 'zhchppkdch','password': 'zc123456'}
        	User.objects.create_user(**self.credentials)

    	def test_login(self):
       		# send login data
        	response = self.client.post('', self.credentials, follow=True)
        	# This shows we have successfully login and status will match 200
        	self.assertEqual(response.status_code, 200)

		
class AddJudge(TestCase):
    #Wenlong Gu (Arvin)
    #Test Add judges
    #Test if we can add another judger into the database
    	def setUp(self):
        	value_a=4
        	Category.objects.create(name="puppy")
        	Game.objects.create(name="gameName",team="random_team",category=Category.objects.get(name="puppy"))
        	Metric.objects.create(name="random_metric",category=Category.objects.get(name="puppy"))
        	User.objects.create_user("random_user","abc@abc.com","123456")
   
    	#create a new judge into the database
    	def test_add_judge(self):
        	judge_2=User.objects.get(username="random_user")


#More tests go below here
