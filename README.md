# Ball-Simulation
The application allows the user to place different kinds of objects (called simultons), which behave/display differently, into a simulation and watch them interact.

Important: To run either the regular or helper simulation, you must run the script named script.py which creates the view and controller by importing their modules (and controller imports model).

- The Mobile_Simulton base class stores the angle (in radians) and speed (in pixels/update) of every mobile object in the simulation (and inherits the information controlled by the Simulton class). It includes methods to query and update this information.
- The Prey base class is an ancestor of every class that produces "edible" objects; it contains only code to call __init__ for Mobile_Simultons (it base class).
- The Ball and Floater classes represent balls (traveling in straight lines) and floaters (travelling more eratically) that traverse the simulation canvas. They are both subclasses (and thus instances) of Prey so they can be "eaten" by Black_Holes, Pulsators, Hunters,
- The Black_Hole class represents a stationary object that eats (removes from the simulation) any Prey object whose center becomes contained its perimeter.
- The Pulsator class represents a special kind of Black_Hole: one that gets bigger (as it eats Prey) and smaller (as it starves); if it gets too small (starves for too long) it dies: removes itself from the simulation.
- The Hunter class represents a special kind of Pulsator: one that is mobile (hence its two base classes), and moves towards the closest Prey that it can see (there are limits to its vision)

Different Type of Buttons:
Ball button: Click anywhere on the canvas, multiple times, to place balls
Start button: Start the simulation. Balls move in a straight line and bounce off walls. Can click on the canvas to add more balls
Stop button: Stop the simulation
Start button: Restart it from where it was stopped
Step button: Run the simulation for one cycle. Each click advances one cycle
Remove button: Any object clicked on will be removed from the simulation; this feature works whether the simulation is running or not, but is easiest to use if the simulation is stopped
Reset button: Reset the simulation. It is stopped with all simultons removed.

Different Types of Objects:
Floater button: Place floaters on the canvas. Each moves differently than a ball, while still bouncing off walls
Black_Hole button: Place a black hole on the canvas. It eats any prey simulton whose center enters its perimeter
Pulsator button: Place a pulsator on the canvas. When it eats a simulton it grows; if it doesn't eat any simultons in 30 cycles, it shrinks and ultimately it can remove itself from the simulation if its size shrinks to 0
Hunter button: Place a hunter on the canvas. It pursues prey (within its range of vision) and grows and shrinks like a pulsator