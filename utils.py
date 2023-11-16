import sympy as sp
from tkinter import ttk
from variables import *
from variables import variables_dict

meters_to_inches = 0.0254 ** -1
inches_to_milimeters = 25.4

def create_entry(crr_row, var_name, frame):
    label = ttk.Label(frame, text=f"{var_name}:")
    label.grid(row= crr_row, column= 0, padx= 10, pady= 10)

    input = ttk.Entry(frame)
    input.grid(row= crr_row, column= 1, padx= 10, pady= 10)

    return input


def create_option(crr_row, var_name, frame, options):
    label = ttk.Label(frame, text=f"{var_name}:")
    label.grid(row= crr_row, column= 0, padx= 10, pady= 10)
    
    combobox = ttk.Combobox(frame, textvariable=var_name, values=options)
    combobox.grid(row= crr_row, column= 1, padx= 10, pady= 10)

    return combobox


def create_section(main_frame, section_name):
    section = variables_dict[section_name]
    crr_row = 0

    frame_global = ttk.Frame(main_frame)
    frame_gear = ttk.Frame(frame_global)
    frame_pinion = ttk.Frame(frame_global)
    frame_mutual = ttk.Frame(frame_global)

    frame_global.grid(column=0)
    frame_gear.grid(padx= 10, pady= 10)
    frame_pinion.grid(padx= 10, pady= 10)
    frame_mutual.grid(padx= 10, pady= 10)

    for var in [*section["gear"], *section["pinion"], *section["mutual"]]:
        is_gear = crr_row < len(section["gear"])
        is_pinion = crr_row <= len(section["gear"]) * 2 - 1
        
        crr_sub_section = "gear" if is_gear else"pinion" if is_pinion else "mutual"
        crr_frame = frame_gear if is_gear else frame_pinion if is_pinion else frame_mutual

        var_infos = section[crr_sub_section][var]

        if (var_infos["type"] == "label"):
            element = create_entry(crr_row, var, crr_frame)
        else:
            element = create_option(crr_row, var, crr_frame, var_infos["options"])

        variables_dict[section_name][crr_sub_section][var]["element"] = element
        crr_row += 1

    btn_func = calc_first if section_name == "section_1" else calc_second if section_name == "section_2" else calc_third # define a função do botão, baseando-se no nome da section

    calc_btn = ttk.Button(
        frame_global, text="Calcular", command=lambda: btn_func(main_frame)
    )
    calc_btn.grid(columnspan=2)


def create_table(frame, items):
    table = ttk.Treeview(frame, columns=("Nome", "Valor", "Unidade"))

    table.heading("Nome", text="Nome")
    table.heading("Valor", text="Valor")
    table.heading("Unidade", text="Unidade")

    for values in items:
      table.insert("", "end", values=values)

    table.grid(row= 0, column= 1, padx= 10, pady= 10)


def define_values(var_obj, list_values, table_values):
   var_value = var_obj["element"].get()

   if (not var_value == ''): # verifica se o valor foi definido no campo
        list_values.append((var_obj["var"], var_value)) # tupla com a variavel e o valor
        table_values.append((var_obj["var"], var_value, ""))


def calc_first(frame):
    first_section = {
      **variables_dict["section_1"]["gear"], 
      **variables_dict["section_1"]["pinion"], 
      **variables_dict["section_1"]["mutual"]
    } # cria objeto com todas as variaveis da section 1

    list_values = [] # tuplas com variaves e valores
    table_values = [] # tuplas com variaveis, valores e unidades
    for var_name in first_section:
       define_values(first_section[var_name], list_values, table_values)

    equations = [
        sp.Eq(Pc_g, sp.pi * d_g / N_g),
        sp.Eq(Pb_g, Pc_g * sp.cos(0.5)),
        sp.Eq(Pd_g, N_g / d_g),
        sp.Eq(m_g, (d_g * inches_to_milimeters) / N_g),
        sp.Eq(Pc_p, sp.pi * d_p / N_p),
        sp.Eq(Pb_p, Pc_p * sp.cos(0.5)),
        sp.Eq(Pd_p, N_p / d_p),
        sp.Eq(m_p, (d_p * inches_to_milimeters) / N_p),
    ]

    equations_with_values = [eq.subs(list_values) for eq in equations] # substitui nas equações os valores definidos
    solution = sp.solve(equations_with_values)

    for var in solution:
        table_values.append((var, solution[var], ""))

    gear_list_values = [
        ["adendo", 1/Pd_g, "in-¹"],
        ["dedendo", 1.25/Pd_g, "in-¹"],
        ["profundidade de trabalo", 2/Pd_g, "in-¹"],
        ["profundidade total", 2.25/Pd_g if (1 < 20) else ((2.2/Pd_g) + 0.002), "in-¹"],
        ["espessura circular dente", 1.571/Pd_g, "in-¹"],
        ["raio arredondamento", 0.3/Pd_g if (1 < 20) else "não padronizado", "in-¹"],
        ["folga basica minima", 0.25/Pd_g if (1 < 20) else ((0.2/Pd_g) + 0.002), "in-¹"],
        ["largura minima topo", 0.25/Pd_g if (1 < 20) else "não padronizado", "in-¹"],
        ["folga dentes polidos", 0.35/Pd_g if (1 < 20) else ((0.35/Pd_g) + 0.002), "in-¹"]
    ]

    pinion_list_values = [
        ["adendo", 1/Pd_p, "in-¹"],
        ["dedendo", 1.25/Pd_p, "in-¹"],
        ["profundidade de trabalo", 2/Pd_p, "in-¹"],
        ["profundidade total", 2.25/Pd_p if (1 < 20) else ((2.2/Pd_p) + 0.002), "in-¹"],
        ["espessura circular dente", 1.571/Pd_p, "in-¹"],
        ["raio arredondamento", 0.3/Pd_p if (1 < 20) else "não padronizado", "in-¹"],
        ["folga basica minima", 0.25/Pd_p if (1 < 20) else ((0.2/Pd_p) + 0.002), "in-¹"],
        ["largura minima topo", 0.25/Pd_p if (1 < 20) else "não padronizado", "in-¹"],
        ["folga dentes polidos", 0.35/Pd_p if (1 < 20) else ((0.35/Pd_p) + 0.002), "in-¹"]
    ]

    create_table(frame, [*table_values, *gear_list_values, *pinion_list_values])


def calc_second(frame):
  pass


def calc_third(frame):
  pass
