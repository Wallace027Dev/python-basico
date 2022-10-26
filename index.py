#PRIMEIRO OLÁ MUNDO

print("Olá, mundo!");


#DESMONSTRANDO FORMAS DE IMPRIMIR VALOR

print(12345);
print('valor',12345);
print('valor = {}'.format(12345));
print(f'valor = {12345}');
print("valor",12345);
print("valor = {}".format(12345));
print(f"valor = {12345}");


#IMPRIMINDO NUMERO E TIPO

x=5;
print(x,type(x));


#MOSTRANDO ALGUMAS SINTAXES DO PYTHON
"""
print(help(int));
"""

#PROGRAMA BASICO USANDO FOR, IF, ELSE E RANGE

a = 0
for i in range(30):
    if a % 2 ==0:
        a += 1 
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
            print (a)


#VARIÁVEIS DE PYTHON

x=10
print(x)
#substituindo o valor de X
x=20
print(x)
#guardando uma variavel não definida
#b


#ESCOPO E TEMPO DE VIDA

#Variáveis locais

def multiplicador(numero):
    a=2 #esta varia tem escopo local
    print(f"Dentro da função, a variável vale: {a}")
    return a*numero

a=3 #esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável vale: {a}")



def multiplicador(numero):
    return a*numero
a=3 #esta variável tem escopo global
b=multiplicador(5)
print(f"A variável b vale: {b}")


def multiplicador(numero):
    global a #todas as referências à variável são para a global
    a=2 #a global será alterado
    print(f"Dentro da função, a variável vale: {a}")
    return a*numero
a=3 #esta variável tem escopo global
b=multiplicador(5)
print(f"A variável b vale: {b}")
print(f"fora da função, a variável a vale: {a}")

#EXERCITANDO
def func():
    x=1
    print(x)
x=10
func()
print(x)

Texto='texto de exemplo'
print(Texto)

#TIPOS DE DADOS E EXPRESSOES EM PYTHON
#Tipos Numéricos

print(type(2+3+1))
print(type(2+3+1.0))

print (2**3) #exponenciação
print (type(2**3))
print (type(2.0**3))

x = 5/2
print(x)

x=21//2
print(x)
y=21%2
print(y)

#o tipo complex
r=complex(2,5)
print(r)
#É o tipo utilizado para manipular números complexos,
#na forma x + yj, sendo x a parte real e 
# y a parte imaginária do complexo.
w=2+5j
print(type(w))
# A chamada r.conjugate() retorna o conjugado do número complexo r,
# em que a parte real é mantida e
# a parte imaginária tem o seu sinal trocado.

#O tipo bool
print(2<3)

#TIPOS SEQUENCIAIS
#Dicionário usando cpf, nome e sobrenome
pessoas={'1111111111111':['João','Silva'],'2222222222222':['Maria','Vitória'],'3333333333333':['Wallace','Vieira']}
print(pessoas['1111111111111'])

""" 
(2+3)–(4**2)+(5/2)–(5//2)
5-16+2.5-2
"""

# print(5-16+2.5-2)
a=['U']+['RN']
len(a)
b=['4']*4
len(b)
print(len(a),len(b))
#len=length

#EXERCITANDO O QUE FOI APRENDIDO ATÉ AQUI
a=['10']
b=['20']
c=['30']
print(a+b+c)

a=['10']
b=['20']
c=['30']
print((a*2)+(b*3)+(c*4))


x=0
a=10
b=5

x=(-b)/a
fx=a*x+b

#print(x)
#print(fx)
print('A raiz da equação do primeiro grau é: x={}'.format(x))

#ENTRADA DE DADOS COM INPUT()
nome= input('Entre com seu nome: ')
print('Você digitou:',nome) #A FUNÇÃO INPUT SEMPRE RECEBE VALORES COMO STRING


#FUNÇÃO EVAL
numero=eval(input('Entre com um numero inteiro: '))
numero=numero+2
print(numero) #A função eval() recebe uma string, mas trata como um valor numérico

#EXERCÍCIO PARA CALCULAR IMC
alt=eval(input('informe sua altura metro: '))
pe=eval(input('informe seu peso em kg: '))
imc=pe/(alt**2)
print(imc)


#FORMATAÇÃO DE DADOS DE SAÍDA
hora,minuto,segundo=10,26,18
print(str(hora)+':'+str(minuto)+':'+str(segundo))
print('{}:{}:{}'.format(hora,minuto,segundo)) #usando format
print(f'{hora}:{minuto}:{segundo}') #usando print() e 'f'
print('{:4},{:5}'.format(10,100)) #especificando largura
print('{:8.5}'.format(10/3)) #O método format() também pode ser usado como precisão definida

