from Hexagon.Dimensions import calculate_hexagon_dimensions as cd
from Trapeze.Dimensions import calculate_trapeze_dimensions as cd1
from Asymm.Dimensions import calculate_asymHex_dimensions as cd2

from Hexagon.Draw import draw_hexagons as draw_hexs
from Trapeze.Draw import draw_trapezes as draw_traps
from Asymm.Draw import draw_asymHex as draw_asymHexs

from Configuration.Configuration import Configuration

import csv
import pandas as pd
import db_services as db
import sys

def actual_hexagon_test(weight, dest, din, length, actual_compo):

    rows_array = [float(i) for i in actual_compo.split('-')]
    if(len(rows_array) % 2 == 1):
            n_rows = len(rows_array)
            radius = float(dest)
            radius = radius / 2
            #Call the function to calculate the dimension of the hexagon
            hexagons = cd(radius, n_rows, rows_array, 9999, config)
            total = len(hexagons)
            single = sum([int(i) for i in actual_compo.split('-')])
            uuid = draw_hexs(hexagons, True, config)
            save_on_csv_hex(hexagons, "_attuale", dest, din, length, weight, actual_compo, single*total, uuid)
    
    return single*total

def hexagon_test(weight, dest, din, length, total_actual_hexagon):
        max_found = 0;
        best_compo = ""

        if float(dest)  <= 40:
            compo_list = ["5-6-7-8-7-6-5", "6-7-8-9-8-7-6", "4-5-6-5-4"]
        elif float(dest)  > 40 and float(dest)  <= 50:
            compo_list = ["6-7-8-9-8-7-6", "5-6-7-8-7-6-5", "4-5-6-5-4"]
        elif float(dest)  > 50 and float(dest)  <= 70:
            compo_list = ["3-4-5-4-3", "4-5-6-5-4"]
        elif float(dest)  > 70:
            compo_list = ["3-4-5-4-3"]

        for i in range(0, len(compo_list)):
            rows_array = [float(i) for i in compo_list[i].split('-')]
            if(len(rows_array) % 2 == 1):
                n_rows = len(rows_array)
                radius = float(dest)
                radius = radius / 2
                #Call the function to calculate the dimension of the hexagon
                hexagons = cd(radius, n_rows, rows_array, 9999, config)
                total = len(hexagons)
                single = sum([int(i) for i in compo_list[i].split('-')])
                total_tubes_1 =  single * total
                
                if single * weight < 25:
                    if total_tubes_1 > max_found:
                        max_found = total_tubes_1
                        best_compo = compo_list[i]
                        best_hex = hexagons

        uuid = draw_hexs(best_hex, False, config)
        save_on_csv_hex(best_hex, "", dest, din, length, weight, best_compo, max_found, uuid, best_hex[0].hex_height)
        

        return max_found
    
def trapezoid_test(weight, dest, din, length, total_actual_hexagon):
    
    if float(dest)  <= 40:
        compos = ["8-7-6-5", "9-8-7-6"]
    elif float(dest)  > 40 and float(dest)  <= 50:
        compos = ["9-8-7-6", "8-7-6-5", "6-5-4"]
    elif float(dest)  > 50 and float(dest)  <= 70:
        compos = ["5-4-3", "6-5-4"]
    elif float(dest)  > 70:
        compos = ["4-3"]
    
    max_found = 0
    
    
    for compo in compos:
        single = sum([int(i) for i in compo.split('-')])
        trapezes = cd1(float(dest)/2, compo, config)
        total = single * len(trapezes)
        if total > max_found:
            max_found = total
            best_compo = compo
            best_trapezes = trapezes

    uuid = draw_traps(best_trapezes, config)
    save_on_csv_trapezoid(best_trapezes, dest, din, length, weight, best_compo, max_found, uuid, trapezes[0].h_max)
    

    return max_found


def asym_hexagon_test(weight, dest, din, length, total_actual_hexagon):
    
    compos = ["3-4-5-4"]
    
    
    single = sum([int(i) for i in compos[0].split('-')])            
    hexs = cd2(float(dest)/2, compos[0], config)
    total = single * len(hexs)
    
    uuid = draw_asymHexs(hexs, False, config)
    save_on_csv_hex(hexs, "_asimmetrico", dest, din, length, weight, compos[0], total, uuid, hexs[0].h_max)

    return total

if len(sys.argv) > 1:
    parameter_value = sys.argv[1]
    print("Parameter:", parameter_value)
else:
    print("No parameter provided.")

def save_on_csv_trapezoid(trapezes, dest, din, length, weight, compo, total, uuid, hmax):

    with open(str(int(dest)) + 'coordinate_trapezi.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['d_int', 'd_est', 'lunghezza', 'peso_uni', 'ascissa', 'ordinata', 'composizione_fascio', 'num_pezzi_strato', 'forma_fascio', 'uuid', 'altezza_max'])

        for trapeze in trapezes:
            writer.writerow([din, dest, length, weight, int(round(trapeze.origin_x - config.start_originx)), int(round(trapeze.origin_y - config.start_originy)), compo, total, 'trapezio', uuid, hmax])
        
    read_dataframe(str(int(dest)) + 'coordinate_trapezi.csv')


def save_on_csv_hex(hexagons, actual, dest, din, length, weight, compo, total, uuid, hmax):
    with open(str(int(dest)) + 'coordinate_esagoni' + actual + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['d_int', 'd_est', 'lunghezza', 'peso_uni', 'ascissa', 'ordinata', 'composizione_fascio', 'num_pezzi_strato', 'forma_fascio', 'uuid', 'altezza_max'])

        for hexagon in hexagons:
            writer.writerow([din, dest, length, weight, int(round(hexagon.origin_x - config.start_originx)), int(round(hexagon.origin_y - config.start_originy)), compo, total, 'esagono' + actual, uuid, hmax])
        
    read_dataframe(str(int(dest)) + 'coordinate_esagoni' + actual + '.csv')



def read_dataframe(csv_file):

    df = pd.read_csv(csv_file)
    print(df)
    #db.test_insert(df)







parameter_list = parameter_value.split(',')

diameter_in = float(parameter_list[0])
diameter_out = float(parameter_list[1])
length = float(parameter_list[2])

weight = float(parameter_list[3])

# Corrected class name
config = Configuration(rect_width=1250, rect_height=1050, inter=3, uuid_length=100, images_path="./images/")


#db.db_connect()

if(len(parameter_list) > 6):
    actual_compo = parameter_list[6]
    total_actual_hexagon = actual_hexagon_test(weight, diameter_out, diameter_in, length, actual_compo)
else:
    total_actual_hexagon = -1

total_hexagon = hexagon_test(weight, diameter_out, diameter_in, length, total_actual_hexagon)
total_trapezoid = trapezoid_test(weight, diameter_out, diameter_in, length, total_actual_hexagon)
total_asym_hexagon = asym_hexagon_test(weight, diameter_out, diameter_in, length, total_actual_hexagon)