genero = ['masculino', 'feminino', 'outros']
estadoCivil = ('solteiro','casado','separado')

cliente = {
    'Codigo'     : 123,
    'Nome'       : 'Jose da Silva',
    'Nascimento' : '01/05/1942',
    'CPF'        : '111222333-44'
}
print(cliente)
print('Nome do cliente: ', cliente['Nome'])
print('CPF do clinte: ', cliente['CPF'])

xCodigo     = input('Digite seu código: ')
xNome       = input('Digite seu nome: ')
xNascimento = input('Digite seu nascimento: ')
xCPF        = input('Digite seu CPF: ')

Cliente = {
    'Codigo'     : xCodigo,
    'Nome'       : xNome,
    'Nascimento' : xNascimento,
    'CPF'        : xCPF
}
print(Cliente)


