# -*- coding: utf-8 -*-
import sys
sys.path.append('../')


from get_elastic import general_functions

excel = "excels_holiday_rent/airbnb.xls"

sheets_and_indexes  = {'0':["index_list_homes_airbnb", "index_list_description_airbnb"]}
types_index = {'0':["unstructured", "unstructured"]}

main_field = "id_airbnb"
name_items = {"index_list_homes_airbnb":["id_airbnb","name","lat", "lng", "place", "url", "upload_date"], "index_list_description_airbnb":["price"]}
name_excel = "airbnb"

restriction = {'place':'Puerto de la Cruz'}


general_functions.write_excel(sheets_and_indexes, types_index, name_items, name_excel, main_field=main_field, restriction = restriction)
