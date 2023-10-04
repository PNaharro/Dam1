pacient= {'nom': 'Pep', 'edat': 42, 'Diabetic': True}
f = open('pacient.txt','w+')
f.write(pacient['nom']+'    '+str(pacient['edat'])+'    '+str(pacient['Diabetic']))