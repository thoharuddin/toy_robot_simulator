# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

class TestGame(TransactionCase):
    def setUp(self):
        super(TestGame, self).setUp()
        self.game = self.env["toy.robot.simulator"]

    def test_example_a(self):
        point = [0,0,"NORTH"]
        place = self.game.create({"point_x": point[0], "point_y": point[1],"facing": point[2]})
        place.place_point()
        place.move()
        self.assertEqual(place.report, "0, 1, NORTH")

    def test_example_a(self):
        point = [0,0,"NORTH"]
        place = self.game.create({"point_x": point[0], "point_y": point[1],"facing": point[2]})
        place.place_point()
        place.left()
        self.assertEqual(place.report, "0, 0, WEST")
    
    def test_example_a(self):
        point = [1,2,"EAST"]
        place = self.game.create({"point_x": point[0], "point_y": point[1],"facing": point[2]})
        place.place_point()
        place.move()
        place.move()
        place.left()
        place.move()
        self.assertEqual(place.report, "3, 3, NORTH")