import sympy as sp
from math import pi
import math

from tkinter import ttk
from variables import *
from variables import variables_dict

meters_to_inches = 0.0254 ** -1
inches_to_milimeters = 25.4
# objetos para armazenar os valores calculados e definidos
gear_values_1 =  {}
pinion_values_1 =  {}
mutual_values_1 =  {}

gear_values_2 =  {}
pinion_values_2 =  {}
mutual_values_2 =  {}

gear_values_3 =  {}
pinion_values_3 =  {}
mutual_values_3 =  {}

apertado_values_1 = {}
folgado_values_1 = {}

open_values_1 = {}
close_values_1 = {}

corrente_values_1 = {}
# cria um campo do tipo entry
def create_entry(crr_row, var_name, frame):
    label = ttk.Label(frame, text=f"{var_name}:")
    label.grid(row= crr_row, column= 0, padx= 3, pady= 3)

    input = ttk.Entry(frame)
    input.grid(row= crr_row, column= 1, padx= 3, pady= 3)

    return input

# cria um campo do tipo combobox (select)
def create_option(crr_row, var_name, frame, options):
    label = ttk.Label(frame, text=f"{var_name}:")
    label.grid(row= crr_row, column= 0, padx= 3, pady= 3)
    
    combobox = ttk.Combobox(frame, textvariable=var_name, values=options)
    combobox.grid(row= crr_row, column= 1, padx= 3, pady= 3)

    return combobox

# cria as tabelas para mostrar o resultado dos calculos
def create_table(frame, items, row, column, widths):
    table = ttk.Treeview(frame, columns=("Nome", "Valor", "Unidade"))

    table.heading("#0", text="ID")
    table.heading("Nome", text="Nome")
    table.heading("Valor", text="Valor")
    table.heading("Unidade", text="Unidade")

    table.column("#0", width=widths[0])
    table.column("Nome", width=widths[1])
    table.column("Valor", width=widths[2])
    table.column("Unidade", width=widths[3])

    id = 0
    for item in items:
      values = items[item] # pega a lista contendo, nome, valor, unidade de medida
      id += 1
      table.insert("", str(id), values=values)

    table.grid(row= row, column= column, padx= 10, pady= 10)

# cria as telas principais, que armazena com os campos input e futuramente as tabelas
def create_section(main_frame, section_name):
    section = variables_dict[section_name]
    crr_row = 0

    frame_gear = ttk.Frame(main_frame)
    frame_pinion = ttk.Frame(main_frame)
    frame_mutual = ttk.Frame(main_frame)

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

    btn_func = calc_first if section_name == "section_1" else calc_second if section_name == "section_2" else calc_third if section_name == "section_3" else calc_fourth if section_name == "section_4" else calc_tifth if section_name == "section_5" else calc_sixth
    
    calc_btn = ttk.Button(
        main_frame, text="Calcular", command=lambda: btn_func(main_frame)
    ) # define a função do botão, baseando-se no nome da section
    calc_btn.grid(columnspan=2)

# armazena os valores calculados e definidos pelo usuario
def define_values(var_obj, seted_values, gear_obj, pinion_obj, mutual_obj, has_calculated = False):
   var_name = var_obj["var"]
   var_value = var_obj["value"] if has_calculated else var_obj["element"].get() # verifica se foi calculado ou definido pelo usuario(isso implica em como o valor fica armazenado)

   if (not var_value == ''): # verifica se o valor foi definido no campo
        value = sp.sympify(var_value)
        seted_values.append((var_name, value)) # tupla com a variavel e o valor
        
        if str(var_name).split("_")[-1] == 'g' or str(var_name).split("_")[-1] == 'a' or str(var_name).split("_")[-1] == 'o': # valida se a variavel é da gear, pinion ou mutual
            gear_obj[str(var_name)] = ((var_name, value, ""))
        elif str(var_name).split("_")[-1] == 'p' or str(var_name).split("_")[-1] == 'f' or str(var_name).split("_")[-1] == 'c':
            pinion_obj[str(var_name)] = ((var_name, value, ""))
        else:
            mutual_obj[str(var_name)] = ((var_name, value, ""))

# função que realiza os calculos da primeira tela
def calc_first(frame):
    # as variaveis a seguir são definidas em um escopo global, mas são "redefinidas" localmente, por isso a necessidade dessa linha
    global gear_values_1, pinion_values_1, mutual_values_1

    first_section = {
      **variables_dict["section_1"]["gear"], 
      **variables_dict["section_1"]["pinion"], 
      **variables_dict["section_1"]["mutual"]
    } # cria objeto com todas as variaveis da section 1

    seted_values = [] # tuplas para setar os valores definidos pelo usuario

    for var_name in first_section: # armazena os valores definidos pelo usuario
       define_values(first_section[var_name], seted_values, gear_values_1, pinion_values_1, mutual_values_1)

    θ = mutual_values_1["θ"][1]

    equations = [
        sp.Eq(Pc_g, pi * d_g / N_g),
        sp.Eq(Pb_g, Pc_g * sp.cos(θ)),
        sp.Eq(Pd_g, N_g / d_g),
        sp.Eq(m_g, (d_g * inches_to_milimeters) / N_g),
        sp.Eq(Pc_p, pi * d_p / N_p),
        sp.Eq(Pb_p, Pc_p * sp.cos(θ)),
        sp.Eq(Pd_p, N_p / d_p),
        sp.Eq(m_p, (d_p * inches_to_milimeters) / N_p),
    ] # define equações para os calculos

    equations_with_values = [eq.subs(seted_values) for eq in equations] 
    # substitui nas equações os valores definidos pelo usuario
    solution = sp.solve(equations_with_values) # realiza o calculo

    for var in solution: # armazena os valores calculados
        var_obj = {
            "var": var,
            "value": solution[var]
        }
        define_values(var_obj, seted_values, gear_values_1, pinion_values_1, mutual_values_1, True)

    val_Pd_g = gear_values_1["Pd_g"][1] # define o valor das variaveis para calculos futuros
    val_d_g = gear_values_1["d_g"][1]
    val_Pb_g = gear_values_1["Pb_g"][1]

    val_Pd_p = pinion_values_1["Pd_p"][1]
    val_d_p = pinion_values_1["d_p"][1]
    val_Pb_p = pinion_values_1["Pb_p"][1]
    
    gear_values_1 = { # mais valores, esses só precisam do passo diametral
        **gear_values_1,
        "adendo": ["adendo", 1/val_Pd_g, "in-¹"],
        "dedendo": ["dedendo", 1.25/val_Pd_g, "in-¹"],
        "profundidade de trabalo": ["profundidade de trabalo", 2/val_Pd_g, "in-¹"],
        "profundidade total":
            ["profundidade total", 2.25/val_Pd_g if (1 < 20) else ((2.2/val_Pd_g) + 0.002), "in-¹"],
        "espessura circular dente": ["espessura circular dente", 1.571/val_Pd_g, "in-¹"],
        "raio arredondamento":
            ["raio arredondamento", 0.3/val_Pd_g if (1 < 20) else "não padronizado", "in-¹"],
        "folga basica":
            ["folga basica", 0.25/val_Pd_g if (1 < 20) else ((0.2/val_Pd_g) + 0.002), "in-¹"],
        "largura topo": ["largura topo", 0.25/val_Pd_g if (1 < 20) else "não padronizado", "in-¹"],
        "folga dentes":
            ["folga dentes", 0.35/val_Pd_g if (1 < 20) else ((0.35/val_Pd_g) + 0.002), "in-¹"]
    }

    pinion_values_1 = {
        **pinion_values_1,
        "adendo": ["adendo", 1/val_Pd_p, "in-¹"],
        "dedendo": ["dedendo", 1.25/val_Pd_p, "in-¹"],
        "profundidade de trabalo": ["profundidade de trabalo", 2/val_Pd_p, "in-¹"],
        "profundidade total":
            ["profundidade total", 2.25/val_Pd_p if (1 < 20) else ((2.2/val_Pd_p) + 0.002), "in-¹"],
        "espessura circular dente": ["espessura circular dente", 1.571/val_Pd_p, "in-¹"],
        "raio arredondamento":
            ["raio arredondamento", 0.3/val_Pd_p if (1 < 20) else "não padronizado", "in-¹"],
        "folga basica":
            ["folga basica", 0.25/val_Pd_p if (1 < 20) else ((0.2/val_Pd_p) + 0.002), "in-¹"],
        "largura topo": ["largura topo", 0.25/val_Pd_p if (1 < 20) else "não padronizado", "in-¹"],
        "folga dentes":
            ["folga dentes", 0.35/val_Pd_p if (1 < 20) else ((0.35/val_Pd_p) + 0.002), "in-¹"]
    }

    # essa parte calcula o valor da variavel z
    variables_Z_1 = sp.symbols('r_ga_g r_gcos_g r_pa_p r_pcos_p C z')
    r_ga_g, r_gcos_g, r_pa_p, r_pcos_p, c, z = variables_Z_1

    C = val_d_g / 2 + val_d_p / 2

    r_ga_g = (val_d_g / 2 + gear_values_1["adendo"][1]) ** 2
    r_gcos_g = ((val_d_g / 2) * sp.cos(θ)) ** 2
    r_pa_p = (val_d_p / 2 + pinion_values_1["adendo"][1]) ** 2
    r_pcos_p = ((val_d_p / 2) * sp.cos(θ)) ** 2

    solution_z = sp.solve(
        sp.Eq(((r_pa_p - r_pcos_p) ** (1/2)) +
              ((r_ga_g - r_gcos_g) ** (1/2)) - (C * sp.sin(θ)), z),
        variables_Z_1
    )

    mp_g = abs(solution_z[0][-1] / val_Pb_g)
    mp_p = abs(solution_z[0][-1] / val_Pb_p)

    print(solution_z)

    mutual_values_1 = {
        **mutual_values_1,
        "C": ["C", C, "in"],
        "z": ["z", solution_z[0][-1].evalf(), "variavel"],
        "mp_g": ["mp_g", mp_g, "variavel"],
        "mp_p": ["mp_p", mp_p, "variavel"],
    }

    create_table(frame, gear_values_1, 0, 1, [5, 170, 52, 80]) # mostra os valores calculados em uma treeview (tabela)
    create_table(frame, pinion_values_1, 0, 2, [5, 170, 52, 80])
    create_table(frame, mutual_values_1, 1, 1, [5, 170, 52, 80])


def calc_second(frame):
    global gear_values_2, pinion_values_2, mutual_values_2

    first_section = {
      **variables_dict["section_2"]["gear"], 
      **variables_dict["section_2"]["pinion"], 
      **variables_dict["section_2"]["mutual"]
    } # cria objeto com todas as variaveis da section 1

    seted_values = [] # tuplas para setar os valores definidos pelo usuario

    for var_name in first_section: # armazena os valores definidos pelo usuario
       define_values(first_section[var_name], seted_values, gear_values_2, pinion_values_2, mutual_values_2)

    m_g = gear_values_1["m_g"][1] # valores para calculos futuros
    d_g = gear_values_1["d_g"][1]
    F_g = gear_values_2["F_g"][1]
    J_g = gear_values_2["J_g"][1]
    Qv_g = gear_values_2["Qv_g"][1]
    Vt_g = gear_values_2["Vt_g"][1]
    tr_g = gear_values_2["tr_g"][1]
    Ks_g = 1 # gear_values_2["Ks_g"][1]
    mat_g = gear_values_2["mat_g"][1]
    pot_g = gear_values_2["pot_g"][1]
    rpm_g = gear_values_2["rpm_g"][1]
    mover_g = gear_values_2["mover_g"][1]
    adendo_g = gear_values_1["adendo"][1]
    dedendo_g = gear_values_1["dedendo"][1]
    moveabel_g = gear_values_2["moveabel_g"][1]

    m_p = pinion_values_1["m_p"][1]
    d_p = pinion_values_1["d_p"][1]
    F_p = pinion_values_2["F_p"][1]
    J_p = pinion_values_2["J_p"][1]
    Pd_p = pinion_values_1["Pd_p"][1]
    Qv_p = pinion_values_2["Qv_p"][1]
    Vt_p = pinion_values_2["Vt_p"][1]
    tr_p = pinion_values_2["tr_p"][1]
    Ks_p = 1 # pinion_values_2["Ks_p"][1]
    mat_p = pinion_values_2["mat_p"][1]
    pot_p = pinion_values_2["pot_p"][1]
    rpm_p = pinion_values_2["rpm_p"][1]
    mover_p = pinion_values_2["mover_p"][1]
    adendo_p = pinion_values_1["adendo"][1]
    dedendo_p = pinion_values_1["dedendo"][1]
    moveabel_p = pinion_values_2["moveabel_p"][1]
    
    θ = mutual_values_1["θ"][1]
    C = mutual_values_1["C"][1]
    pos = mutual_values_2["theeth_pos"][1]

    F_g = max(8 * m_g, min(F_g, 16 * m_g))
    F_p = max(8 * m_p, min(F_p, 16 * m_g))

    Qv_g_fpm = Qv_g * 196.850394
    Qv_p_fpm = Qv_p * 196.850394

    if (0 < Vt_g <= 800 and not (6 <= Qv_g_fpm <= 8)): Qv_g = 7
    if (800 < Vt_g <= 2000 and not (8 <= Qv_g_fpm <= 10)): Qv_g = 9
    if (2000 < Vt_g <= 4000 and not (10 <= Qv_g_fpm <= 12)): Qv_g = 11
    if (4000 < Vt_g and not (12 <= Qv_g_fpm <= 14)): Qv_g = 13

    if (0 < Vt_p <= 800 and not (6 <= Qv_p_fpm <= 8)): Qv_p = 7
    if (800 < Vt_p <= 2000 and not (8 <= Qv_p_fpm <= 10)): Qv_p = 9
    if (2000 < Vt_p <= 4000 and not (10 <= Qv_p_fpm <= 12)): Qv_p = 11
    if (4000 < Vt_p and not (12 <= Qv_p_fpm <= 14)): Qv_p = 13

    B_g = ((12 / Qv_g) ** (2/3)) / 4
    A_g = 50 + 56 * (1 - B_g)
    mb_g = tr_g / (adendo_g + dedendo_g)

    B_p = ((12 / Qv_p) ** (2/3)) / 4
    A_p = 50 + 56 * (1 - B_p)
    mb_p = tr_p / (adendo_p + dedendo_p)

    kv_g = (A_g / (A_g + ((200 * Vt_g) ** 1/2))) ** B_g
    Ka_g = 1 + ((mover_g + moveabel_g) * 0.25)
    Kb_g = -2 * mb_g + 3.4 if (mb_g >= 0.5 and mb_g <= 1.2) else 1
    Ki_g = 1

    if F_g < 50: km_g = 1.6
    if F_g < 150: km_g = 1.7
    if F_g < 250: km_g = 1.8
    if F_g < 500: km_g = 1.9
    if F_g >= 500: km_g = 2

    kv_p = (A_p / (A_p + ((200 * Vt_p) ** 1/2))) ** B_p
    Ka_p = 1 + ((mover_p + moveabel_p) * 0.25)
    Kb_p = -2 * mb_p + 3.4 if (mb_p >= 0.5 and mb_p <= 1.2) else 1
    Ki_p = 1

    if F_p < 50: km_p = 1.6
    if F_p < 150: km_p = 1.7
    if F_p < 250: km_p = 1.8
    if F_p < 500: km_p = 1.9
    if F_p >= 500: km_p = 2

    torq_g = (60*75*pot_g)/(2*3.14*rpm_g)
    r_g = d_g / 2
    Wt_g = torq_g / r_g
    flex_agma_g = (Wt_g / (F_g * m_g * J_g)) * ((Ka_g * km_g) / kv_g) * (Kb_g + Ks_g + Ki_g)

    torq_p = (60*75*pot_p)/(2*3.14*rpm_p)
    r_p = d_p / 2
    Wt_p = torq_p / r_p
    flex_agma_p = (Wt_p / (F_p * m_p * J_p)) * ((Ka_p * km_p) / kv_p) * (Kb_p + Ks_p + Ki_p)

    gear_values_2 = {
        **gear_values_2,
        "kmg": ["kmg", km_g, 'Fator dinámico'],
        "kvg": ["kvg", kv_g, 'Fator dinámico'],
        "Kag": ["Kag", Ka_g, 'Fator dinámico'],
        "Kig": ["Kig", Ki_g, 'Fator dinámico'],
        "Kbp": ["Kbp", Kb_g, 'Fator dinámico'],
        "Ksg": ["Ksg", Ks_g, 'Fator dinámico'],
        "Ag": ["Ag", A_g, ''],
        "Bg": ["Bg", B_g, ''],
        "mbg": ["mbg", mb_g, 'Razão de recuo'],
        "Qvg": ["Qvg", Qv_g, 'Qualidade Engre.'],
        "σ": ["σ", flex_agma_g, 'Tensão de Flexão'],
    }

    pinion_values_2 = {
        **pinion_values_2,
        "kmp": ["kmp", km_p, 'Fator dinámico'],
        "kvp": ["kvp", kv_p, 'Fator dinámico'],
        "Kap": ["Kap", Ka_p, 'Fator dinámico'],
        "Kip": ["Kip", Ki_p, 'Fator dinámico'],
        "Kbp": ["Kbp", Kb_p, 'Fator dinámico'],
        "Ksp": ["Ksp", Ks_p, 'Fator dinámico'],
        "Ap": ["Ap", A_p, ''],
        "Bp": ["Bp", B_p, ''],
        "mbp": ["mbp", mb_p, 'Razão de recuo'],
        "Qvp": ["Qvp", Qv_p, 'Qualidade Engre.'],
        "σ": ["σ", flex_agma_p, 'Tensão de Flexão'],
    }

    values = [
        191, 181, 179, 174, 162, 158, 181, 174, 172, 168, 158, 154, 179, 172, 170, 166, 156, 152, 174, 168, 166, 163, 154, 149, 162, 158, 156, 154, 145, 141, 158, 154, 152, 149, 141, 137
    ]
    C_p = values[mat_g * 6 + mat_p]

    P_p = ((r_p + 1 / Pd_p) ** 2 - (r_p * sp.cos(θ)) ** 2) ** (1/2) - (pi / Pd_p) * sp.cos(θ)
    P_g = C * sp.sin(θ) + (pos + P_p)
    I = sp.cos(θ) / ((1/P_p + (1 * pos)/P_g) * d_p)

    σc_p = C_p * ((Wt_p / (F_p * I * d_p)) * ((Ka_p * km_p) / kv_p) * Ks_p * 1) ** (1/2)
    σc_g = C_p * ((Wt_g / (F_g * I * d_g)) * ((Ka_g * km_g) / kv_g) * Ks_g * 1) ** (1/2)

    mutual_values_2 = {
        **mutual_values_2,
        "P_p": ["P_p", P_p.evalf(), 'Raio de Curvatura'],
        "P_g": ["P_g", P_g.evalf(), 'Raio de Curvatura'],
        "I": ["I", I.evalf(), 'Fator Geométrico'],
        "σc_p": ["σc_p", σc_p.evalf(), 'Tensão Superficial'],
        "σc_g": ["σc_g", σc_g.evalf(), 'Tensão Superficial'],
    }

    create_table(frame, gear_values_2, 0, 1, [5, 95, 52, 140])
    create_table(frame, pinion_values_2, 1, 1, [5, 95, 52, 140])
    create_table(frame, mutual_values_2, 0, 2, [5, 95, 52, 140])


def calc_third(frame):
    global gear_values_3, pinion_values_3, mutual_values_3

    third_section = {
      **variables_dict["section_3"]["gear"], 
      **variables_dict["section_3"]["pinion"], 
      **variables_dict["section_3"]["mutual"]
    } # cria objeto com todas as variaveis da section 1

    seted_values = [] # tuplas para setar os valores definidos pelo usuario

    for var_name in third_section: # armazena os valores definidos pelo usuario
       define_values(third_section[var_name], seted_values, gear_values_3, pinion_values_3, mutual_values_3)

    T_g = gear_values_3["T_g"][1]
    hb_g = gear_values_3["hb_g"][1]
    Kr_g = gear_values_3["Kr_g"][1]
    N_cicle_g = gear_values_3["N_cicle_g"][1]
    Sfb_linha__g = gear_values_3["Sfb_linha__g"][1]

    T_p = pinion_values_3["T_p"][1]
    hb_p = pinion_values_3["hb_p"][1]
    Kr_p = pinion_values_3["Kr_p"][1]
    N_cicle_p = pinion_values_3["N_cicle_p"][1]
    Sfb_linha__p = pinion_values_3["Sfb_linha__p"][1]

    if (hb_g == 400): Kl_g = 9.4518 * N_cicle_g ** -0.148
    if (hb_g == 250): Kl_g = 4.9404 * N_cicle_g ** -0.1192
    if (hb_g == 160): Kl_g = 2.3194 * N_cicle_g ** -0.1045

    if (hb_p == 400): Kl_p = 9.4518 * N_cicle_p ** -0.148
    if (hb_p == 250): Kl_p = 4.9404 * N_cicle_p ** -0.1192
    if (hb_p == 160): Kl_p = 2.3194 * N_cicle_p ** -0.1045

    Kt_g = 1 if (T_g < 250) else ((460 + T_g) / 620)
    Kt_p = 1 if (T_p < 250) else ((460 + T_p) / 620)

    Sfb_g = (Kl_g / (Kt_g * Kr_g)) * Sfb_linha__g
    Sfb_p = (Kl_p / (Kt_p * Kr_p)) * Sfb_linha__p

    gear_values_3 = {
        **gear_values_3,
        "Kt_g": ["Kt_g", Kt_g, 'Fator Dinámico'],
        "Kr_g": ["Kr_g", Kr_g, 'Fator Dinámico'],
        "Kl_g": ["Kl_g", Kl_g, 'Fator Dinámico'],
        "Sfb_g": ["Sfb_g", Sfb_g, 'Tabelado']
    }

    pinion_values_3 = {
        **pinion_values_3,
        "Kt_p": ["Kt_p", Kt_p, 'Fator Dinámico'],
        "Kr_p": ["Kr_p", Kr_p, 'Fator Dinámico'],
        "Kl_p": ["Kl_p", Kl_p, 'Fator Dinámico'],
        "Sfb_p": ["Sfb_p", Sfb_p, 'Tabelado']
    }

    create_table(frame, gear_values_3, 0, 1, [5, 90, 52, 140])
    create_table(frame, pinion_values_3, 0, 2, [5, 90, 52, 140])


def calc_fourth(frame):
    global apertado_values_1, folgado_values_1

    third_section = {
      **variables_dict["section_4"]["gear"], 
      **variables_dict["section_4"]["pinion"], 
      **variables_dict["section_4"]["mutual"]
    }

    seted_values = [] # tuplas para setar os valores definidos pelo usuario

    for var_name in third_section: # armazena os valores definidos pelo usuario
       define_values(third_section[var_name], seted_values, apertado_values_1, folgado_values_1, {})

    Fi_a = apertado_values_1["Fi_a"][1]
    D_a = apertado_values_1["D_a"][1]
    w_a = apertado_values_1["w_a"][1]
    v_a = apertado_values_1["v_a"][1]
    T_a = apertado_values_1["T_a"][1]

    Fi_f = folgado_values_1["Fi_f"][1]
    D_f = folgado_values_1["D_f"][1]
    w_f = folgado_values_1["w_f"][1]
    v_f = folgado_values_1["v_f"][1]
    T_f = folgado_values_1["T_f"][1]

    Fc_a = (w_a / 32.17) * (v_a / 60) ** 2
    Fi_linha_a = T_a / D_a
    Fl_a = Fi_a + Fi_linha_a + Fc_a

    Fc_f = (w_f / 32.17) * (v_f / 60) ** 2
    Fi_linha_f = T_f / D_f
    Fl_f = Fi_f + Fi_linha_f + Fc_f

    apertado_values_1 = {
        **apertado_values_1,
        "Fc_a": ["Fc_a", Fc_a, ''],
        "Fi_linha_a": ["Fi_linha_a", Fi_linha_a, ''],
        "Fl_a": ["Fl_a", Fl_a, ''],
    }

    folgado_values_1 = {
        **folgado_values_1,
        "Fc_f": ["Fc_f", Fc_f, ''],
        "Fi_linha_f": ["Fi_linha_f", Fi_linha_f, ''],
        "Fl_f": ["Fl_f", Fl_f, ''],
    }

    create_table(frame, apertado_values_1, 0, 1, [5, 90, 52, 140])
    create_table(frame, folgado_values_1, 0, 2, [5, 90, 52, 140])


def calc_tifth(frame):
    global open_values_1, close_values_1

    third_section = {
      **variables_dict["section_5"]["gear"], 
      **variables_dict["section_5"]["pinion"], 
    }

    seted_values = [] # tuplas para setar os valores definidos pelo usuario

    for var_name in third_section: # armazena os valores definidos pelo usuario
       define_values(third_section[var_name], seted_values, open_values_1, close_values_1, {})

    D_o = open_values_1["D_o"][1]
    d_o = open_values_1["d_o"][1]

    D_c = close_values_1["D_c"][1]
    d_c = close_values_1["d_c"][1]

    C_o = D_o + d_o
    θD_o = (math.pi + math.sin(math.radians(2) ** -1)) * ((D_o - d_o) / (2 * C_o))
    θd_o = (math.pi - math.sin(math.radians(2) ** -1)) * ((D_o - d_o) / (2 * C_o))
    L_o = sp.sqrt(4 * C_o**2 - (D_o - d_o)**2) + 0.5 * (D_o * θD_o + d_o * θd_o)

    C_c = D_c + d_c
    θ_c = (pi + math.sin(math.radians(2) ** -1)) * ((D_c + d_c) / (2 * C_c))
    L_c = sp.sqrt(4 * C_c**2 - (D_c + d_c)**2) + 0.5 * (D_c + d_c) * θ_c

    open_values_1 = {
        **open_values_1,
        "C_o": ["C_o", C_o, ''],
        "θD_o": ["θD_o", θD_o, ''],
        "θd_o": ["θd_o", θd_o, ''],
        "L_o": ["L_o", L_o, ''],
    }

    close_values_1 = {
        **close_values_1,
        "C_c": ["C_c", C_c, ''],
        "θ_c": ["θ_c", θ_c, ''],
        "L_c": ["L_c", L_c, ''],
    }

    create_table(frame, open_values_1, 0, 1, [5, 90, 52, 140])
    create_table(frame, close_values_1, 0, 2, [5, 90, 52, 140])


def calc_sixth(frame):
    global corrente_values_1

    third_section = {
      **variables_dict["section_6"]["gear"], 
    }

    seted_values = [] # tuplas para setar os valores definidos pelo usuario

    for var_name in third_section: # armazena os valores definidos pelo usuario
       define_values(third_section[var_name], seted_values, {}, corrente_values_1, {})

    N_c = corrente_values_1["N_c"][1]
    p_c = corrente_values_1["p_c"][1]
    vr_c = corrente_values_1["vr_c"][1]
    Dr_c = corrente_values_1["Dr_c"][1]

    v_c = (p_c * vr_c * N_c / 12) * 0.00508
    y = 360 / N_c
    d_c = math.cos(math.radians(Dr_c) * (y / 2))
    vmin_c = (pi * d_c * vr_c) / 12
    vmax_c = (pi * Dr_c * vr_c) / 12
    Δv_c = (vmax_c - vmin_c) / v_c

    corrente_values_1 = {
        **corrente_values_1,
        "v_c": ["v", v_c, ''],
        "vmin_c": ["vmin", vmin_c, ''],
        "vmax_c": ["vmax", vmax_c, ''],
        "Δv_c": ["Δv", Δv_c, ''],
        "d_c": ["d", d_c, ''],
        "y": ["y", y, ''],
    }

    create_table(frame, corrente_values_1, 0, 1, [5, 90, 52, 140])

