import sympy as sp

variables_g_1 = sp.symbols("Pc_g Pb_g Pd_g N_g d_g m_g")
variables_p_1 = sp.symbols("Pc_p Pb_p Pd_p N_p d_p m_p")

variables_g_2 = sp.symbols("F_g J_g Qv_g Vt_g tr_g rpm_g pot_g")
variables_p_2 = sp.symbols("F_p J_p Qv_p Vt_p tr_p rpm_p pot_p")

variables_g_3 = sp.symbols("T_g N_cicle_g Sfb_linha__g")
variables_p_3 = sp.symbols("T_p N_cicle_p Sfb_linha__p")

(Pc_g, Pb_g, Pd_g, N_g, d_g, m_g) = variables_g_1
(Pc_p, Pb_p, Pd_p, N_p, d_p, m_p) = variables_p_1

(F_g, J_g, Qv_g, Vt_g, tr_g, rpm_g, pot_g) = variables_g_2
(F_p, J_p, Qv_p, Vt_p, tr_p, rpm_p, pot_p) = variables_p_2

(T_g, N_cicle_g, Sfb_linha__g) = variables_g_3
(T_p, N_cicle_p, Sfb_linha__p) = variables_p_3

θ = None
mat_1 = None
mat_2 = None
theeth_pos = None

variables_dict = {
  "section_1": {
    "gear": {
      "Pc_g": [Pc_g, "label", []],
      "Pb_g": [Pb_g, "label", []],
      "Pd_g": [Pd_g, "label", []],
      "N_g": [N_g, "label", []],
      "d_g": [d_g, "label", []],
      "m_g": [m_g, "label", []],
    },
    "pinion": {
      "Pc_p": [Pc_p, "label", []],
      "Pb_p": [Pb_p, "label", []],
      "Pd_p": [Pd_p, "label", []],
      "N_p": [N_p, "label", []],
      "d_p": [d_p, "label", []],
      "m_p": [m_p, "label", []],
    },
    "mutual": {
      "θ": [θ, "select", ["20º", "25°"]],
    }
  },
  "section_2": {
    "gear": {
      "F_g": [F_g, "label", []], 
      "J_g": [J_g, "label", []], 
      "Qv_g": [Qv_g, "label", []], 
      "Vt_g": [Vt_g, "label", []], 
      "tr_g": [tr_g, "label", []], 
      "rpm_g": [rpm_g, "label", []],
      "pot_g": [pot_g, "label", []],
      "mat_1": [mat_1, "select",
        ["Aço", "Ferro maleável", "Ferro nodular", "Ferro fundido", "Alumínio bronze", "Estanho bronze"]
      ],
    },
    "pinion": {
      "F_p": [F_p, "label", []],
      "J_p": [J_p, "label", []],
      "Qv_p": [Qv_p, "label", []],
      "Vt_p": [Vt_p, "label", []],
      "tr_p": [tr_p, "label", []],
      "rpm_p": [rpm_p, "label", []],
      "pot_p": [pot_p, "label", []],
      "mat_2": [mat_2, "select",
        ["Aço", "Ferro maleável", "Ferro nodular", "Ferro fundido", "Alumínio bronze", "Estanho bronze"]
      ],
    },
    "mutual": {
      "theeth_pos": [theeth_pos, "select", ["Interno", "Externo"]],
    }
  },
  "section_3": {
    "gear": {
      "T_g": [T_g, "label", []],
      "N_cicle_g": [N_cicle_g, "label", []],
      "Sfb_linha__g": [Sfb_linha__g, "label", []],
    },
    "pinion": {
      "T_p": [T_p, "label", []],
      "N_cicle_p": [N_cicle_p, "label", []],
      "Sfb_linha__p": [Sfb_linha__p, "label", []],
    },
    "mutual": []
  },
}
