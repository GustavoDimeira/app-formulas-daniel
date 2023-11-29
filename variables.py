import sympy as sp

variables_g_1 = sp.symbols("Pc_g Pb_g Pd_g N_g d_g m_g")
variables_p_1 = sp.symbols("Pc_p Pb_p Pd_p N_p d_p m_p")

variables_g_2 = sp.symbols("F_g J_g Qv_g Vt_g tr_g rpm_g pot_g mat_g mover_g moveabel_g")
variables_p_2 = sp.symbols("F_p J_p Qv_p Vt_p tr_p rpm_p pot_p mat_p mover_p moveabel_p")

variables_g_3 = sp.symbols("T_g N_cicle_g Sfb_linha__g Kr_g hb_g")
variables_p_3 = sp.symbols("T_p N_cicle_p Sfb_linha__p Kr_p hb_p")

variables_a_1 = sp.symbols("Fi_a Fc_a Fi_linha_a Fl_a D_a w_a v_a T_a")
variables_f_1 = sp.symbols("Fi_f Fc_f Fi_linha_f Fl_f D_f w_f v_f T_f")

variables_o_1 = sp.symbols("D_o d_o")
variables_c_1 = sp.symbols("D_c d_c")

variables_co_1 = sp.symbols("N_c p_c vr_c Dr_c")

Pc_g, Pb_g, Pd_g, N_g, d_g, m_g = variables_g_1
Pc_p, Pb_p, Pd_p, N_p, d_p, m_p = variables_p_1

F_g, J_g, Qv_g, Vt_g, tr_g, rpm_g, pot_g, mat_g, mover_g, moveabel_g = variables_g_2
F_p, J_p, Qv_p, Vt_p, tr_p, rpm_p, pot_p, mat_p, mover_p, moveabel_p = variables_p_2

T_g, N_cicle_g, Sfb_linha__g, Kr_g, hb_g = variables_g_3
T_p, N_cicle_p, Sfb_linha__p, Kr_p, hb_p = variables_p_3

Fi_a, Fc_a, Fi_linha_a, Fl_a, D_a, w_a, v_a, T_a = variables_a_1
Fi_f, Fc_f, Fi_linha_f, Fl_f, D_f, w_f, v_f, T_f = variables_f_1

D_o, d_o = variables_o_1
D_c, d_c = variables_c_1

N_c, p_c, vr_c, Dr_c = variables_co_1

θ = "θ"
theeth_pos = "theeth_pos"

variables_dict = {
    "section_1": {
        "gear": {
            "Pc_g": {
                "var": Pc_g,
                "type": "label",
            },
            "Pb_g": {
                "var": Pb_g,
                "type": "label",
            },
            "Pd_g": {
                "var": Pd_g,
                "type": "label",
            },
            "N_g": {
                "var": N_g,
                "type": "label",
            },
            "d_g": {
                "var": d_g,
                "type": "label",
            },
            "m_g": {
                "var": m_g,
                "type": "label",
            },
        },
        "pinion": {
            "Pc_p": {
                "var": Pc_p,
                "type": "label",
            },
            "Pb_p": {
                "var": Pb_p,
                "type": "label",
            },
            "Pd_p": {
                "var": Pd_p,
                "type": "label",
            },
            "N_p": {
                "var": N_p,
                "type": "label",
            },
            "d_p": {
                "var": d_p,
                "type": "label",
            },
            "m_p": {
                "var": m_p,
                "type": "label",
            },
        },
        "mutual": {
            "θ": {
                "var": θ,
                "type": "select",
                "options": ["20º", "25°"]
            },
        }
    },
    "section_2": {
        "gear": {
            "F_g": {
                "var": F_g,
                "type": "label",
            },
            "J_g": {
                "var": J_g,
                "type": "label",
            },
            "Qv_g": {
                "var": Qv_g,
                "type": "label",
            },
            "Vt_g": {
                "var": Vt_g,
                "type": "label",
            },
            "tr_g": {
                "var": tr_g,
                "type": "label",
            },
            "rpm_g": {
                "var": rpm_g,
                "type": "label",
            },
            "pot_g": {
                "var": pot_g,
                "type": "label",
            },
            "mat_g": {
                "var": mat_g,
                "type": "select",
                "options": ["Aço", "Ferro maleável", "Ferro nodular", "Ferro fundido", "Alumínio bronze", "Estanho bronze"]
            },
            "mover_g": {
                "var": mover_g,
                "type": "select",
                "options": ["Uniforme", "Choque Leve", "choque Moderado"]
            },
            "moveabel_g": {
                "var": moveabel_g,
                "type": "select",
                "options": ["Uniforme", "choque Moderado",  "Choque Severo"]
            },
        },
        "pinion": {
            "F_p": {
                "var": F_p,
                "type": "label",
            },
            "J_p": {
                "var": J_p,
                "type": "label",
            },
            "Qv_p": {
                "var": Qv_p,
                "type": "label",
            },
            "Vt_p": {
                "var": Vt_p,
                "type": "label",
            },
            "tr_p": {
                "var": tr_p,
                "type": "label",
            },
            "rpm_p": {
                "var": rpm_p,
                "type": "label",
            },
            "pot_p": {
                "var": pot_p,
                "type": "label",
            },
            "mat_p": {
                "var": mat_p,
                "type": "select",
                "options": ["Aço", "Ferro maleável", "Ferro nodular", "Ferro fundido", "Alumínio bronze", "Estanho bronze"]
            },
            "mover_p": {
                "var": mover_p,
                "type": "select",
                "options": ["Uniforme", "Choque Leve", "choque Moderado"]
            },
            "moveabel_p": {
                "var": moveabel_p,
                "type": "select",
                "options": ["Uniforme", "choque Moderado",  "Choque Severo"]
            },
        },
        "mutual": {
            "theeth_pos": {
                "var": theeth_pos,
                "type": "select",
                "options": ["Interno", "Externo"]
            },
        }
    },
    "section_3": {
        "gear": {
            "T_g": {
                "var": T_g,
                "type": "label",
            },
            "N_cicle_g": {
                "var": N_cicle_g,
                "type": "label",
            },
            "Sfb_linha__g": {
                "var": Sfb_linha__g,
                "type": "label",
            },
            "Kr_g": {
                "var": Kr_g,
                "type": "select",
                "options": ["90%", "99%", "99,9%", "99,99%"]
            },
            "hb_g": {
                "var": hb_g,
                "type": "select",
                "options": [160, 250, 400]
            }
        },
        "pinion": {
            "T_p": {
                "var": T_p,
                "type": "label",
            },
            "N_cicle_p": {
                "var": N_cicle_p,
                "type": "label",
            },
            "Sfb_linha__p": {
                "var": Sfb_linha__p,
                "type": "label",
            },
            "Kr_p": {
                "var": Kr_p,
                "type": "select",
                "options": ["90%", "99%", "99,9%", "99,99%"]
            },
            "hb_p": {
                "var": hb_p,
                "type": "select",
                "options": [160, 250, 400]
            }
        },
        "mutual": {}
    },
    "section_4": {
      "gear": {
        "Fi_a": {
            "var": Fi_a,
            "type": "label"
        },
        "D_a": {
            "var": D_a,
            "type": "label"
        },
        "w_a": {
            "var": w_a,
            "type": "label"
        },
        "v_a": {
            "var": v_a,
            "type": "label"
        },
        "T_a": {
            "var": T_a,
            "type": "label"
        }
      },
      "pinion": {
        "Fi_f": {
            "var": Fi_f,
            "type": "label"
        },
        "D_f": {
            "var": D_f,
            "type": "label"
        },
        "w_f": {
            "var": w_f,
            "type": "label"
        },
        "v_f": {
            "var": v_f,
            "type": "label"
        },
        "T_f": {
            "var": T_f,
            "type": "label"
        }
      },
      "mutual": {},
    },
    "section_5": {
      "gear": {
        "D_o": {
            "var": D_o,
            "type": "label",
        },
        "d_o": {
            "var": d_o,
            "type": "label",
        },
      },
      "pinion": {
        "D_c": {
            "var": D_c,
            "type": "label",
        },
        "d_c": {
            "var": d_c,
            "type": "label",
        },
      },
      "mutual": {}
    },
    "section_6": {
      "pinion": {},
      "gear": {
        "N_c": {
            "var": N_c,
            "type": "label"
        },
        "p_c": {
            "var": p_c,
            "type": "label"
        },
        "vr_c": {
            "var": vr_c,
            "type": "label"
        },
        "Dr_c": {
          "var": Dr_c,
          "type": "label"
        },
      },
      "mutual": {},
    },
}
