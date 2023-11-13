from variables import *
import sympy as sp

meters_to_inches = 0.0254 ** -1
inches_to_milimeters = 25.4

def calc_first():
    first_values = {
      **variables_dict["section_1"]["gear"], 
      **variables_dict["section_1"]["pinion"], 
      # **variables_dict["section_1"]["mutual"]
    }
  
    def get_sympify_value(value, conversion_factor=None):
      print(value)
      value_str = str(value.get())
      if value_str.strip():  # Verifica se a string não está vazia
          result = sp.sympify(value_str)
          if conversion_factor:
              result *= conversion_factor
          return result
      else:
          return None  # Retorna None se a string estiver vazia

    def obter_valores(first_values):
        result = {}
        for key in first_values:
            result[key] = get_sympify_value(first_values[key][3], 1)
        return result

    
    print(obter_valores(first_values))

    print(Pc_g, Pb_g, Pd_g)

    equations = [
        sp.Eq(Pc_g, sp.pi * d_g / N_g),
        sp.Eq(Pb_g, Pc_g * sp.cos(θ)),
        sp.Eq(Pd_g, N_g / d_g),
        sp.Eq(m_g, (d_g * inches_to_milimeters) / N_g),
        sp.Eq(Pc_p, sp.pi * d_p / N_p),
        sp.Eq(Pb_p, Pc_p * sp.cos(θ)),
        sp.Eq(Pd_p, N_p / d_p),
        sp.Eq(m_p, (d_p * inches_to_milimeters) / N_p),
    ]

    solution = sp.solve(equations, variables_g_1 + variables_p_1)


def calc_second():
  pass


def calc_third():
  pass