from variables import variables_dict
from tkinter import ttk

from calc_functions import calc_first, calc_second, calc_third

sections_infos = [
  {
    "calc_function": calc_first,
  },
  {
    "calc_function": calc_second,
  },
  {
    "calc_function": calc_third,
  },
]

def create_entry(crr_row, var_name, frame, section, crr_sub_section):
  label = ttk.Label(frame, text=f"{var_name}:")
  label.grid(row= crr_row, column= 0, padx= 10, pady= 10)

  input = ttk.Entry(frame)
  input.grid(row= crr_row, column= 1, padx= 10, pady= 10)

  variables_dict[section][crr_sub_section][var_name].append(input)


def create_options(crr_row, var_name, frame, options, section, crr_sub_section):
  label = ttk.Label(frame, text=f"{var_name}:")
  label.grid(row= crr_row, column= 0, padx= 10, pady= 10)
  
  combobox = ttk.Combobox(frame, textvariable=var_name, values=options)
  combobox.grid(row= crr_row, column= 1, padx= 10, pady= 10)

  variables_dict[section][crr_sub_section][var_name].append(input)


def create_sections(root):
  for section in variables_dict:
    crr_section = variables_dict[section]
    crr_row = 0

    frame_global = ttk.Frame(root)
    frame_global.grid()

    frame_gear = ttk.Frame(frame_global)
    frame_gear.grid(padx= 10, pady= 10)

    frame_pinion = ttk.Frame(frame_global)
    frame_pinion.grid(padx= 10, pady= 10)

    for var in [*crr_section["gear"], *crr_section["pinion"], *crr_section["mutual"]]:
      is_gear = crr_row < len(crr_section["gear"])
      is_pinion = crr_row <= len(crr_section["gear"])  * 2 - 1
      
      crr_sub_section = "gear" if is_gear else"pinion" if is_pinion else "mutual"
      crr_frame = frame_gear if is_gear else frame_pinion if is_pinion else frame_global

      var_infos = crr_section[crr_sub_section][var]

      if (var_infos[1] == "label"):
        create_entry(crr_row, var, crr_frame, section, crr_sub_section)
      else:
        create_options(crr_row, var, crr_frame, var_infos[2], section, crr_sub_section)

      crr_row += 1

    section_index = int(section.split("_")[1]) - 1
    calc_btn = ttk.Button(
      frame_global, text="Calcular", command=sections_infos[section_index]["calc_function"]
    )
    calc_btn.grid(columnspan=2)
