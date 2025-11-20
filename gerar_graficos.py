
import numpy as np
import matplotlib.pyplot as plt

# Definição das Funções
# K(t): Nível de conhecimento em função do tempo t
def K(t):
    return 100 / (1 + np.exp(-0.3 * (t - 10)))

# K'(t): Velocidade do aprendizado (derivada de K(t))
def K_prime(t):
    exp_term = np.exp(-0.3 * (t - 10))
    return (30 * exp_term) / ((1 + exp_term)**2)

# Dados para os Gráficos
# Define um intervalo de tempo de 0 a 40 (semanas ou meses)
t_values = np.linspace(0, 40, 400)
knowledge_values = K(t_values)
learning_rate_values = K_prime(t_values)

# Encontra o ponto de inflexão (máxima velocidade de aprendizado)
inflection_point_t = 10
max_learning_rate = K_prime(inflection_point_t)

# Gráfico 1: Curva de Conhecimento K(t)
plt.figure(figsize=(10, 6))
plt.plot(t_values, knowledge_values, label='Curva de Conhecimento K(t)', color='blue')
plt.axhline(y=100, color='r', linestyle='--', label='Limite (Conhecimento Máximo = 100)')
plt.axvline(x=inflection_point_t, color='g', linestyle='--', label=f'Ponto de Inflexão (t={inflection_point_t})')
plt.title('Curva de Aprendizado Contínuo')
plt.xlabel('Tempo de Estudo (t)')
plt.ylabel('Nível de Conhecimento Adquirido K(t)')
plt.legend()
plt.grid(True)
plt.savefig('curva_conhecimento.png')
print("Gráfico 'curva_conhecimento.png' salvo.")

# Gráfico 2: Velocidade do Aprendizado K'(t)
plt.figure(figsize=(10, 6))
plt.plot(t_values, learning_rate_values, label="Velocidade de Aprendizado K'(t)", color='green')
plt.axvline(x=inflection_point_t, color='purple', linestyle='--', label=f'Velocidade Máxima em t={inflection_point_t}')
plt.title('Velocidade do Aprendizado')
plt.xlabel('Tempo de Estudo (t)')
plt.ylabel("Ritmo de Aprendizado K'(t)")
plt.legend()
plt.grid(True)
plt.savefig('velocidade_aprendizado.png')
print("Gráfico 'velocidade_aprendizado.png' salvo.")
