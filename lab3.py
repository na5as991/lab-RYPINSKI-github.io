import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
import statsmodels.api as sm

data = load_diabetes()
age, bmi, target = data.data[:, 0], data.data[:, 2], data.target

def group(val): return 'Меньше 100' if val < 100 else '100–200' if val <= 200 else 'Больше 200'
groups = np.array([group(t) for t in target])
colors = {'Меньше 100': 'blue', '100–200': 'orange', 'Больше 200': 'red'}

plt.figure(figsize=(8, 6))
for g in np.unique(groups):
    mask = groups == g
    plt.scatter(age[mask], bmi[mask], label=g, color=colors[g], alpha=0.6)

plt.xlabel('Age (норм.)')
plt.ylabel('BMI')
plt.title('Diabetes: Age vs BMI (по target)')
plt.legend(title='Группа target')
plt.grid(True)
plt.tight_layout()
plt.show()

try:
    co2 = sm.datasets.co2.load_pandas().data['co2'].resample('ME').mean()['1958-01':'1980-12']
    co2.plot(figsize=(10, 4), title='CO2 Concentration (1958–1980)')
    plt.ylabel('CO2 (ppm)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("Ошибка при построении графика 3:", e)