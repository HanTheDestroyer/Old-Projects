# Sandpile_Simulation
Shows the results of Sandpile Simulations with and without Numba

Related Numberphile video: https://www.youtube.com/watch?v=1MtEUErz7Gg

Simulation has to iterate over a grid of size AxB. And it has to run until each cell of the mentioned grid has less than four pieces of sand.
With Python, it becomes very slow even with smaller grid sizes. Numba's jit acceleration can be used here for immense speed gains.

For a grid of 200x200, with center cell having 5000 pieces of sand, simulation takes following times.

Without Numba: 72.46 seconds

With Numba+jit: 00.64 seconds

This means that bigger grids are out of question. A grid of 640x640 with 10 million sand in the middle takes around half an hour to one hour with Numba's Jit.
But the results can be presented in an artsy way.

![sandpile](https://github.com/HanTheDestroyer/Sandpile_Simulation/assets/123021973/c27729f7-c242-46e6-bbf3-7fd4ac5bab4d)

Run sandpile.py for the regular version. Or,

Run numba_sandpile.py for numba version then use numba_sandpile_pygame to show the results on the screen.
