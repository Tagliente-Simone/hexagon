from Asymm.Asymm import AsymHex
from Asymm.RotatedAsymm import RotatedAsymHex
from Hexagon.Dimensions import calculate_hexagon_dimensions as cd
from Hexagon.Hexagon import Hexagon
from Trapeze.Dimensions import calculate_trapeze_dimensions as cd1
from Asymm.Dimensions import calculate_asymHex_dimensions as cd2

from Hexagon.Draw import draw_hexagons as draw_hexs
from Trapeze.Draw import draw_trapezes as draw_traps
from Asymm.Draw import draw_asymHex as draw_asymHexs

from Configuration.Configuration import Configuration

import csv
import pandas as pd
from Trapeze.Trapeze import Trapeze
import db_services as db
import sys
import os
import shutil
import json

def empty_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

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
            save_on_csv_hex(hexagons, "_attuale", dest, din, length, weight, actual_compo, single*total, uuid, "0")
    
    return single*total

def hexagon_test(weight, dest, din, length, total_actual_hexagon):
        max_found = 0;
        best_compo = ""

        if float(dest)  <= 40:
            compo_list = ["5-6-7-8-7-6-5", "6-7-8-9-8-7-6", "4-5-6-5-4"]
        elif float(dest)  > 40 and float(dest)  <= 50:
            compo_list = ["6-7-8-9-8-7-6", "5-6-7-8-7-6-5", "4-5-6-5-4"]
        elif float(dest)  > 50 and float(dest)  <= 70:
            compo_list = ["3-4-5-4-3", "4-5-6-5-4", "4-5-6-7-6-5-4", "5-6-7-8-7-6-5"]
        elif float(dest)  > 70:
            compo_list = ["3-4-5-4-3", "3-4-3"]

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
    if isinstance(trapezes[0], Trapeze):
        ordered_trapezes = sorted(trapezes, key=lambda x: (x.origin_y, x.origin_x), reverse=True)
    else:
        ordered_trapezes = sorted(trapezes, key=lambda x: (x.origin_y, x.origin_x), reverse=True)
    with open(str(int(dest)) + 'coordinate_trapezi.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['d_int', 'd_est', 'lunghezza', 'peso_uni', 'ascissa', 'ordinata', 'composizione_fascio', 'num_pezzi_strato', 'forma_fascio', 'uuid', 'altezza_max', 'rotazione'])

        for trapeze in ordered_trapezes:
            if isinstance(trapeze, Trapeze):
                rotazione_rilascio = 90;
                trapeze.origin_x, trapeze.origin_y = trapeze.origin_y, trapeze.origin_x
            else:
                rotazione_rilascio = 0;
            rotazione_totale = trapeze.angle + rotazione_rilascio
            writer.writerow([din, dest, length, weight, int(round(trapeze.origin_y - config.start_originy)), int(round(trapeze.origin_x - config.start_originx)), compo, total, 'trapezio', uuid, hmax, rotazione_totale])
        
    read_dataframe(str(int(dest)) + 'coordinate_trapezi.csv')


def save_on_csv_hex(hexagons, actual, dest, din, length, weight, compo, total, uuid, hmax):
    if isinstance(hexagons[0], Hexagon) or isinstance(hexagons[0], RotatedAsymHex):
        ordered_hexagons = sorted(hexagons, key=lambda x: (x.origin_x, x.origin_y), reverse=True)
    else:
        ordered_hexagons = sorted(hexagons, key=lambda x: (x.origin_y, x.origin_x), reverse=True)
    with open(str(int(dest)) + 'coordinate_esagoni' + actual + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['d_int', 'd_est', 'lunghezza', 'peso_uni', 'ascissa', 'ordinata', 'composizione_fascio', 'num_pezzi_strato', 'forma_fascio', 'uuid', 'altezza_max', 'rotazione'])

        for hexagon in ordered_hexagons:
            if isinstance(hexagon, Hexagon) or isinstance(hexagon, RotatedAsymHex):
                rotazione_rilascio = 0;
            else:
                rotazione_rilascio = 90;
                hexagon.origin_x, hexagon.origin_y = hexagon.origin_y, hexagon.origin_x
            rotazione_totale = hexagon.angle + rotazione_rilascio
            writer.writerow([din, dest, length, weight, int(round(hexagon.origin_y - config.start_originy)), int(round(hexagon.origin_x - config.start_originx)), compo, total, 'esagono' + actual, uuid, hmax, rotazione_totale])
        
    read_dataframe(str(int(dest)) + 'coordinate_esagoni' + actual + '.csv')



def read_dataframe(csv_file):

    df = pd.read_csv(csv_file)
    print(df)
    #db.test_insert(df)






empty_folder('./images')

parameter_list = parameter_value.split(',')

diameter_in = float(parameter_list[0])
diameter_out = float(parameter_list[1])
length = float(parameter_list[2])

weight = float(parameter_list[3])

################################################################################################################################################
## MODIFICARE LA RIGA 202 e 203 per il calcolo dell'altezza e larghezza massima in eccesso
exceed_height = 1070 + (3/4 * diameter_out)
exceed_width = 1230 + (2/3 * diameter_out)
################################################################################################################################################



config = Configuration(exceed_width, exceed_height, inter=3, uuid_length=100, images_path="./images/")


#db.db_connect()

if(len(parameter_list) > 6):
    actual_compo = parameter_list[6]
    total_actual_hexagon = actual_hexagon_test(weight, diameter_out, diameter_in, length, actual_compo)
else:
    total_actual_hexagon = -1

total_hexagon = hexagon_test(weight, diameter_out, diameter_in, length, total_actual_hexagon)
total_trapezoid = trapezoid_test(weight, diameter_out, diameter_in, length, total_actual_hexagon)
total_asym_hexagon = asym_hexagon_test(weight, diameter_out, diameter_in, length, total_actual_hexagon)