# Missão 1: Restaurando as Regras Escolares
# Verifica se a nota do aluno garante aprovação (nota >= 5).
def verificar_aprovacao(nota):
    if nota >= 5:
        return "Aprovado"
    else:
        return "Reprovado"


# Missão 2: O Sistema Eleitoral Secreto
# Verifica se o usuário possui idade mínima para votar (idade >= 16).
def verificar_voto(idade):
    if idade >= 16:
        return "Você pode votar."
    else:
        return "Você não pode votar."


# Missão 3: Recuperando o Sistema de Notas
# Classifica a nota do aluno e retorna um comentário baseado na faixa de pontuação.
def classificar_nota(nota):
    if 90 <= nota <= 100:
        return "Parabéns, você tirou A!"
    elif 80 <= nota < 90:
        return "Muito bem, você tirou B."
    elif 70 <= nota < 80:
        return "Bom trabalho, você tirou C."
    elif 60 <= nota < 70:
        return "Fique atento, você tirou D."
    else:
        return "Estude um pouco mais, você tirou F."


# Missão 4: Restaurando a Identificação de Números
# Recebe dois números e retorna a sua soma.
def somar_numeros(a, b):
    return a + b


# Missão 5: Recuperando o Cofre de Segurança
# Compara a senha informada com a senha correta ("Python123") e retorna o status do acesso.
def verificar_senha(senha):
    senha_correta = "Python123"
    if senha == senha_correta:
        return "Acesso permitido."
    else:
        return "Acesso negado."


# Missão 6: Reforçando a Segurança e a Contagem do Sistema
# Utiliza um laço de repetição while para imprimir os números de 1 a 10.
def contar_ate_dez():
    i = 1
    while i <= 10:
        print(i)
        i += 1


# Missão 7: Organizando a Lista
# Cria uma lista de números desordenados e a retorna ordenada.
def ordenar_lista():
    numeros = [8, 3, 10, 1, 5]
    return sorted(numeros)


# Missão 8: Acessando os Registros de Alunos
# Trabalha com uma tupla de nomes e retorna o primeiro e o último nome.
def acessar_registros(alunos=("Ana", "Bruno", "Carla", "Daniel", "Eduardo")):
    return alunos[0], alunos[-1]


# Missão 9: Calculando o Dobro de um Número
# Recebe um número e retorna uma string com o dobro do número.
def dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"


# Missão 10: Contando Letras
# Recebe um nome e retorna quantas letras ele possui, em formato de string.
def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras."


if __name__ == '__main__':
    print("=== Missão 1: Restaurando as Regras Escolares ===")
    print("Resultado:", verificar_aprovacao(8))
    print("\n=== Missão 2: O Sistema Eleitoral Secreto ===")
    print("Resultado:", verificar_voto(16))
    print("\n=== Missão 3: Recuperando o Sistema de Notas ===")
    print("Resultado:", classificar_nota(85))
    print("\n=== Missão 4: Restaurando a Identificação de Números ===")
    print("Resultado:", somar_numeros(4, 5))
    print("\n=== Missão 5: Recuperando o Cofre de Segurança ===")
    print("Resultado:", verificar_senha("Python123"))
    print("\n=== Missão 6: Reforçando a Segurança e a Contagem do Sistema ===")
    contar_ate_dez()
    print("\n=== Missão 7: Organizando a Lista ===")
    print("Resultado:", ordenar_lista())
    print("\n=== Missão 8: Acessando os Registros de Alunos ===")
    print("Resultado:", acessar_registros())
    print("\n=== Missão 9: Calculando o Dobro de um Número ===")
    print("Resultado:", dobro(5))
    print("\n=== Missão 10: Contando Letras ===")
    print("Resultado:", contar_letras("Ana"))