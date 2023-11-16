import sympy as sp

variables_g_1 = sp.symbols("Pc_g Pb_g Pd_g N_g d_g m_g")
variables_p_1 = sp.symbols("Pc_p Pb_p Pd_p N_p d_p m_p")

variables_g_2 = sp.symbols("F_g J_g Qv_g Vt_g tr_g rpm_g pot_g")
variables_p_2 = sp.symbols("F_p J_p Qv_p Vt_p tr_p rpm_p pot_p")

variables_g_3 = sp.symbols("T_g N_cicle_g Sfb_linha__g")
variables_p_3 = sp.symbols("T_p N_cicle_p Sfb_linha__p")

Pc_g, Pb_g, Pd_g, N_g, d_g, m_g = variables_g_1
Pc_p, Pb_p, Pd_p, N_p, d_p, m_p = variables_p_1

F_g, J_g, Qv_g, Vt_g, tr_g, rpm_g, pot_g = variables_g_2
F_p, J_p, Qv_p, Vt_p, tr_p, rpm_p, pot_p = variables_p_2

T_g, N_cicle_g, Sfb_linha__g = variables_g_3
T_p, N_cicle_p, Sfb_linha__p = variables_p_3

θ = None
mat_g = None
mat_p = None
theeth_pos = None

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
        },
        "mutual": []
    },
}
