# Ball-Simulation
The application allows the user to place different kinds of objects (called simultons), which behave/display differently, into a simulation and watch them interact.

![image](https://github.com/Philipn03/Ball-Simulation/assets/97057738/4c5efc7b-4c7e-4465-bd11-5b0ee38e7e58)

Different Types of Objects:
- Floater button: Place floaters on the canvas. Each moves differently than a ball, while still bouncing off walls
- Black_Hole button: Place a black hole on the canvas. It eats any prey simulton whose center enters its perimeter
- Pulsator button: Place a pulsator on the canvas. When it eats a simulton it grows; if it doesn't eat any simultons in 30 cycles, it shrinks and ultimately it can remove itself from the simulation if its size shrinks to 0
- Hunter button: Place a hunter on the canvas. It pursues prey (within its range of vision) and grows and shrinks like a pulsator

![image](https://github.com/Philipn03/Ball-Simulation/assets/97057738/cae928dd-ebd5-4115-a7fe-63495f470abf)


Different Type of Buttons:
- Ball button: Click anywhere on the canvas, multiple times, to place balls
- Start button: Start the simulation. Balls move in a straight line and bounce off walls. Can click on the canvas to add more balls
- Stop button: Stop the simulation
- Start button: Restart it from where it was stopped
- Step button: Run the simulation for one cycle. Each click advances one cycle
- Remove button: Any object clicked on will be removed from the simulation; this feature works whether the simulation is running or not, but is easiest to use if the simulation is stopped
- Reset button: Reset the simulation. It is stopped with all simultons removed.


