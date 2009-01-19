# -*- coding: utf-8 -*-
"""
"""

from quantities.unitquantity import UnitCurrent, \
    UnitLuminousIntensity, UnitQuantity
from quantities.units.time import s
from quantities.units.length import m
from quantities.units.energy import J
from quantities.units.velocity import c
from quantities.units.force import N
from math import pi


A = amp = amps = ampere = amperes = UnitCurrent(
    'ampere',
    symbol='A',
    aliases=['amp', 'amps', 'amperes']
)
mA = milliamp = milliampere = UnitCurrent(
    'milliampere',
    A/1000,
    symbol='mA',
    aliases=['milliamp', 'milliamps', 'milliamperes']
)
uA = microampere = UnitCurrent(
    'microampere',
    mA/1000,
    symbol='uA',
    u_symbol='µA',
    aliases=['uA', 'microamp', 'microamps', 'microamperes'])
nA = nanoamp = nanoampere = UnitCurrent(
    'nanoampere',
    uA/1000,
    symbol='nA',
    aliases=['nanoamp', 'nanoamps', 'nanoamperes']
)
pA = picoamp = picoampere = UnitCurrent(
    'picoampere',
    nA/1000,
    symbol='pA',
    aliases=['picoamp', 'picoamps', 'picoamperes']
)
aA = abampere = biot = UnitCurrent(
    'abampere',
    10*A,
    symbol='aA',
    aliases=['abamperes', 'biot', 'biots']
)

esu = statcoulomb = statC = franklin = Fr = UnitQuantity(
    'statcoulomb',
    0.1*A*m/c,
    symbol='esu',
    aliases=['statcoulombs', 'statC', 'franklin', 'franklins', 'Fr']
)
esu_per_second = statampere = UnitCurrent(
    'statampere',
    esu/s,
    symbol='(esu/s)',
    aliases=['statamperes']
)

ampere_turn = UnitQuantity(
    'ampere_turn',
    1*A
)
Gi = gilbert = UnitQuantity(
    'gilbert',
    10/(4*pi)*ampere_turn,
    symbol='Gi'
)

C = coulomb = UnitQuantity(
    'coulomb',
    A*s,
    symbol='C'
)
V = volt = UnitQuantity(
    'volt',
    J/C,
    symbol='V',
    aliases=['volts']
)
F = farad = UnitQuantity(
    'farad',
    C/V,
    symbol='F',
    aliases=['farads']
)
ohm = UnitQuantity(
    'ohm',
    V/A,
    u_symbol='Ω',
    aliases=['ohms']
)
S = siemens = UnitQuantity(
    'siemens',
    A/V,
    symbol='S'
)
Wb = weber = UnitQuantity(
    'weber',
    V*s,
    symbol='Wb',
    aliases=['webers']
)
T = tesla = UnitQuantity(
    'tesla',
    Wb/m**2,
    symbol='T',
    aliases=['teslas']
)
H = henry = UnitQuantity(
    'henry',
    Wb/A,
    symbol='H'
)
abfarad = UnitQuantity(
    'abfarad',
    1e9*farad,
    aliases=['abfarads']
)
abhenry = UnitQuantity(
    'abhenry',
    1e-9*henry
)
abmho = UnitQuantity(
    'abmho',
    1e9*S
)
abohm = UnitQuantity(
    'abohm',
    1e-9*ohm
)
abvolt = UnitQuantity(
    'abvolt',
    1e-8*V,
    aliases=['abvolts']
)
e = elementary_charge = UnitQuantity(
    'elementary_charge',
    1.602176487e-19*C,
    symbol='e',
    note='relative uncertainty = 6.64e-8'
)
chemical_faraday = UnitQuantity(
    'chemical_faraday',
    9.64957e4*C
)
physical_faraday = physical_faradays = UnitQuantity(
    'physical_faraday',
    9.65219e4*C
)
faraday = C12_faraday = UnitQuantity(
    'faraday',
    96485.3399*C,
    symbol='F',
    aliases=['faradays']
)
gamma = UnitQuantity(
    'gamma',
    1e-9*T
)
gauss = UnitQuantity(
    'gauss',
    1e-4*T,
    symbol='G'
)
maxwell = UnitQuantity(
    'maxwell',
    1e-8*Wb,
    symbol='Mx',
    aliases=['maxwells']
)
Oe = oersted = UnitQuantity(
    'oersted',
    1000/(4*pi)*A/m,
    symbol='Oe',
    aliases=['aliases']
)
statfarad = statF = stF = UnitQuantity(
    'statfarad',
    1.112650e-12*F,
    symbol='stF',
    aliases=['statfarads', 'statF']
)
stathenry = statH = stH = UnitQuantity(
    'stathenry',
    8.987554e11*H,
    symbol='stH',
    aliases=['statH', 'stH']
)
statmho = statS = stS = UnitQuantity(
    'statmho',
    1.112650e-12*S,
    symbol='stS'
)
statohm = UnitQuantity(
    'statohm',
    8.987554e11*ohm,
    u_symbol='stΩ',
    aliases=['statohms']
)
statvolt = statV = stV = UnitQuantity(
    'statvolt',
    2.997925e2*V,
    symbol='stV',
    aliases=['statvolts', 'statV', 'stV']
)
unit_pole = UnitQuantity(
    'unit_pole',
    1.256637e-7*Wb
)
vacuum_permeability = mu_0 = magnetic_constant = UnitQuantity(
    'magnetic_constant',
    4*pi*10**-7*N/A**2,
    symbol='epsilon_0',
    u_symbol='μ₀',
    aliases=['vacuum_permeability']
)
vacuum_permittivity = epsilon_0 = electric_constant = UnitQuantity(
    'electric_constant',
    1/(mu_0*c**2),
    symbol='epsilon_0',
    u_symbol='ε₀',
    aliases=['vacuum_permittivity']
)
Z_0 = impedence_of_free_space = characteristic_impedance_of_vacuum = \
        UnitQuantity(
    'characteristic_impedance_of_vacuum',
    mu_0*c,
    symbol='Z_0',
    u_symbol='Z₀',
    aliases=['impedence_of_free_space']
)

cd = candle = candela = UnitLuminousIntensity(
    'candela',
    symbol='cd',
    aliases=['candle', 'candles', 'candelas']
)

del UnitQuantity, s, m, J, c
