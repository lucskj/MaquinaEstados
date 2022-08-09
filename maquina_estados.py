# Lucas Kreutzer de Jesus

"""
ENUNCIADO
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a linguagem Python, C ou C++.
Este programa, quando executado, irá determinar se uma string de entrada faz parte da linguagem 𝐿 definida  por
𝐿 = {𝑥 | 𝑥 ∈ {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) contendo várias strings.
A primeira linha do arquivo indica quantas strings estão no arquivo de texto de entrada. As linhas subsequentes contém
uma string por linha.  A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa
que você irá desenvolver:
3
abbaba
abababb
bbabbaaab
Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será representado  por  um
número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e somente uma linha de saída para cada
string. Estas linhas conterão a string de entrada e o resultado da validação conforme o formato indicado a seguir:
abbaba: não pertence.
A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será composta de uma
linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
"""

# Definição de uma função para lidar com a validação das palavras.
def check_string(palavra):
  resultado = True                   # Inicializando uma variável de retorno.
  palavra_min = palavra.lower()       # Deixando a palavra em minúsculo para facilitar a validação.
  letras_possiveis = ['a', 'b', 'c']  # Lista com os caracteres possíveis, de acordo com o alfabeto proposto.
  tamanho_palavra = len(palavra)      # Variável para armazenar o tamanho da palavra.

  # Loop para checar cada letra dentro da palavra em questão.
  for i in range(0, tamanho_palavra):
    letra = palavra_min[i]

    # Caso seja um caracter inválido, retornará falso.
    if letra not in letras_possiveis:
      return False
    elif letra == 'a':
      # Caso o caracter 'a' esteja na última ou penúltima posição, sabemos que a palavra está inválida.
      # Essa condição vem antes para evitar erro de "Out of Bounds".
      if i == tamanho_palavra-1 or i == tamanho_palavra-2:
        return False
      # Caso contrário, checaremos os dois caracteres posteriores.
      if palavra_min[i+1] == 'b' and palavra_min[i+2] == 'b':
        resultado = True
      else:
        return False

  return resultado


# Variável que irá armazenar o nome do arquivo que será lido.
# Portanto, para realizar os testes, é necessário alterar o valor aqui.
arquivo = "strings3.txt"

# Importante notar que eu direcionei a abertura de arquivos dentro da pasta 'Arquivos'. 
# Então, peço que mova qualquer arquivo novo desejado para a pasta indicada, ou altere o caminho no parâmetro abaixo.
# A estrutura 'with' efetua o fechamento automático do arquivo após seu uso.
with open("Arquivos/%s" % arquivo) as dados:
  nomes = dados.readlines()
  qtd_palavras = int(nomes[0])

  # Checando se o inteiro passado na primeira linha do arquivo bate com a quantidade de palavras existentes nas linhas seguintes.
  if len(nomes) == qtd_palavras+1:
    contador = 1
    # Loop para checar cada palavra dentro do arquivo.
    while contador <= qtd_palavras:
      # Retirando o caracter adicional '\n' e chamando a função de checagem.
      palavra = nomes[contador].strip('\n')
      resposta = check_string(palavra)
  
      # Realizando o print do resultado de acordo com o retorno da função.
      if resposta:
        print("%s: pertence." % palavra)
      else:
        print("%s: não pertence." % palavra)
      contador += 1
  else:
    print("Quantidade de palavras não corresponde.")
