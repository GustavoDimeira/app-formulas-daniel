import tkinter as tk
import sympy as sp

def get_sympify_value(value, conversion_factor=None):
    value_str = str(value.get())
    if value_str.strip():  # Verifica se a string não está vazia
        result = sp.sympify(value_str)
        if conversion_factor:
            result *= conversion_factor
        return result
    else:
        return None  # Retorna None se a string estiver vazia

def obter_valores(first_values, conversion_factors):
    result = {}
    for key, conversion_factor in conversion_factors.items():
        result[key] = get_sympify_value(first_values[key][3], conversion_factor)
    return result

root = tk.Tk()
variables_dict = {"section_1": {"gear": {}, "pinion": {}}}
meters_to_inches = 39.3701  # Fator de conversão de metros para polegadas

conversion_factors_gear = {"Pc_g": None, "Pb_g": None, "Pd_g": None, "N_g": None, "d_g": meters_to_inches, "m_g": None, "θ": None}
conversion_factors_pinion = {"Pc_p": None, "Pb_p": None, "Pd_p": None, "N_p": None, "d_p": meters_to_inches, "m_p": None}

# Exemplo de uso
first_values_gear = variables_dict["section_1"]["gear"]
first_values_pinion = variables_dict["section_1"]["pinion"]

valores_gear = obter_valores(first_values_gear, conversion_factors_gear)
valores_pinion = obter_valores(first_values_pinion, conversion_factors_pinion)

print(valores_gear)
print(valores_pinion)

root.mainloop()
