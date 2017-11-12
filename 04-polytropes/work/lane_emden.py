import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode, odeint

def lane_emden(xi, theta, n):
    """Lane-Emden equation rewritten as a system of first-order ODEs
    theta[0] is theta itself theta[1] is its first derivative"""
    return [theta[1], - 2.0 / xi * theta[1] - theta[0]**n]

def lane_emden_jac(xi, theta, n):
    """Jacobian matrix of lane_emden"""
    return [[0.0, - n * theta[0]**(n-1)],
            [1.0, - 2.0 / xi]]

def get_solution(n):
    le = ode(lane_emden, lane_emden_jac)
    le.set_f_params(n)
    le.set_jac_params(n)
    le.set_integrator('lsoda')
    le.set_initial_value([1.0, 0.0], t=1e-6)

    xi = np.linspace(1e-6,10,500)
    theta = np.zeros_like(xi)

    for i in range(1, xi.shape[0]):
        theta[i] = le.integrate(xi[i])[0]
        if theta[i] < 0:
            break

    mask = theta>0

    return xi[mask], theta[mask]

def plot_solution(n, **kwargs):
    xi, theta = get_solution(n)
    plt.plot(xi, theta, **kwargs)
