"""Em sua programação semanal, uma rede de televisão apresenta os seguintes telejornais:
• Bom Dia Nação, apresentado por Zé PINHEIRO e por Ana Carla ARAÚJO
• Jornal Brasileiro, apresentado por Bill BONNER E CARLA VASCONCELOS
Crie um programa no qual o usuário informe o sobrenome de um dos apresentadores. Se o
sobrenome informado não estiver na lista acima, o programa deve mostrar a mensagem
“Apresentador(a) desconhecido(a).”. Em caso positivo, o programa deve mostrar o nome do
telejornal apresentado pelo apresentador(a)."""

sobrenome = input('Informe o sobrenome de um apresentador: ').upper()

if sobrenome == 'PINHEIRO' or 'ARAÚJO':
    print('Bom Dia Nação, apresentado por Zé PINHEIRO e por Ana Carla ARAÚJO')

elif sobrenome == 'BONNER' or 'VASCONCELOS':
    print('Jornal Brasileiro, apresentado por Bill BONNER E CARLA VASCONCELOS')

else:
    print('Apresentador(a) desconhecido(a).')
