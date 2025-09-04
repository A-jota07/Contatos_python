README: Agenda de Contatos em Python 🐍
Este projeto é uma agenda de contatos simples, criada em Python, que permite salvar, listar, remover contatos e realizar outras ações, como backup e exportação para PDF. A interface gráfica (GUI) é construída usando a biblioteca Tkinter.

📋 Funcionalidades
Salvar Contato: Adicione novos contatos com nome, telefone e e-mail. A aplicação valida se os campos estão preenchidos e se o telefone e o e-mail seguem um formato válido.

Listar Contatos: Visualize todos os contatos salvos em uma lista organizada.

Remover Contato: Exclua um contato da lista.

Backup: Crie uma cópia de segurança do arquivo de contatos (contatos.csv) em uma pasta backups com carimbo de data e hora.

Exportar para PDF: Gere um arquivo PDF (Contatos.pdf) com a lista de todos os contatos.

🛠️ Pré-requisitos
Para rodar este projeto, você precisará ter o Python instalado. As bibliotecas reportlab e tkinter também são necessárias. A tkinter geralmente já vem instalada com o Python, mas a reportlab precisa ser instalada manualmente.

Você pode instalar a biblioteca reportlab usando o pip, o gerenciador de pacotes do Python:

pip install reportlab


🚀 Como Usar
Baixe os arquivos: Certifique-se de que todos os arquivos (main.py, utils.py, contatos.py e ui.py) estão no mesmo diretório.

Execute o script: Abra o terminal ou prompt de comando, navegue até a pasta do projeto e execute o arquivo principal:

python main.py


Interface Gráfica: Uma janela da interface da agenda de contatos será aberta. Você pode usar os botões e campos de texto para interagir com a aplicação.

Acessórios: Os contatos são salvos em um arquivo chamado contatos.csv na mesma pasta do script. Backups são salvos na pasta backups e o PDF exportado é gerado como Contatos.pdf.

📁 Estrutura do Projeto
main.py: Ponto de entrada da aplicação.

ui.py: Contém a lógica para a criação da interface gráfica (Tkinter).

contatos.py: Lida com as operações de CRUD (Create, Read, Update, Delete) dos contatos.

utils.py: Funções auxiliares para validação de dados, backup e exportação.

contatos.csv: O arquivo onde os dados dos contatos são armazenados.

🤝 Contribuições
Contribuições são bem-vindas! Se você tiver alguma ideia ou encontrar um bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.
