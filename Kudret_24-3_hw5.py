data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for i in data:
    if type(i).istitle(i):
        designations.append(i)
    else:
        codes.append(i)
i = 0
operators = dict()
while i < len(codes):
    operators[designations[i]] = {codes[i]}
    i += 1
operators.pop('Katel')
operators.pop('Fonex')
operators['O!'].add('0700')
operators['O!'].add('0500')
operators['Megacom'].add('0999')
operators['Megacom'].add('0555')
operators['Beeline'].add('0222')
operators['Beeline'].add('0777')
for i in operators:
    print(f'{i} - {operators[i]}' )