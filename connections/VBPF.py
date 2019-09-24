#!/usr/bin/env python
# coding: utf-8

import nbnorms.norms.SP16_13330_2017_Rev01 as sp

import nbnorms.service.validation as valid

import math
def check(input, printIndex = 1) :

    Yn = input['Yn']

    Yc = input['Yc']

    steelGrade = input['steel']

    w = input['w']

    t1 = input['t1']

    t2 = input['t2']

    dp = input['dp']

    tp = input['tp']

    Lw = input['Lw']

    Kf = input['Kf']

    a = input['a']

    b = input['b']

    c = input['c']

    d = input['d']

    n = input['n']

    m = input['m']

    db = input['db']

    dh = input['dh']

    countOfShearPlanes = input['countOfShearPlanes']

    mu = input['mu']

    Yh = input['Yh']
    if printIndex > 0 : print('Yn = ', "{:.1f}".format(Yn))
    if printIndex > 0 : print('Yc = ', "{:.1f}".format(Yc))
    if printIndex > 0 : print('Марка стали - ', steelGrade)
    if printIndex > 0 : print('w = ', "{:.1f}".format(w))
    if printIndex > 0 : print('t1 = ', "{:.1f}".format(t1))
    if printIndex > 0 : print('t2 = ', "{:.1f}".format(t2))
    if printIndex > 0 : print('dp = ', "{:.1f}".format(dp))
    if printIndex > 0 : print('tp = ', "{:.1f}".format(tp))
    Lw =  Lw - 10

    if printIndex > 0 : print('Lw = ', "{:.1f}".format(Lw))
    if printIndex > 0 : print('Kf = ', "{:.1f}".format(Kf))
    table_C3 = sp.t_C3({'grade' : steelGrade, 'thickness': t1}, printIndex - 1)


    Kf_min = sp.t_38({ **{

        'TYPE' : 'T2',

        'WELDING' : 'SEMI-AUTO',

        't' : max(tp, t1)

    }, **table_C3}, 0)['Kf'] # mm


    if printIndex > 0 : print('Kf_min = ', "{:.1f}".format(Kf_min))
    if printIndex > 0 : valid.bool(Kf >= Kf_min)
    if printIndex > 0 : valid.bool(Kf <= 1.2 * min(t1, tp))
    if printIndex > 0 : valid.bool(Lw >= max(40, 4*Kf))

    

    isWeldOk = (Kf >= Kf_min)  and (Kf <= 1.2 * min(t1, tp)) and (Lw >= max(40, 4*Kf))
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
    if printIndex > 0 : print('mu = ',  "{:.2f}".format(mu))
    if printIndex > 0 : print('Yh = ',  "{:.2f}".format(Yh))
    if printIndex > 0 : valid.bool((b >= 2.5 * dh or n <= 1) and (d >= 2.5*dh or m <= 1))
    if printIndex > 0 : valid.bool(a >= 1.3*dh and c >= 1.3*dh)

    isBoltsOk = ((b >= 2.5 * dh or n <= 1) and (d >= 2.5 * dh or m <= 1) and a >= 1.3*dh and c >= 1.3*dh)
    table_C3 = sp.t_C3({'grade' : steelGrade, 'thickness': t1}, printIndex - 1)
    table_C3['Ym'] = 1.025

    Ry = sp.t_2(table_C3, printIndex - 1)['Ry']
    A1 = t1 * w

    if printIndex > 0 : print("A1 = ", "{:.2f}".format(A1))
    N1 = A1 * Ry * Yc / Yn

    if printIndex > 0 : print("N1 = ", "{:.2f}".format(N1))
    table_C3 = sp.t_C3({'grade' : steelGrade, 'thickness': t2}, printIndex - 1)
    table_C3['Ym'] = 1.025

    Ry = sp.t_2(table_C3, printIndex - 1)['Ry']
    A2 = 2 * t2 * w

    if printIndex > 0 : print("A2 = ", "{:.2f}".format(A2))
    N2 = A2 * Ry * Yc / Yn

    if printIndex > 0 : print("N2 = ", "{:.2f}".format(N2))
    Rbun = sp.t_D8({'d' : db}, printIndex - 1)
    Rbh = sp.f_3(Rbun, printIndex - 1)
    countOfBolts = n * m

    if printIndex > 0 : print("countOfBolts = ", countOfBolts)
    Abn =  sp.t_D9({'d' : db}, printIndex - 1)
    Qbh = sp.f_191({**Rbh,  **Abn, **{'mu' : mu, 'Yh' : Yh}}, printIndex - 1)
    N3 = sp.f_192({**Qbh, **{

        'n' : countOfBolts,

        'Yc' : Yc,

        'k' : countOfShearPlanes

    }}, printIndex - 1)['N'] / Yn


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
    N5 = A5 * Ry * Yc / Yn

    if printIndex > 0 : print("N5 = ", "{:.2f}".format(N5))
    return {'N1' : N1, 'N2' : N2, 'N3' : N3, 'N4' : N4, 'N5' : N5, 'isWeldOk' : isWeldOk, 'isBoltsOk' : isBoltsOk}
