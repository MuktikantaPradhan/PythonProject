import nlglib
realise_en = Realiser(host='nlg.kutlak.info', port=40000)

p = Clause(NP('YouTube'), VP('video','sharing'))
p['TENSE'] = 'PAST'
q = Clause(NP('Video'), VP('free','upload'))
q['TENSE'] = 'PAST'
print(realise_en(p))
print(realise_en(q))
r=Clause(realise_en(p)[:-1],'while',realise_en(q))
print(r)