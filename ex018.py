from math import  radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo de {}°C tem o SENO de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O ângulo de {}°C tem o COSSENO de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O ângulo de {}°C tem a TANGENTE de {:.245f}'.format(ang, tangente))
