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



# Missão 5: Recuperando o Cofre de Segurança
# Compara a senha informada com a senha correta ("Python123") e retorna o status do acesso.



# Missão 6: Reforçando a Segurança e a Contagem do Sistema
# Utiliza um laço de repetição while para imprimir os números de 1 a 10.



# Missão 7: Organizando a Lista
# Cria uma lista de números desordenados e a retorna ordenada.


# Missão 8: Acessando os Registros de Alunos
# Trabalha com uma tupla de nomes e retorna o primeiro e o último nome.


# Missão 9: Calculando o Dobro de um Número
# Recebe um número e retorna uma string com o dobro do número.



# Missão 10: Contando Letras
# Recebe um nome e retorna quantas letras ele possui, em formato de string.



if __name__ == '__main__':
    print("=== Missão 1: Restaurando as Regras Escolares ===")
    print("Resultado:", verificar_aprovacao(6))
    print("\n=== Missão 2: O Sistema Eleitoral Secreto ===")
    print("Resultado:", verificar_voto(15))
    print("\n=== Missão 3: Recuperando o Sistema de Notas ===")
    print("Resultado:", classificar_nota(85))
