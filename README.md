# ship-sim
shipping sim to play with threading/async and serve as a data source for an api and dashboard

--unimplemented--

components:

Ship
has: home, cargo, cargo_max, speed, destination

Planet
has: ports, cargo, production capacity per product, requests for products

What the sim does:
each time tick:
-ships in transit move
-ships at port unload
-unloaded ships go home
-ships at home orbit (doesn't take up a port)
-ships waiting for port orbit
-planets use resources
-planets that reach 0 for a resource create a request
-planets read the request board and fill a request if they have a free ship and a surplus
-if configured, every few ticks send an http post request with the current state of the planets
