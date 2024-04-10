import dearpygui.dearpygui as dpg
from jinja2 import Template
import json
from dataclasses import dataclass

dpg.create_context()

# MODEL

@dataclass
class Model:
    name : str
    template : str
    variables : dict

@dataclass
class Program:
    models : list[Model]


# A global variable defining the current program being worked on
prgrm = Program(models=[])

# LOGIC

def render_data():
    "render the template using the data"
    plate = Template(dpg.get_value("model_template"))
    data = json.loads(dpg.get_value("model_data"))
    dpg.set_value("output", plate.render(data))

def add_model():
    global prgrm
    mdl = Model(name=dpg.get_value("model_name"), template=dpg.get_value("model_template"), variables=json.loads(dpg.get_value("model_data")))
    dpg.set_value("model_name", "")
    dpg.set_value("model_template", "")
    dpg.set_value("model_data", "")
    prgrm.models.append(mdl)
    load_models()

# GUI


with dpg.window(tag="Primary Window"):
    with dpg.tab_bar():
        with dpg.tab(label="Models"):
            dpg.add_input_text(tag="model_name", label="model name")
            dpg.add_text("Template")
            dpg.add_input_text(tag="model_template", height=200, multiline=True)

            dpg.add_text("Data")
            dpg.add_input_text(tag="model_data", height=200, multiline=True)

            dpg.add_table(tag="models_list")

    dpg.add_button(label="Add", callback=add_model)
    dpg.add_button(label="Run", callback=render_data)

    dpg.add_text("Output")
    dpg.add_input_text(tag="output", height=200, multiline=True)


def load_models():
    dpg.delete_item("models_list", children_only=True)

    # load the columns
    dpg.add_table_column(label="Name", parent="models_list")
    # reload the values
    for model in prgrm.models:
        with dpg.table_row(parent="models_list"):
            dpg.add_text(model.name, user_data=model.name)


# after displaying the whole GUI how I think it is supposed to be let's load the different tables
load_models()

dpg.create_viewport(title='Blueprint template', width=800, height=640)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()