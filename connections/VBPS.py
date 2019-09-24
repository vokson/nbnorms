#!/usr/bin/env python
# coding: utf-8

import nbnorms.norms.SP16_13330_2017_Rev01 as sp

import nbnorms.service.validation as valid

import math
def check(input, printIndex = 1) :

    Yn = input['Yn']

    Yc = input['Yc']

    steelGrade = input['steel']

    countOfShearPlanes = input['countOfShearPlanes']

    dp = input['dp']

    tp = input['tp']

    w = input['w']

    t = input['t']

    h = input['h']

    tr = input['tr']

    Lw = input['Lw']

    Kf = input['Kf']

    a = input['a']

    b = input['b']

    c = input['c']

    d = input['d']

    m = input['m']

    n = input['n']

    db = input['db']

    dh = input['dh']

    strengthClass = input['strengthClass']

    precisionClass = input['precisionClass']
    if printIndex > 0 : print('Yn = ', "{:.1f}".format(Yn))
    if printIndex > 0 :

        print('Yс = ', "{:.1f}".format(Yc))
    if printIndex > 0 : print('Марка стали - ', steelGrade)
    if printIndex > 0 : print('w = ', "{:.1f}".format(w))
    if printIndex > 0 :

        print('t = ', "{:.1f}".format(t))
    if printIndex > 0 : print('h = ', "{:.1f}".format(h))
    if printIndex > 0 : print('tr = ', "{:.1f}".format(tr))
    if printIndex > 0 : print('dp = ', "{:.1f}".format(dp))
    if printIndex > 0 : print('tp = ', "{:.1f}".format(tp))
    Lw =  Lw - 10

    if printIndex > 0 : print('Lw = ', "{:.1f}".format(Lw))
    if printIndex > 0 : print('Kf = ', "{:.1f}".format(Kf))
    table_C3 = sp.t_C3({'grade' : steelGrade, 'thickness': t}, printIndex - 1)


    Kf_min = sp.t_38({ **{

        'TYPE' : 'T2',

        'WELDING' : 'SEMI-AUTO',

        't' : max(tp, t)

    }, **table_C3}, 0)['Kf'] # mm


    if printIndex > 0 : print('Kf_min = ', "{:.1f}".format(Kf_min))
    if printIndex > 0 : valid.bool(Kf >= Kf_min)
    if printIndex > 0 : valid.bool(Kf <= 1.2 * min(t, tp))
    if printIndex > 0 : valid.bool(Lw >= max(40, 4*Kf))

    

    isWeldOk = (Kf >= Kf_min)  and (Kf <= 1.2 * min(t, tp)) and (Lw >= max(40, 4*Kf))
    beta = sp.t_39({

        'd' : 2,

        'Kf' : Kf,

        'WELDING' : 'SEMI-AUTO',

        'LOCATION' : 'BOTTOM'

    }, printIndex - 1)
    Rwun = 490 # МПа

    Rwf = 215 # МПа

    Rwz = 0.45 * Rwun # МПа

    

    if printIndex > 0 : print('Rwz = ',  "{:.2f}".format(Rwz))
    if printIndex > 0 : print('a = ',  a)
    if printIndex > 0 : print('b = ',  b)
    if printIndex > 0 : print('n = ',  n)
    if printIndex > 0 : print('c = ',  c)
    if printIndex > 0 : print('d = ',  d)
    if printIndex > 0 : print('m = ',  m)
    if printIndex > 0 : print('db = ',  db)
    if printIndex > 0 : print('dh = ',  dh)
    if printIndex > 0 : print('countOfShearPlanes = ',  countOfShearPlanes)
    if printIndex > 0 : valid.bool((b >= 2.5 * dh or n <= 1) and (m <= 1 or (d >= 2.5 * dh and m > 2) or (2 * d >= 2.5 * dh and m == 2)))
    if printIndex > 0 : valid.bool(a >= 2*dh and c >= 1.5*dh)

        

    isBoltsOk = (b >= 2.5 * dh or n <= 1) and (m <= 1 or (d >= 2.5 * dh and m > 2) or (2 * d >= 2.5 * dh and m == 2)) and (a >= 2*dh) and (c >= 1.5*dh)
    table_C3 = sp.t_C3({'grade' : steelGrade, 'thickness': t}, printIndex - 1)
    table_C3['Ym'] = 1.025

    table_2 = sp.t_2(table_C3, printIndex - 1)

    Ry = table_2['Ry']
    A1 = t * (w - m * dh) + tr * h

    if printIndex > 0 : print("A1 = ", "{:.2f}".format(A1))
    x1 = (tr * h ** 2 / 2 - (w - m * dh) * t ** 2 / 2) / A1

    if printIndex > 0 : print("x1 = ", "{:.2f}".format(x1))
    Y1 = tr * h ** 3 / 12 + tr * h * (h/2 - x1) ** 2 + (w - m * dh) * t ** 3 / 12 + (w - m * dh) * t * (x1 + t/2) ** 2

    if printIndex > 0 : print("Y1 = ", "{:.2f}".format(Y1))
    W1 = Y1 / max(t + x1, h - x1)

    if printIndex > 0 : print("W1 = ", "{:.2f}".format(W1))
    N1 = Ry / (1 / A1 + (1.5 * t + x1) / W1) / Yn / Yc

    if printIndex > 0 : print("N1 = ", "{:.2f}".format(N1))
    table_D5 = sp.t_D5({'strengthClass' : strengthClass}, printIndex - 1)
    table_5 = sp.t_5({**table_D5, **table_2, **{'strengthClass' : strengthClass, 'precisionClass' : precisionClass}}, printIndex - 1)
    countOfBolts = n * m

    if printIndex > 0 : print("countOfBolts = ", countOfBolts)
    Ab =  sp.t_D9({'d' : db}, printIndex - 1)
    table_41 = sp.t_41({

        **{

            'count' : n,

            'precisionClass' : precisionClass,

            'stress' : 'SHEAR',

            'a' : a,

            's' : b,

            'd' : dh

        },

        **table_C3

    }, printIndex - 1)
    Nbs = sp.f_186({**table_5,  **table_41, **Ab, **{'ns' : countOfShearPlanes, 'Yc' : Yc}}, printIndex - 1)
    table_41 = sp.t_41({

        **{

            'count' : n,

            'precisionClass' : precisionClass,

            'stress' : 'COMPRESSION',

            'a' : a,

            's' : b,

            'd' : dh

        },

        **table_C3

    }, printIndex - 1)
    Nbp = sp.f_187({**table_5,  **table_41, **{'t' : t, 'db' : db, 'Yc' : Yc}}, printIndex - 1)
    N2 = countOfBolts * Nbs['Nbs'] / Yn

    if printIndex > 0 : print("N2 = ", "{:.2f}".format(N2))
    N3 = countOfBolts * Nbp['Nbp'] / Yn

    if printIndex > 0 : print("N3 = ", "{:.2f}".format(N3))
    N4f = sp.f_176({ **{

        'Kf' : Kf,

        'Lw' : Lw,

        'Yc' : Yc,

        'Rwf' : Rwf

    }, **beta}, printIndex - 1)['N']
    N4z = sp.f_177({ **{

        'Kf' : Kf,

        'Lw' : Lw,

        'Yc' : Yc,

        'Rwz' : Rwz

    }, **beta}, printIndex - 1)['N']
    N4 = 4 * min(N4f, N4z) / Yn

    if printIndex > 0 : print("N4 = ", "{:.2f}".format(N4))
    table_C3 = sp.t_C3({'grade' : steelGrade, 'thickness': tp}, printIndex - 1)
    table_C3['Ym'] = 1.025

    Ry = sp.t_2(table_C3, printIndex - 1)['Ry']
    A5 = dp ** 2 - (dp - 2 * tp) ** 2

    if printIndex > 0 : print("A5 = ", "{:.2f}".format(A5))
    N5 = A5 * Ry / Yn / Yc

    if printIndex > 0 : print("N5 = ", "{:.2f}".format(N5))
    return {'N1' : N1, 'N2' : N2, 'N3' : N3, 'N4' : N4, 'N5' : N5, 'isWeldOk' : isWeldOk, 'isBoltsOk' : isBoltsOk}
