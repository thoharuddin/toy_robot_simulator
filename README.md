Odoo - Toy Robot Simulator
=======================
We can play Toy Robot Simulator here (with Odoo 14.0)
![alt text](https://github.com/thoharuddin/toy_robot_simulator/blob/main/game/static/description.png "Description")

Description
========
The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.
There are no other obstructions on the table surface.
The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

Create an application that can read in commands of the following form:
PLACE X,Y,F MOVE LEFT RIGHT REPORT
PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
> The origin (0,0) can be considered to be the SOUTH WEST most corner.

The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.
MOVE will move the toy robot one unit forward in the direction it is currently facing.
LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. REPORT will announce the X,Y and F of the robot.
This can be in any form, but standard output is sufficient.
A robot that is not on the table can choose the ignore the MOVE, LEFT, RIGHT and REPORT commands.
Input can be from a file, or from standard input, as the developer chooses. Provide test data to exercise the application.

Constraint
========

The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any move that would cause the robot to fall must be ignored.
Example Input and Output :

Example a : PLACE 0,0,NORTH - MOVE - REPORT
> Expected output: 0,1,NORTH

Example b PLACE 0,0,NORTH - LEFT - REPORT
> Expected output: 0,0,WEST

Example c PLACE 1,2,EAST - MOVE - MOVE - LEFT - MOVE - REPORT
> Expected output: 3,3,NORTH

Unit Test
========
You can modified test code on game/test/test_game.py, here is an example of the test code :
```python
 def test_example_a(self):
         point = [0,0,"NORTH"]
         place = self.game.create({"point_x": point[0], "point_y": point[1],"facing": point[2]})
         place.place_point()
         place.move()
         self.assertEqual(place.report, "0, 1, NORTH")
```

you can place the robot on point[] variable and move the robot using command move(), left() and right().
to run the test you can just run odoo.bin like this :
```
 python3 ../odoo-bin -c ../odoo-server.conf -d <database> -u <module> --test-enable --stop-after-init
```

when warning/error occurs, the log will show you the details.
```
 2022-08-03 10:17:09,275 4085 ERROR game odoo.addons.game.tests.test_game: ERROR: TestGame.test_example_a
 Traceback (most recent call last):
   File "/opt/odoo/custom/toy/game/tests/test_game.py", line 31, in test_example_a
     place.move()
   File "/opt/odoo/custom/toy/game/models/game.py", line 46, in move
     raise models.ValidationError(
 odoo.exceptions.ValidationError: Your robot will Fall.
```

Credits
=======
Thoharuddin Hanif
