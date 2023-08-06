import sys
import os
import re

def render(template_path, context): # Define uma função chamada 'render' que recebe o caminho para o arquivo de template e um dicionário 'context'.
    template = open(template_path, 'r').read() # Abre o arquivo de template em modo de leitura e lê todo o conteúdo para a variável 'template'.
    return template.format(**context).strip('"') # Substitui os placeholders no template pelos valores do dicionário 'context' usando a função 'format'. Em seguida, remove as aspas duplas no início e no final do resultado.

def main(): # Define a função principal 'main'.
    if len(sys.argv) != 2: # Verifica se o número de argumentos fornecidos na linha de comando é diferente de 2.
        print("Usage: python3 render.py <template_file>") # Imprime uma mensagem de uso correto do script.
        sys.exit(1)

    template_path = sys.argv[1] # Armazena o caminho para o arquivo de template, que é o segundo argumento fornecido na linha de comando.

    if not template_path.endswith('.template'): # Verifica se o arquivo de template não possui a extensão '.template'.
        print("Error: Template file must have a .template extension.") # Imprime uma mensagem de erro informando a extensão correta do arquivo de template.
        sys.exit(1)

    if not os.path.exists(template_path): # Verifica se o arquivo de template não existe.
        print(f"Error: {template_path} does not exist.") # Imprime uma mensagem de erro informando que o arquivo de template não existe.
        sys.exit(1)

    context = {} # Cria um dicionário vazio chamado 'context' para armazenar as informações do arquivo 'settings.py'.
    settings = open("settings.py", 'r').read() # Abre o arquivo 'settings.py' em modo de leitura e lê todo o conteúdo para a variável 'settings'.

    for line in settings.splitlines(): # Itera sobre as linhas do arquivo 'settings.py'.
        if line.startswith('#'): # Se a linha começar com '#', é um comentário, então pula para a próxima linha.
            continue

        match = re.match(r'(\w+)\s*=\s*(.*)', line) # Usa uma expressão regular para procurar um padrão de atribuição no formato 'variavel = valor' em cada linha.
        if match: # Se encontrou um padrão de atribuição na linha, continua.
            key, value = match.groups() # Obtém o nome da variável (chave) e o valor correspondente (valor) do padrão encontrado.

            # Remove as aspas duplas no início e no final do valor, se estiverem presentes.
            context[key] = value.strip('"')

    rendered_html = render(template_path, context) # Chama a função 'render' para preencher o template com as informações do dicionário 'context' e armazena o resultado na variável 'rendered_html'.

    output_file = template_path.replace('.template', '.html') # Obtém o nome do arquivo de saída (HTML) trocando a extensão '.template' pela '.html'.

    open(output_file, 'w').write(rendered_html) # Abre o arquivo de saída (HTML) em modo de escrita e escreve o conteúdo do template renderizado.

if __name__ == '__main__':
    main()
