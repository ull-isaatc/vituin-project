# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_infraestructuras_generales/infraestructuras.xlsx"
sheet = 0
name_index = "index_aeropuertos"
type_index = "structured"

name_items = {
    "type_rows" : "place_origin",
    "type_cols" : "year_month"
}



table_start_and_end = {
    "start_row": 256,
    "start_col": 0,
    "end_row": 269,
    "end_col": 106,
    "start_value_row": 257,
    "start_value_col": 1
}
type_value = int

attributes_to_fixed={
    "airport": "Tenerife (ambos)"
}

field_region = ['place_origin']

fields_to_change = {'TOTAL AEROPUERTOS DE ORIGEN' : 'Canarias'}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed, field_region = fields_to_change, fields_to_change = fields_to_change)
