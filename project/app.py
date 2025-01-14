# import streamlit as st
# import matplotlib.pyplot as plt
# from fuzzy_system import calculate_heating_with_rule_strength, temperature, occupants, insulation, heating

# # Заголовок додатку
# st.title("Systém regulácie teploty")
# # Функція для створення графіків функцій належності
# def plot_dynamic_membership(temp, occ, ins):
#     fig, axs = plt.subplots(2, 2, figsize=(10, 10))

#     # Температура
#     axs[0, 0].plot(temperature.universe, temperature['very_low'].mf, label='Very Low')
#     axs[0, 0].plot(temperature.universe, temperature['low'].mf, label='Low')
#     axs[0, 0].plot(temperature.universe, temperature['low_medium'].mf, label='Low Medium')
#     axs[0, 0].plot(temperature.universe, temperature['high_medium'].mf, label='High Medium')
#     axs[0, 0].plot(temperature.universe, temperature['high'].mf, label='High')
#     axs[0, 0].plot(temperature.universe, temperature['very_high'].mf, label='Very High')
#     axs[0, 0].axvline(x=temp, color='r', linestyle='--', label=f'Input: {temp}°C')
#     axs[0, 0].set_title("Teplota")
#     axs[0, 0].legend()

#     # Кількість людей
#     axs[0, 1].plot(occupants.universe, occupants['very_few'].mf, label='Very Few')
#     axs[0, 1].plot(occupants.universe, occupants['few'].mf, label='Few')
#     axs[0, 1].plot(occupants.universe, occupants['few_moderate'].mf, label='Few Moderate')
#     axs[0, 1].plot(occupants.universe, occupants['moderate_many'].mf, label='Moderate Many')
#     axs[0, 1].plot(occupants.universe, occupants['many'].mf, label='Many')
#     axs[0, 1].plot(occupants.universe, occupants['very_many'].mf, label='Very Many')
#     axs[0, 1].axvline(x=occ, color='r', linestyle='--', label=f'Input: {occ}')
#     axs[0, 1].set_title("Počet osôb")
#     axs[0, 1].legend()

#     # Ізоляція
#     axs[1, 0].plot(insulation.universe, insulation['very_poor'].mf, label='Very Poor')
#     axs[1, 0].plot(insulation.universe, insulation['poor'].mf, label='Poor')
#     axs[1, 0].plot(insulation.universe, insulation['average_poor'].mf, label='Average Poor')
#     axs[1, 0].plot(insulation.universe, insulation['average_good'].mf, label='Average Good')
#     axs[1, 0].plot(insulation.universe, insulation['good'].mf, label='Good')
#     axs[1, 0].plot(insulation.universe, insulation['excellent'].mf, label='Excellent')
#     axs[1, 0].axvline(x=ins, color='r', linestyle='--', label=f'Input: {ins}')
#     axs[1, 0].set_title("Izolácia")
#     axs[1, 0].legend()
    
#     # Нагрівання
#     axs[1, 1].plot(heating.universe, heating['very_low'].mf, label='Very Low')
#     axs[1, 1].plot(heating.universe, heating['low'].mf, label='Low')
#     axs[1, 1].plot(heating.universe, heating['low_medium'].mf, label='Low Medium')
#     axs[1, 1].plot(heating.universe, heating['medium_high'].mf, label='Medium High')
#     axs[1, 1].plot(heating.universe, heating['high'].mf, label='High')
#     axs[1, 1].plot(heating.universe, heating['very_high'].mf, label='Very High')
#     axs[1, 1].set_title("Vykurovanie")
#     axs[1, 1].legend()

#     plt.tight_layout()
#     return fig

# # Введення параметрів через слайдери
# temp = st.slider("Teplota (°C)", 0, 40, 20)
# occ = st.slider("Počet osôb", 0, 10, 5)
# ins = st.slider("Izolácia", 0, 10, 5)

# # Обчислення інтенсивності опалення
# try:
#     heating_value = calculate_heating_with_rule_strength(temp, occ, ins)
#     st.write(f"Intenzita vykurovania: {heating_value:.5f}%")
#     st.bar_chart([heating_value])  # Графічне представлення результату
# except Exception as e:
#     st.error(f"Chyba: {e}")

# # Відображення графіків функцій належності
# st.write("### Funkcie príslušnosti premenných")
# fig = plot_dynamic_membership(temp, occ, ins)
# st.pyplot(fig)
import streamlit as st
import matplotlib.pyplot as plt
from fuzzy_system import calculate_heating_with_rule_strength, rules, temperature, occupants, insulation, heating
import skfuzzy as fuzz
import numpy as np

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
    axs[0, 0].legend(loc='upper right')

    # Кількість людей
    axs[0, 1].plot(occupants.universe, occupants['very_few'].mf, label='Very Few')
    axs[0, 1].plot(occupants.universe, occupants['few'].mf, label='Few')
    axs[0, 1].plot(occupants.universe, occupants['few_moderate'].mf, label='Few Moderate')
    axs[0, 1].plot(occupants.universe, occupants['moderate_many'].mf, label='Moderate Many')
    axs[0, 1].plot(occupants.universe, occupants['many'].mf, label='Many')
    axs[0, 1].plot(occupants.universe, occupants['very_many'].mf, label='Very Many')
    axs[0, 1].axvline(x=occ, color='r', linestyle='--', label=f'Input: {occ}')
    axs[0, 1].set_title("Počet osôb")
    axs[0, 1].legend(loc='upper right')

    # Ізоляція
    axs[1, 0].plot(insulation.universe, insulation['very_poor'].mf, label='Very Poor')
    axs[1, 0].plot(insulation.universe, insulation['poor'].mf, label='Poor')
    axs[1, 0].plot(insulation.universe, insulation['average_poor'].mf, label='Average Poor')
    axs[1, 0].plot(insulation.universe, insulation['average_good'].mf, label='Average Good')
    axs[1, 0].plot(insulation.universe, insulation['good'].mf, label='Good')
    axs[1, 0].plot(insulation.universe, insulation['excellent'].mf, label='Excellent')
    axs[1, 0].axvline(x=ins, color='r', linestyle='--', label=f'Input: {ins}')
    axs[1, 0].set_title("Izolácia")
    axs[1, 0].legend(loc='upper right')
    
    # Нагрівання
    axs[1, 1].plot(heating.universe, heating['very_low'].mf, label='Very Low')
    axs[1, 1].plot(heating.universe, heating['low'].mf, label='Low')
    axs[1, 1].plot(heating.universe, heating['low_medium'].mf, label='Low Medium')
    axs[1, 1].plot(heating.universe, heating['medium_high'].mf, label='Medium High')
    axs[1, 1].plot(heating.universe, heating['high'].mf, label='High')
    axs[1, 1].plot(heating.universe, heating['very_high'].mf, label='Very High')
    axs[1, 1].set_title("Vykurovanie")
    axs[1, 1].legend(loc='upper right')

    plt.tight_layout()
    return fig

# Візуалізація сили правил

def plot_clipped_combined(rules_strengths, result_value):
    """
    Vizualizácia kombinovaného grafu skrátených funkcií príslušnosti.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    combined_mf = np.zeros_like(heating.universe)

    for rule_strength, consequent_label in rules_strengths:
        clipped_mf = np.fmin(rule_strength, heating[consequent_label.split('[')[1][:-1]].mf)
        combined_mf = np.fmax(combined_mf, clipped_mf)
        ax.fill_between(heating.universe, 0, clipped_mf, alpha=0.4, label=f'Clipped MF: {consequent_label.split("[")[1][:-1]}')

    ax.plot(heating.universe, combined_mf, color='black', linestyle='-', linewidth=2, label='Combined MF')
    ax.axvline(result_value, color='red', linestyle='--', linewidth=2, label=f'Result: {result_value:.2f}%')
    ax.set_title("Combined Clipped Membership Functions")
    ax.set_xlabel("Heating")
    ax.set_ylabel("Membership Degree")
    ax.legend(loc='upper right')
    ax.grid(True)

    st.pyplot(fig)

def visualize_rule_strength(temp, occ, ins):
    st.write("## Vizualizácia sily pravidiel")

    active_rules = []

    # Перебір кожного правила
    for idx, rule in enumerate(rules):
        antecedents = list(rule.antecedent_terms)

        # Отримання міток для антецедентів
        try:
            temp_label = str(antecedents[0])  # Додати перевірку на структуру
            occ_label = str(antecedents[1])
            ins_label = str(antecedents[2])
        except AttributeError as e:
            st.warning(f"Rule {idx + 1} antecedent access error: {e}")
            continue

        # Отримання мітки для консеквенту
        try:
            consequent_label = str(rule.consequent[0])
        except AttributeError as e:
            st.warning(f"Rule {idx + 1} consequent access error: {e}")
            continue

        # Розрахунок значень належності
        temp_mf = fuzz.interp_membership(temperature.universe, temperature[temp_label.split('[')[1][:-1]].mf, temp)
        occ_mf = fuzz.interp_membership(occupants.universe, occupants[occ_label.split('[')[1][:-1]].mf, occ)
        ins_mf = fuzz.interp_membership(insulation.universe, insulation[ins_label.split('[')[1][:-1]].mf, ins)

        # Мінімальна сила правила
        rule_strength = min(temp_mf, occ_mf, ins_mf)

        if rule_strength > 0:
            active_rules.append((rule_strength, consequent_label))
            st.write(f"### pravidlo {idx + 1}: {temp_label} & {occ_label} & {ins_label} : ({consequent_label})")
            st.write(f"sila pravidla: {rule_strength:.2f}")

            # Побудова графіків
            fig, axs = plt.subplots(1, 4, figsize=(20, 4))

            # Температура
            axs[0].plot(temperature.universe, temperature[temp_label.split('[')[1][:-1]].mf, label=temp_label)
            axs[0].axvline(temp, color='r', linestyle='--', label=f'vstup: {temp}')
            axs[0].axhline(rule_strength, color='black', linestyle='-', label=f'sila pravidla: {rule_strength:.2f}')
            axs[0].set_title("Teplota")
            axs[0].legend(loc='upper right')

            # Кількість людей
            axs[1].plot(occupants.universe, occupants[occ_label.split('[')[1][:-1]].mf, label=occ_label)
            axs[1].axvline(occ, color='r', linestyle='--', label=f'vstup: {occ}')
            axs[1].axhline(rule_strength, color='black', linestyle='-', label=f'sila pravidla: {rule_strength:.2f}')
            axs[1].set_title("Počet osôb")
            axs[1].legend()

            # Ізоляція
            axs[2].plot(insulation.universe, insulation[ins_label.split('[')[1][:-1]].mf, label=ins_label)
            axs[2].axhline(rule_strength, color='black', linestyle='-', label=f'sila pravidla: {rule_strength:.2f}')
            axs[2].axvline(ins, color='r', linestyle='--', label=f'vstup: {ins}')
            axs[2].set_title("Izolácia")
            axs[2].legend()

            # Heating (вихідна частина правила)
            axs[3].plot(heating.universe, heating[consequent_label.split('[')[1][:-1]].mf, label=consequent_label)
            axs[3].axhline(rule_strength, color='black', linestyle='-', label=f'sila pravidla: {rule_strength:.2f}')
            axs[3].set_title("Vykurovanie")
            axs[3].legend()

            plt.tight_layout()
            st.pyplot(fig)

    # Відображення комбінованого графіка для всіх активних правил
    if active_rules:
        plot_clipped_combined(active_rules, heating_value)

# Введення параметрів через слайдери
temp = st.slider("Teplota (°C)", 0, 40, 20)
occ = st.slider("Počet osôb", 0, 10, 5)
ins = st.slider("Izolácia", 0, 10, 5)

# Обчислення інтенсивності опалення
try:
    heating_value = calculate_heating_with_rule_strength(temp, occ, ins)
    st.write(f"Intenzita vykurovania: {heating_value:.5f}%")
    st.bar_chart([heating_value])  # Графічне представлення результату

    # Відображення сили правил
    visualize_rule_strength(temp, occ, ins)

except Exception as e:
    st.error(f"Chyba: {e}")

# Відображення графіків функцій належності
st.write("### Funkcie príslušnosti premenných")
fig = plot_dynamic_membership(temp, occ, ins)
st.pyplot(fig)
