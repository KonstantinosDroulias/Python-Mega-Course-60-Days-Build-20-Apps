from traceback import extract_tb
import extractor_functions

import FreeSimpleGUI as sg

sg.theme("LightGrey1")

label_archive = sg.Text("Select archive:")
input_archive = sg.Input()
choose_archive_btn = sg.FileBrowse('Choose Archive', key="archive")

label_destination = sg.Text("Select dest dir:")
input_destination = sg.Input()
choose_destination_btn = sg.FileBrowse('Choose Destination', key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="white")

window = sg.Window("Archive Extractor",
                   layout=[[label_archive, input_archive, choose_archive_btn],
                           [label_destination, input_destination, choose_destination_btn],
                           [extract_button, output_label]])

while True:
    event, value = window.read()
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window['output'].update(value="Extraction Completed")

window.close()