# The Earth-Moon Lagrange Point _L_<sub>1</sub>
The Lagrange point between the Earth and Moon is the point where the inward attraction of the Earth and outward pull of the Moon are such that these forces provide the exact amount of centripetal force required for a satellite to orbit them with the same period as the moon. 

## The Theory
It is assumed that the orbits are circular; and the mass of the Earth (_M_) is much larger than that of the Moon (_m_) or satellite (_m<sub>s</sub>_) such that $(M >> m, M >> m_s)$.

If we have the force of gravity from the Earth as:

```math
F_{G_{E}} = \frac{GMm_s}{r^2} 
```
and the force of gravity from the moon as:

```math
F_{G_{m}} = \frac{Gmm_s}{(R-r)^2} 
```
then combining both forces gives 

```math
F_{G_{E}} - F_{G_{m}} = F_{net} ,
```
where $F_{net}$ is the centripetal acceleration of the satellite. Thus, this then becomes:

```math
\frac{GMm_s}{r^2} - \frac{Gmm_s}{(R-r)^2} = m_s\omega^2r
```
```math
\frac{GM}{r^2} - \frac{Gm}{(R-r)^2} = \omega^2r
```
## The Secant Method
To solve for the distance _r_ from the Earth to _L_<sub>1</sub>, the secant method was used. 

```math
x_3 = x_2 - f(x_2)\frac{x_2 - x_1}{f(x_2) - f(x_1)}
```
This yielded a result of **_r_ = 3.260 $\times$ 10<sup>8</sup>m**, to 4 significant figures. 

## Gravitational Field Strength
A plot of the gravitational field strength along a straight line stretching from the surface of the Earth to the moon is as below: 
<p align="center">
  <img width="460" height="300" src="https://github.com/amlh22/python-practice/assets/101705746/fa1c168a-a8f2-48f2-9fda-2512c02e1c70">
</p>

|               | Earth         | Moon |
| ------------- | :-------------: | :-----: |
| Gravitational field strength at surface  | 9.82ms<sup>-2</sup>  | 1.62ms<sup>-2</sup> |
