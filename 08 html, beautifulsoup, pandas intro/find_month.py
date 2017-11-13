def month_string_to_number(elem):

    lst = ['jan', 'feb', 'mär', 'apr',
       'mai', 'jun', 'jul', 'aug',
       'sep', 'okt', 'nov', 'dez']

    for elem in lst:

        if elem in test.lower():
            m = {
            'jan': 1,
            'feb': 2,
            'mär': 3,
            'apr':4,
             'mai':5,
             'jun':6,
             'jul':7,
             'aug':8,
             'sep':9,
             'okt':10,
             'nov':11,
             'dez':12
            }
            s = elem.strip()[:3].lower()

            try:
                out = m[s]
                return out
            except:
                raise ValueError('Not a month')
