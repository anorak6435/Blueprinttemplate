import dearpygui.dearpygui as dpg
from jinja2 import Template
import json

dpg.create_context()

# LOGIC

def render_data():
    "render the template using the data"
    plate = Template(dpg.get_value("template"))
    data = json.loads(dpg.get_value("data"))
    dpg.set_value("output", plate.render(data))




# GUI


with dpg.window(tag="Primary Window"):
    dpg.add_text("Template")
    dpg.add_input_text(tag="template", height=200, multiline=True)

    dpg.add_text("Data")
    dpg.add_input_text(tag="data", height=200, multiline=True)

    dpg.add_button(label="Run", callback=render_data)

    dpg.add_text("Output")
    dpg.add_input_text(tag="output", height=200, multiline=True)


dpg.create_viewport(title='Blueprint template', width=800, height=640)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()