print("Seja bem-vindo ao site de apostas!")
print("Aqui sua aposta vale dinheiro, fique à vontade!")
print("Para começarmos, faça seu login")



email = str(input("Digite seu Email: "))
senha = str(input("Digite sua Senha: "))
idade = int(input("Digite sua idade: "))
if email == 'paulo@hotmail.com' and senha == '12345':
    print("Parabéns! Seu login foi validado com sucesso!")
    print("Vamos as apostas?")
else:
    print("seu login está incorreto. ")
if not idade >= 18:
    print(" Infelizmente você não tem idade para acessar esse site . ")
else:
    print(" Seja bem vindo ao site.")
futapostas =str(input("Digite um time: "))
placar =str(input("Digite o seu palpite, exemplo (7x1),(7x2) entre outros... "))
if placar == '3x0'or placar == '5x5':
    print(" Que bom você conseguiu acertar o placar. ")
else:
    print(" Você perdeu sua aposta. ")