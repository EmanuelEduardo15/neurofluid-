import numpy as np
from scipy.integrate import solve_ivp

class NeurofluidSimulator:
    def __init__(self, mu=0.3, D=1e-3, v=0.5):
        self.params = {
            'viscosidade_cognitiva': mu,
            'difusao': D,
            'velocidade': v
        }
        self.mesh = self._create_mesh()
        
    def _create_mesh(self, n=100):
        return np.linspace(0, 10, n)
    
    def _equation(self, t, rho):
        grad = np.gradient(rho, self.mesh)
        return (self.params['difusao'] * np.gradient(grad, self.mesh) 
                - self.params['viscosidade_cognitiva'] * rho**2
                + self.params['velocidade'] * grad)
    
    def run(self, t_span=(0, 100), dt=0.1):
        self.solution = solve_ivp(
            self._equation, t_span, np.exp(-(self.mesh-5)**2),
            t_eval=np.arange(*t_span, dt),
            method='LSODA'
        )
        return self
    
    def visualize(self):
        from matplotlib import pyplot as plt
        plt.figure(figsize=(10,6))
        plt.plot(self.mesh, self.solution.y[:,-1])
        plt.title(f"Neurofluid Simulation (μ={self.params['viscosidade_cognitiva']})")
        plt.savefig('simulation.png')
        return plt
