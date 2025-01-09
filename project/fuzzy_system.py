
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Вхідні змінні
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
occupants = ctrl.Antecedent(np.arange(0, 11, 1), 'occupants')
insulation = ctrl.Antecedent(np.arange(0, 11, 1), 'insulation')

# Вихідна змінна
heating = ctrl.Consequent(np.arange(0, 101, 1), 'heating')

# Функції належності
temperature['very_low'] = fuzz.trapmf(temperature.universe, [0, 0, 5, 10])
temperature['low'] = fuzz.trimf(temperature.universe, [5, 10, 15])
temperature['low_medium'] = fuzz.trimf(temperature.universe, [10, 15, 20])
temperature['high_medium'] = fuzz.trimf(temperature.universe, [15, 20, 25])
temperature['high'] = fuzz.trimf(temperature.universe, [20, 30, 40])
temperature['very_high'] = fuzz.trapmf(temperature.universe, [35, 40, 40, 40])

occupants['very_few'] = fuzz.trapmf(occupants.universe, [0, 0, 1, 2])
occupants['few'] = fuzz.trimf(occupants.universe, [1, 3, 5])
occupants['few_moderate'] = fuzz.trimf(occupants.universe, [3, 5, 7])
occupants['moderate_many'] = fuzz.trimf(occupants.universe, [5, 7, 9])
occupants['many'] = fuzz.trimf(occupants.universe, [7, 9, 10])
occupants['very_many'] = fuzz.trapmf(occupants.universe, [8, 10, 10, 10])

insulation['very_poor'] = fuzz.trapmf(insulation.universe, [0, 0, 2, 4])
insulation['poor'] = fuzz.trimf(insulation.universe, [2, 4, 6])
insulation['average_poor'] = fuzz.trimf(insulation.universe, [4, 6, 7])
insulation['average_good'] = fuzz.trimf(insulation.universe, [6, 7, 9])
insulation['good'] = fuzz.trimf(insulation.universe, [7, 9, 10])
insulation['excellent'] = fuzz.trapmf(insulation.universe, [9, 10, 10, 10])

heating['very_low'] = fuzz.trapmf(heating.universe, [0, 0, 10, 20])
heating['low'] = fuzz.trimf(heating.universe, [10, 20, 40])
heating['low_medium'] = fuzz.trimf(heating.universe, [20, 40, 60])
heating['medium_high'] = fuzz.trimf(heating.universe, [40, 60, 80])
heating['high'] = fuzz.trimf(heating.universe, [60, 80, 100])
heating['very_high'] = fuzz.trapmf(heating.universe, [80, 100, 100, 100])

heating.defuzzify_method = 'centroid'

# Всі можливі правила вручну
rules = [
    ctrl.Rule(temperature['very_low'] & occupants['very_few'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_few'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_few'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_few'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_few'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_few'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['very_low'] & occupants['few'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['very_low'] & occupants['few'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['few'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['few'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['few'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['few'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['very_low'] & occupants['few_moderate'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['very_low'] & occupants['few_moderate'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['few_moderate'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['few_moderate'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['few_moderate'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['few_moderate'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['very_low'] & occupants['moderate_many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['very_low'] & occupants['moderate_many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['moderate_many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['moderate_many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['moderate_many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['moderate_many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['very_low'] & occupants['many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['very_low'] & occupants['many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['very_low'] & occupants['very_many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['very_low'] & occupants['very_many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low'] & occupants['very_few'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low'] & occupants['very_few'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['very_few'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['very_few'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['very_few'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['very_few'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low'] & occupants['few'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low'] & occupants['few'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['few'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['few'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['few'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['few'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low'] & occupants['few_moderate'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low'] & occupants['few_moderate'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['few_moderate'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['few_moderate'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['few_moderate'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['few_moderate'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low'] & occupants['moderate_many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low'] & occupants['moderate_many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['moderate_many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['moderate_many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['moderate_many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['moderate_many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low'] & occupants['many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low'] & occupants['many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low'] & occupants['very_many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low'] & occupants['very_many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['very_many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['very_many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low'] & occupants['very_many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low'] & occupants['very_many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_few'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_few'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_few'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_few'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_few'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_few'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low_medium'] & occupants['few'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low_medium'] & occupants['few_moderate'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few_moderate'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few_moderate'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few_moderate'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few_moderate'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['few_moderate'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low_medium'] & occupants['moderate_many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['moderate_many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['moderate_many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['moderate_many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['moderate_many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['moderate_many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low_medium'] & occupants['many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_many'] & insulation['very_poor'], heating['very_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_many'] & insulation['poor'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_many'] & insulation['average_good'], heating['medium_high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_many'] & insulation['good'], heating['high']),
    ctrl.Rule(temperature['low_medium'] & occupants['very_many'] & insulation['excellent'], heating['low_medium']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_few'] & insulation['very_poor'], heating['high']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_few'] & insulation['poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_few'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_few'] & insulation['average_good'], heating['low_medium']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_few'] & insulation['good'], heating['low']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_few'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high_medium'] & occupants['few'] & insulation['very_poor'], heating['high']),
    ctrl.Rule(temperature['high_medium'] & occupants['few'] & insulation['poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['few'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['few'] & insulation['average_good'], heating['low_medium']),
    ctrl.Rule(temperature['high_medium'] & occupants['few'] & insulation['good'], heating['low']),
    ctrl.Rule(temperature['high_medium'] & occupants['few'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high_medium'] & occupants['few_moderate'] & insulation['very_poor'], heating['high']),
    ctrl.Rule(temperature['high_medium'] & occupants['few_moderate'] & insulation['poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['few_moderate'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['few_moderate'] & insulation['average_good'], heating['low_medium']),
    ctrl.Rule(temperature['high_medium'] & occupants['few_moderate'] & insulation['good'], heating['low']),
    ctrl.Rule(temperature['high_medium'] & occupants['few_moderate'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high_medium'] & occupants['moderate_many'] & insulation['very_poor'], heating['high']),
    ctrl.Rule(temperature['high_medium'] & occupants['moderate_many'] & insulation['poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['moderate_many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['moderate_many'] & insulation['average_good'], heating['low_medium']),
    ctrl.Rule(temperature['high_medium'] & occupants['moderate_many'] & insulation['good'], heating['low']),
    ctrl.Rule(temperature['high_medium'] & occupants['moderate_many'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high_medium'] & occupants['many'] & insulation['very_poor'], heating['high']),
    ctrl.Rule(temperature['high_medium'] & occupants['many'] & insulation['poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['many'] & insulation['average_good'], heating['low_medium']),
    ctrl.Rule(temperature['high_medium'] & occupants['many'] & insulation['good'], heating['low']),
    ctrl.Rule(temperature['high_medium'] & occupants['many'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_many'] & insulation['very_poor'], heating['high']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_many'] & insulation['poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_many'] & insulation['average_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_many'] & insulation['average_good'], heating['low_medium']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_many'] & insulation['good'], heating['low']),
    ctrl.Rule(temperature['high_medium'] & occupants['very_many'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['very_few'] & insulation['very_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high'] & occupants['very_few'] & insulation['poor'], heating['low_medium']),
    ctrl.Rule(temperature['high'] & occupants['very_few'] & insulation['average_poor'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['very_few'] & insulation['average_good'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['very_few'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['very_few'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['few'] & insulation['very_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high'] & occupants['few'] & insulation['poor'], heating['low_medium']),
    ctrl.Rule(temperature['high'] & occupants['few'] & insulation['average_poor'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['few'] & insulation['average_good'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['few'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['few'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['few_moderate'] & insulation['very_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high'] & occupants['few_moderate'] & insulation['poor'], heating['low_medium']),
    ctrl.Rule(temperature['high'] & occupants['few_moderate'] & insulation['average_poor'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['few_moderate'] & insulation['average_good'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['few_moderate'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['few_moderate'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['moderate_many'] & insulation['very_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high'] & occupants['moderate_many'] & insulation['poor'], heating['low_medium']),
    ctrl.Rule(temperature['high'] & occupants['moderate_many'] & insulation['average_poor'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['moderate_many'] & insulation['average_good'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['moderate_many'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['moderate_many'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['many'] & insulation['very_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high'] & occupants['many'] & insulation['poor'], heating['low_medium']),
    ctrl.Rule(temperature['high'] & occupants['many'] & insulation['average_poor'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['many'] & insulation['average_good'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['many'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['many'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['very_many'] & insulation['very_poor'], heating['medium_high']),
    ctrl.Rule(temperature['high'] & occupants['very_many'] & insulation['poor'], heating['low_medium']),
    ctrl.Rule(temperature['high'] & occupants['very_many'] & insulation['average_poor'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['very_many'] & insulation['average_good'], heating['low']),
    ctrl.Rule(temperature['high'] & occupants['very_many'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['high'] & occupants['very_many'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_few'] & insulation['very_poor'], heating['low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_few'] & insulation['poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_few'] & insulation['average_poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_few'] & insulation['average_good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_few'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_few'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['few'] & insulation['very_poor'], heating['low']),


    ctrl.Rule(temperature['very_high'] & occupants['few'] & insulation['poor'], heating['very_low']),#187
    ctrl.Rule(temperature['very_high'] & occupants['few'] & insulation['average_poor'], heating['very_low']),#188

    ctrl.Rule(temperature['very_high'] & occupants['few'] & insulation['average_good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['few'] & insulation['good'], heating['very_low']),
    
    ctrl.Rule(temperature['very_high'] & occupants['few'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['few_moderate'] & insulation['very_poor'], heating['low']),
    ctrl.Rule(temperature['very_high'] & occupants['few_moderate'] & insulation['poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['few_moderate'] & insulation['average_poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['few_moderate'] & insulation['average_good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['few_moderate'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['few_moderate'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['moderate_many'] & insulation['very_poor'], heating['low']),
    ctrl.Rule(temperature['very_high'] & occupants['moderate_many'] & insulation['poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['moderate_many'] & insulation['average_poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['moderate_many'] & insulation['average_good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['moderate_many'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['moderate_many'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['many'] & insulation['very_poor'], heating['low']),
    ctrl.Rule(temperature['very_high'] & occupants['many'] & insulation['poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['many'] & insulation['average_poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['many'] & insulation['average_good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['many'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['many'] & insulation['excellent'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_many'] & insulation['very_poor'], heating['low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_many'] & insulation['poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_many'] & insulation['average_poor'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_many'] & insulation['average_good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_many'] & insulation['good'], heating['very_low']),
    ctrl.Rule(temperature['very_high'] & occupants['very_many'] & insulation['excellent'], heating['very_low']),
]


heating_ctrl = ctrl.ControlSystem(rules)
heating_simulation = ctrl.ControlSystemSimulation(heating_ctrl)

# Функція для обчислення з силою правил
def calculate_heating_with_rule_strength(temp, occ, ins):
    if not (0 <= temp <= 40):
        raise ValueError("Temperature must be in range 0-40 °C")
    if not (0 <= occ <= 10):
        raise ValueError("Occupants count must be in range 0-10")
    if not (0 <= ins <= 10):
        raise ValueError("Insulation level must be in range 0-10")

    # Встановлення вхідних значень
    heating_simulation.input['temperature'] = temp
    heating_simulation.input['occupants'] = occ
    heating_simulation.input['insulation'] = ins

    # Розрахунок сили правил вручну
    active_rules = 0
    for idx, rule in enumerate(rules):
        antecedents = rule.antecedent_terms

        temp_label = antecedents[0].label
        occ_label = antecedents[1].label
        ins_label = antecedents[2].label

        temp_mf = fuzz.interp_membership(temperature.universe, temperature[temp_label].mf, temp)
        occ_mf = fuzz.interp_membership(occupants.universe, occupants[occ_label].mf, occ)
        ins_mf = fuzz.interp_membership(insulation.universe, insulation[ins_label].mf, ins)

        # Мінімальна сила правила
        rule_strength = min(temp_mf, occ_mf, ins_mf)
        if rule_strength > 0:
            active_rules += 1
            print(f"Rule {idx + 1}: Strength = {rule_strength:.2f}")

    if active_rules == 0:
        raise ValueError("No active rules for the given inputs. Check the rule definitions.")

    heating_simulation.compute()

    result = heating_simulation.output.get('heating', None)
    if result is None:
        raise ValueError("Heating calculation failed. Check your rules or inputs.")

    print(f"Heating Output: {result:.2f}%")
    return result

# Візуалізація результатів
def plot_membership():
    plt.figure(figsize=(10, 6))
    plt.plot(heating.universe, heating['very_low'].mf, label='Very Low')
    plt.plot(heating.universe, heating['low'].mf, label='Low')
    plt.plot(heating.universe, heating['low_medium'].mf, label='Low Medium')
    plt.plot(heating.universe, heating['medium_high'].mf, label='Medium High')
    plt.plot(heating.universe, heating['high'].mf, label='High')
    plt.plot(heating.universe, heating['very_high'].mf, label='Very High')
    plt.title('Heating Membership Functions')
    plt.xlabel('Heating (%)')
    plt.ylabel('Membership Degree')
    plt.legend()
    plt.grid()
    plt.show()


