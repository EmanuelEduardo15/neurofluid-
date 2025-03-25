import numpy as np
from scipy.integrate import solve_ivp

class CognitiveFlowSimulator:
    """Simulador principal do modelo neurofluid"""
    
    def __init__(self, mu=0.3, D=1e-3, v=0.5):
        self.mu = mu
        self.D = D
        self.v = v
        self.x = np.linspace(0, 10, 100)
        self.rho = np.exp(-(self.x-5)**2)  # Condição inicial
        
    def _equation(self, t, rho):
        """Equação diferencial principal"""
        grad = np.gradient(rho, self.x)
        return self.D * np.gradient(grad, self.x) - self.mu * rho**2 + self.v * grad
        
    def run(self, t_span=(0, 100), dt=0.1):
        """Executa a simulação"""
        sol = solve_ivp(self._equation, t_span, self.rho, 
                       t_eval=np.arange(*t_span, dt),
                       method='LSODA')
        self.results = sol
        return self
    
    def visualize(self):
        """Gera gráficos dos resultados"""
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10,6))
        for t in [0, 50, 100]:
            plt.plot(self.x, self.results.y[:,t], 
                    label=f't={self.results.t[t]:.1f}')
        plt.legend()
        plt.title(f"Simulação Neurofluid (μ={self.mu})")
        plt.savefig('results.png')
        return plt.gcf()
