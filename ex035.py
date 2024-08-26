print('-=-'*8)
print('Analisador de Triângulos')
print('-=-'*8)
seg1 = float(input('Primeiro seguimento: '))
seg2 = float(input('Segundo seguimento: '))
seg3 = float(input('Terceiro seguimento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 or se3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR Triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulo')
