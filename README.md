
# Cathodic Ray Tube simulator

We have developed a pc simulator of how would a cathodic ray tube would work in practice given specific values.
The simulator includes 2 modes (sinusoidal and non-sinusoidal). The way the simulator works is by using the following formulas:

**First formula:**

Charge of the electron = $charge$

mass of the electron = $mass$

$$charge / mass$$

This formula will give us the element load ratio.

**Second formula:**

Voltage = $V$

Width of the plate = $W$

velocity of the laser = $v_x$

Distance between the plates = $d$

$$\theta_y = (VW/v_x^2 *d) (charge/mass)$$

$$\theta_x = (VW/v_x^2 *d) (charge/mass)$$

This formula will give us the $x$ and $y$ angle of the laser that would be the way that the laser would move on the screen.

**To be able to draw the Lissajous shapes, we need to parameterize the formulas resulting in the following:**

**Third formula:**

Frequency 1 = $f_1$

Frequency 2 = $f_2$

Phase = $\delta$


$$y = (W/v_x^2 * d )(charge/mass) (sen(f_1 * t))$$ 


$$x = (W/v_x^2 * d )(charge/mass) (sen((f_2 * t) + \delta))$$


## Spanish explanation video
[video](https://www.youtube.com/watch?v=7MQQK4SGXrw)


## Set up
Download the following dependencies with pip install:
```
pip install tkinter

pip install matplotlib

```

## ScreenShots
![Alt text](/screenshots/simulador.png?raw=true "ScreenShot")





