# cases_meta.py

# a list of the different cases describing the format of molecular states:
# each case's caseID is (its index in this list) + 1.
cases = ['dcs', 'hunda', 'hundb', 'ltcs', 'nltcs', 'stcs', 'lpcs',
       'asymcs', 'asymos', 'sphcs', 'sphos', 'ltos', 'lpos', 'nltos']

case_descriptions = {
'dcs': 'Diatomic closed-shell molecules',
'hunda': "Hund's case (a) diatomics",
'hundb': "Hund's case (b) diatomics",
'ltcs': 'Closed-shell, linear triatomic molecules',
'nltcs': 'Closed-shell, non-linear triatomics',
'stcs': 'Closed shell, symmetric-top molecules',
'lpcs': 'Closed-shell, linear polyatomic molecules',
'asymcs': 'Closed-shell, asymmetric top molecules',
'asymos': 'Open-shell, asymmetric top molecules',
'sphcs': 'Closed-shell, spherical-top molecules',
'sphos': 'Open-shell, spherical-top molecules',
'ltos': 'Open-shell,linear triatomic molecules',
'lpos': 'Open-shell, linear polyatomic molecules',
'nltos': 'Open-shell, non-linear triatomics',
}

caseIDs = {'dcs': 1, 'hunda': 2, 'hundb': 3, 'ltcs': 4, 'nltcs': 5,
           'stcs': 6, 'lpcs': 7, 'asymcs': 8, 'asymos': 9, 'sphcs': 10,
           'sphos': 11, 'ltos': 12, 'lpos': 13, 'nltos': 14}
