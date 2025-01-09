import streamlit as st
import matplotlib.pyplot as plt
from fuzzy_system import calculate_heating_with_rule_strength, temperature, occupants, insulation, heating
st.set_page_config(page_title="Ваш додаток", page_icon="🔥", layout="centered")
# Заголовок додатку
st.title("Systém regulácie teploty")
# Функція для створення графіків функцій належності
def plot_dynamic_membership(temp, occ, ins):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    # Температура
    axs[0, 0].plot(temperature.universe, temperature['very_low'].mf, label='Very Low')
    axs[0, 0].plot(temperature.universe, temperature['low'].mf, label='Low')
    axs[0, 0].plot(temperature.universe, temperature['low_medium'].mf, label='Low Medium')
    axs[0, 0].plot(temperature.universe, temperature['high_medium'].mf, label='High Medium')
    axs[0, 0].plot(temperature.universe, temperature['high'].mf, label='High')
    axs[0, 0].plot(temperature.universe, temperature['very_high'].mf, label='Very High')
    axs[0, 0].axvline(x=temp, color='r', linestyle='--', label=f'Input: {temp}°C')
    axs[0, 0].set_title("Teplota")
    axs[0, 0].legend()

    # Кількість людей
    axs[0, 1].plot(occupants.universe, occupants['very_few'].mf, label='Very Few')
    axs[0, 1].plot(occupants.universe, occupants['few'].mf, label='Few')
    axs[0, 1].plot(occupants.universe, occupants['few_moderate'].mf, label='Few Moderate')
    axs[0, 1].plot(occupants.universe, occupants['moderate_many'].mf, label='Moderate Many')
    axs[0, 1].plot(occupants.universe, occupants['many'].mf, label='Many')
    axs[0, 1].plot(occupants.universe, occupants['very_many'].mf, label='Very Many')
    axs[0, 1].axvline(x=occ, color='r', linestyle='--', label=f'Input: {occ}')
    axs[0, 1].set_title("Počet osôb")
    axs[0, 1].legend()

    # Ізоляція
    axs[1, 0].plot(insulation.universe, insulation['very_poor'].mf, label='Very Poor')
    axs[1, 0].plot(insulation.universe, insulation['poor'].mf, label='Poor')
    axs[1, 0].plot(insulation.universe, insulation['average_poor'].mf, label='Average Poor')
    axs[1, 0].plot(insulation.universe, insulation['average_good'].mf, label='Average Good')
    axs[1, 0].plot(insulation.universe, insulation['good'].mf, label='Good')
    axs[1, 0].plot(insulation.universe, insulation['excellent'].mf, label='Excellent')
    axs[1, 0].axvline(x=ins, color='r', linestyle='--', label=f'Input: {ins}')
    axs[1, 0].set_title("Izolácia")
    axs[1, 0].legend()
    
    # Нагрівання
    axs[1, 1].plot(heating.universe, heating['very_low'].mf, label='Very Low')
    axs[1, 1].plot(heating.universe, heating['low'].mf, label='Low')
    axs[1, 1].plot(heating.universe, heating['low_medium'].mf, label='Low Medium')
    axs[1, 1].plot(heating.universe, heating['medium_high'].mf, label='Medium High')
    axs[1, 1].plot(heating.universe, heating['high'].mf, label='High')
    axs[1, 1].plot(heating.universe, heating['very_high'].mf, label='Very High')
    axs[1, 1].set_title("Vykurovanie")
    axs[1, 1].legend()

    plt.tight_layout()
    return fig

# Введення параметрів через слайдери
temp = st.slider("Teplota (°C)", 0, 40, 20)
occ = st.slider("Počet osôb", 0, 10, 5)
ins = st.slider("Izolácia", 0, 10, 5)

# Обчислення інтенсивності опалення
try:
    heating_value = calculate_heating_with_rule_strength(temp, occ, ins)
    st.write(f"Intenzita vykurovania: {heating_value:.5f}%")
    st.bar_chart([heating_value])  # Графічне представлення результату
except Exception as e:
    st.error(f"Chyba: {e}")

# Відображення графіків функцій належності
st.write("### Funkcie príslušnosti premenných")
fig = plot_dynamic_membership(temp, occ, ins)
st.pyplot(fig)
