#!/usr/bin/env python
# coding: utf-8

# СП 16.13330.2017
# ====

# ### Формула 3

# $ R_{bh} = 0.7 * R_{bun}$

# In[1]:


def f_3(input, printIndex = 1):
    
    Rbun = input['Rbun']
    Rbh = 0.7 * Rbun
    
    if printIndex > 0 :
        print('Rbh = 0.7 * Rbun = ', "{:.2f}".format(Rbh))
    
    return {'Rbh' : Rbh}


# ### Формула 176

# $ N = \beta_{f} * K_{f} * L_{w} * R_{wf} * Y_{c}$

# In[2]:


def f_176(input, printIndex = 1):
    
    beta_f = input['beta_f']
    Kf = input['Kf']
    Lw =  input['Lw']
    Rwf =  input['Rwf']
    Yc =  input['Yc']
    
    N = beta_f * Kf * Lw * Rwf * Yc
    
    if printIndex > 0 :
        print('N = beta_f * Kf * Lw * Rwf * Yc = ', "{:.2f}".format(N))
    
    return {'N' : N}


# ### Формула 177

# $ N = \beta_{z} * K_{f} * L_{w} * R_{wz} * Y_{c}$

# In[3]:


def f_177(input, printIndex = 1):
    
    beta_z = input['beta_z']
    Kf = input['Kf']
    Lw =  input['Lw']
    Rwz =  input['Rwz']
    Yc =  input['Yc']
    
    N = beta_z * Kf * Lw * Rwz * Yc
    
    if printIndex > 0 :
        print('N = beta_z * Kf * Lw * Rwz * Yc = ', "{:.2f}".format(N))
    
    return {'N' : N}


# ### Формула 186

# $ N_{bs} = R_{bs} * A_{b} * n_{s} * Y_{b} * Y_{c}$

# In[6]:


def f_186(input, printIndex = 1):
    
    Rbs = input['Rbs']
    Ab = input['Ab']
    ns =  input['ns']
    Yb =  input['Yb']
    Yc =  input['Yc']
    
    Nbs= Rbs * Ab * ns * Yb * Yc
    
    if printIndex > 0 :
        print('Nbs =  Rbs * Ab * ns * Yb * Yc = ', "{:.2f}".format(Nbs))
    
    return {'Nbs' : Nbs}


# ### Формула 187

# $ N_{bp} = R_{bp} * d_{b} * \sum t * Y_{b} * Y_{c}$

# In[5]:


def f_187(input, printIndex = 1):
    
    Rbp = input['Rbp']
    db = input['db']
    t =  input['t']
    Yb =  input['Yb']
    Yc =  input['Yc']
    
    Nbp = Rbp * db * t * Yb * Yc
    
    if printIndex > 0 :
        print('Nbp =  Rbp * db * t * Yb * Yc = ', "{:.2f}".format(Nbp))
    
    return {'Nbp' : Nbp}


# ### Формула 191

# $ Q_{bh} = R_{bh} * A_{bn} * \mu  / \gamma_{h}$

# In[4]:


def f_191(input, printIndex = 1):
    
    Rbh = input['Rbh']
    Abn = input['Abn']
    mu =  input['mu']
    Yh =  input['Yh']
    
    Qbh = Rbh * Abn * mu / Yh
    
    if printIndex > 0 :
        print('Qbh = Rbh * Abn * mu / Yh = ', "{:.2f}".format(Qbh))
    
    return {'Qbh' : Qbh}


# ### Формула 192

# $ N = n * Q_{bh} * k * Yb * Yc$

# In[5]:


def f_192(input, printIndex = 1):
    
    n = input['n']
    Qbh = input['Qbh']
    Yc = input['Yc']
    k = input['k']
    
    def get_Yb(n):
        if 0 < n < 5:
            return 0.8
        elif 5 <= n < 10 :
            return 0.9
        else:
            return 1.0
            
    N = Qbh * k * Yc * get_Yb(n) * n
    
    if printIndex > 0 :
        print('N  = Qbh * k * Yb * Yc * n = ', "{:.2f}".format(N))
        
    return {'N' : N}


# ### Таблица 2

# In[6]:


def t_2(input, printIndex = 1):
    
    Ryn = input['Ryn']
    Run = input['Run']
    Ym = input['Ym']
    
    Ry = Ryn / Ym
    Ru = Run / Ym
    Rs = 0.58 * Ry
    Rp = Ru
    Rlp = 0.5 * Rp
    Rcd = 0.025 * Rp
    
    if printIndex > 0 :
        print('Ry = ', "{:.2f}".format(Ry))
        print('Ru = ', "{:.2f}".format(Ru))
        print('Rs = ', "{:.2f}".format(Rs))
        print('Rp = ', "{:.2f}".format(Rp))
        print('Rlp = ', "{:.2f}".format(Rlp))
        print('Rcd = ', "{:.2f}".format(Rcd))
        
    return {'Ry' : Ry, 'Ru' : Ru, 'Rs' : Rs, 'Rp' : Rp, 'Rlp' : Rlp, 'Rcd' : Rcd}


# ### Таблица 5

# In[4]:


def t_5(input, printIndex = 1):
    
    Ru = input['Ru']
    strengthClass = input['strengthClass']
    precisionClass = input['precisionClass']
    Rbun = input['Rbun']
    
    if strengthClass == '5.6':
        Rbs = 0.42 * Rbun
        Rbt = 0.45 * Rbun
    
    if strengthClass == '5.8':
        Rbs = 0.41 * Rbun
        Rbt = 0.00 * Rbun
        
    if strengthClass == '8.8':
        Rbs = 0.40 * Rbun
        Rbt = 0.54 * Rbun
        
    if strengthClass == '10.9':
        Rbs = 0.40 * Rbun
        Rbt = 0.70 * Rbun
        
    if strengthClass == '12.9':
        Rbs = 0.35 * Rbun
        Rbt = 0.70 * Rbun        
    
    if precisionClass == 'A':
        Rbp = 1.6 * Ru
    if precisionClass == 'B':
        Rbp = 1.35 * Ru
    
    if printIndex > 0 :
        print('Rbs = ', "{:.2f}".format(Rbs))
        print('Rbt = ', "{:.2f}".format(Rbt))
        print('Rbp = ', "{:.2f}".format(Rbp))
        
    return {'Rbs' : Rbs, 'Rbt' : Rbt, 'Rbp' : Rbp}


# ### Таблица 38

# In[7]:


def t_38(input, printIndex = 1):
    
    typeOfConnection = input['TYPE']
    typeOfWelding = input['WELDING']
    Ryn = input['Ryn']
    t = input['t']
    
    if typeOfConnection == 'T2' or typeOfConnection == 'L' or typeOfConnection == '||':
        if typeOfWelding == 'HAND':
            if Ryn <= 285:
                if 4 <= t <= 5: kf = 4
                if 6 <= t <= 10: kf = 4
                if 11 <= t <= 16: kf = 4
                if 17 <= t <= 22: kf = 6
                if 23 <= t <= 32: kf = 10
                if 33 <= t <= 40: kf = 12
            if 285 < Ryn <= 390:
                if 4 <= t <= 5: kf = 4
                if 6 <= t <= 10: kf = 5
                if 11 <= t <= 16: kf = 6
                if 17 <= t <= 22: kf = 8
                if 23 <= t <= 32: kf = 10
                if 33 <= t <= 40: kf = 14
            
        if typeOfWelding == 'AUTO' or typeOfWelding == 'SEMI-AUTO':
            if Ryn <= 285:
                if 4 <= t <= 5: kf = 3
                if 6 <= t <= 10: kf = 4
                if 11 <= t <= 16: kf = 4
                if 17 <= t <= 22: kf = 6
                if 23 <= t <= 32: kf = 10
                if 33 <= t <= 40: kf = 12
            if 285 < Ryn <= 390:
                if 4 <= t <= 5: kf = 3
                if 6 <= t <= 10: kf = 4
                if 11 <= t <= 16: kf = 5
                if 17 <= t <= 22: kf = 8
                if 23 <= t <= 32: kf = 10
                if 33 <= t <= 40: kf = 14
            if 390 < Ryn <= 590:
                if 4 <= t <= 5: kf = 4
                if 6 <= t <= 10: kf = 5
                if 11 <= t <= 16: kf = 6
                if 17 <= t <= 22: kf = 8
                if 23 <= t <= 32: kf = 10
                if 33 <= t <= 40: kf = 14
                    
    if typeOfConnection == 'T1' and Ryn <= 375:
        if typeOfWelding == 'HAND':
            if 4 <= t <= 5: kf = 5
            if 6 <= t <= 10: kf = 6
            if 11 <= t <= 16: kf = 7
            if 17 <= t <= 22: kf = 8
            if 23 <= t <= 32: kf = 10
            if 33 <= t <= 40: kf = 14
        if typeOfWelding == 'AUTO' or typeOfWelding == 'SEMI-AUTO':
            if 4 <= t <= 5: kf = 4
            if 6 <= t <= 10: kf = 5
            if 11 <= t <= 16: kf = 6
            if 17 <= t <= 22: kf = 10
            if 23 <= t <= 32: kf = 10
            if 33 <= t <= 40: kf = 18

    if printIndex > 0 :
        print('Kf = ', kf)
        
    return {'Kf' : kf}


# ### Таблица 39

# In[8]:


def t_39(input, printIndex = 1):
    
    locationOfSeam = input['LOCATION']
    typeOfWelding = input['WELDING']
    Kf = input['Kf']
    d = input['d']
    
    if typeOfWelding == 'AUTO' and 3 <= d <= 5:
        if locationOfSeam == 'FLAT':
            if 3 <= Kf <= 16:
                beta_f = 1.1
                beta_z = 1.15
            if Kf > 16:
                beta_f = 0.7
                beta_z = 1.0
                
        if locationOfSeam == 'BOTTOM':
            if 3 <= Kf <= 8:
                beta_f = 1.1
                beta_z = 1.15
            if 9 <= Kf <= 16:
                beta_f = 0.9
                beta_z = 1.05
            if Kf > 16:
                beta_f = 0.7
                beta_z = 1.0        
                
    if (typeOfWelding == 'AUTO' or typeOfWelding == 'SEMI-AUTO') and (1.4 <= d <= 2):
        if locationOfSeam == 'FLAT':
            if 3 <= Kf <= 12:
                beta_f = 0.9
                beta_z = 1.05
            if 14 <= Kf <= 16:
                beta_f = 0.8
                beta_z = 1.0
            if Kf > 16:
                beta_f = 0.7
                beta_z = 1.0
                
        if locationOfSeam in ['BOTTOM', 'HORIZONTAL', 'VERTICAL']:
            if 3 <= Kf <= 8:
                beta_f = 0.9
                beta_z = 1.05
            if 9 <= Kf <= 12:
                beta_f = 0.8
                beta_z = 1.0
            if Kf > 12:
                beta_f = 0.7
                beta_z = 1.0
                
    if (typeOfWelding == 'HAND') or (typeOfWelding == 'SEMI-AUTO' and d < 1.4):
        if locationOfSeam in ['FLAT', 'TOP', 'BOTTOM', 'HORIZONTAL', 'VERTICAL']:
            beta_f = 0.7
            beta_z = 1.0

    if printIndex > 0 :
        print('beta_f = ', beta_f, '; beta_z = ', beta_z)
        
    return {'beta_f' : beta_f, 'beta_z' : beta_z}


# ### Таблица 41

# In[7]:


def t_41(input, printIndex = 1):
    
    count = input['count']
    precisionClass = input['precisionClass']
    stress = input['stress']
    Ryn = input['Ryn']
    a = input['a']
    s = input['s']
    d = input['d']
    Yb = 0
    
    if stress == 'SHEAR' :
        Yb = 1.0
        if count > 1 and precisionClass != 'A' :
            Yb = Yb * 0.9
            
    if stress == 'COMPRESSION':
        if count == 1:
            
            if Ryn <= 285:
                if 1.5 <= a/d : Yb = 0.4 * min(2.0, a/d) + 0.2
                if 1.35 <= a/d < 1.5 : Yb = a/d - 0.7
                    
            if 285 < Ryn <= 375:
                if 1.5 <= a/d : Yb = 0.5 * min(2.0, a/d)
                if 1.35 <= a/d < 1.5 : Yb = 0.67 * a/d - 0.25
                    
            if Ryn > 375:
                if a/d >= 2.5 : Yb = 1.0
                    
        if count > 1:
            
            if (Ryn <= 285) and (1.5 <= a/d) and (2.0 <= s/d) :
                Yb = min(0.4 * min(2.0, a/d) + 0.2, 0.4 * min(2.5, s/d))
                
            if (285 < Ryn <= 375) and (1.5 <= a/d) and (2.0 <= s/d) :
                Yb = min(0.5 * min(2.0, a/d), 0.5 * min(2.5, s/d) - 0.25)
                
            if (Ryn > 375) and (a/d >= 2.5) and (s/d >= 3) :
                Yb = 1.0
            
            if precisionClass != 'A' : Yb = Yb * 0.9
           

    if printIndex > 0 :
        print('Yb = ', "{:.2f}".format(Yb))
        
    return {'Yb' : Yb}


# ### Таблица В.3

# In[9]:


def t_C3(input, printIndex = 1):
    
    g = input['grade']
    t = input['thickness']
    
    if g == 'C235' or g == 'С235' : # русский и английский вариант
        if 2.0 <= t <= 4.0:
            Ryn = 245
            Run = 370
            
    if g == 'C245' or g == 'С245' : # русский и английский вариант
        if 2.0 <= t <= 20.0:
            Ryn = 235
            Run = 360
            
    if g == 'C255' or g == 'С255' : # русский и английский вариант
        if 2.0 <= t < 4.0:
            Ryn = 255
            Run = 380
        elif 4 <= t <= 10:
            Ryn = 245
            Run = 380
        elif 10 < t <= 20:
            Ryn = 245
            Run = 370
        elif 20 < t <= 40:
            Ryn = 235
            Run = 370
     
    if g == 'C345' or g == 'С345' : # русский и английский вариант
        if 2.0 <= t <= 10.0:
            Ryn = 345
            Run = 490
        elif 10 <= t <= 20:
            Ryn = 325
            Run = 470
        elif 20 < t <= 40:
            Ryn = 305
            Run = 460
        elif 40 < t <= 60:
            Ryn = 285
            Run = 450
        elif 60 < t <= 80:
            Ryn = 275
            Run = 440
        elif 80 < t <= 160:
            Ryn = 265
            Run = 430
            
    if g == 'C345K' or g == 'С345К' : # русский и английский вариант
        if 4.0 <= t <= 10.0:
            Ryn = 345
            Run = 470
            
    if g == 'C355' or g == 'С355' : # русский и английский вариант
        if 8.0 <= t <= 16.0:
            Ryn = 355
            Run = 470
        elif 16 <= t <= 40:
            Ryn = 345
            Run = 470
        elif 40 < t <= 60:
            Ryn = 335
            Run = 470
        elif 60 < t <= 80:
            Ryn = 325
            Run = 470
        elif 80 < t <= 100:
            Ryn = 315
            Run = 470
        elif 100 < t <= 160:
            Ryn = 295
            Run = 470
            
    if g == 'C355-1' or g == 'C355-K' or g == 'С355-1' or g == 'С355-К': # русский и английский вариант
        if 8.0 <= t <= 16.0:
            Ryn = 345
            Run = 470
        elif 16 <= t <= 40:
            Ryn = 345
            Run = 470
        elif 40 < t <= 50:
            Ryn = 335
            Run = 470
    
    if g == 'C355P' or g == 'С355П': # русский и английский вариант
        if 8.0 <= t <= 16.0:
            Ryn = 355
            Run = 470
        elif 16 <= t <= 40:
            Ryn = 345
            Run = 470
    
    if g == 'C390' or g == 'C390-1'  or g == 'С390' or g == 'С390-1': # русский и английский вариант
        if 8.0 <= t <= 50.0:
            Ryn = 390
            Run = 520
            
    if g == 'C440' or g == 'С440': # русский и английский вариант
        if 8.0 <= t <= 50.0:
            Ry = 440
            Run = 540
            
    if g == 'C550' or g == 'С550': # русский и английский вариант
        if 8.0 <= t <= 50.0:
            Ryn = 540
            Run = 640
            
    if g == 'C590' or g == 'С590': # русский и английский вариант
        if 8.0 <= t <= 50.0:
            Ryn = 590
            Run = 685
            
    if g == 'C690' or g == 'С690': # русский и английский вариант
        if 8.0 <= t <= 50.0:
            Ryn = 690
            Run = 785
        
    if printIndex > 0 :
        print('Ryn = ', Ryn, '; Run = ', Run)
        
    return {'Ryn' : Ryn, 'Run' : Run}


# ### Таблица Г.5

# In[10]:


def t_D5(input, printIndex = 1):
    
    strengthClass = input['strengthClass']
    
    Rbun = {
        '5.6' : 500,
        '5.8' : 500,
        '8.8' : 830,
        '10.9' : 1040,
        '12.9' : 1220,
    }
    
    Rbyn = {
        '5.6' : 300,
        '5.8' : 400,
        '8.8' : 664,
        '10.9' : 936,
        '12.9' : 1098,
    }
    
    if printIndex > 0 :
        print('Rbun = ', Rbun[strengthClass], '; Rbyn = ', Rbyn[strengthClass])
        
    return {'Rbun' : Rbun[strengthClass], 'Rbyn' : Rbyn[strengthClass]}


# ### Таблица Г.8

# In[10]:


def t_D8(input, printIndex = 1):
    
    d = input['d']
    
    Rbun = {
        16 : 1078,
        20 : 1078,
        22 : 1078,
        24 : 1078,
        27 : 1078,
        30 : 900,
        36 : 800,
        42 : 650,
        48 : 600
    }
    
    if printIndex > 0 :
        print('Rbun = ', Rbun[d])
        
    return {'Rbun' : Rbun[d]}


# ### Таблица Г.9

# In[11]:


def t_D9(input, printIndex = 1):
    
    import math
    
    d = input['d']
    
    Abn = {
        16 : 157,
        18 : 192,
        20 : 245,
        22 : 303,
        24 : 353,
        27 : 459,
        30 : 561,
        36 : 816,
        42 : 1120,
        48 : 1472
    }
    
    Ab = math.pi * (d/2) ** 2
    
    if printIndex > 0 :
        print('Ab = ', "{:.1f}".format(Ab), '; Abn = ', Abn[d])
        
    return {'Ab' : Ab, 'Abn' : Abn[d]}

