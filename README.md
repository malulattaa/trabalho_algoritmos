# Gerenciador de Eventos — Projeto Final de Algoritmos

O sistema consiste em um gerenciador de eventos, tendo como funcionalidades principais, o gerenciamento de eventos, o gerenciamento de participantes e os relatórios e estatísticas.

## Estrutura do Projeto

Dividi as funcionalidades em arquivos distintos referentes a cada área:
- `participante.py`: cadastro, busca, atualização e inscrição
- `evento.py`: gerenciamento de eventos
- `estatisticas.py`: relatórios e análises
- `temas.py`: temas disponíveis para eventos e preferências
- `menu.py`: menus e navegação
- `dados.py`: dicionários com dados de eventos e participantes para falicitar o teste
- `util.py`: funções utilitárias reutilizáveis


## Funcionalidades úteis:
    Como já mencionado, o arquivo util.py contém funcionalidades que são importantes no sistema e que foram colocadas em uma função devido a necessidade de ser utilizada regularmente.
    
    Nele constam funções como:
    - **ler_opcao**: utilizada em menus para ler a opção que o usuário deseja executar, recebendo como parâmetro um limite superior (lim_sup), sendo o número de opções que o usuário pode escolher, de 0 até o limite, onde o número 0 utilizado para voltar a sessão anterior.
    - **limpar_tela**: usado para melhorar a interface com o usuário, permitindo uma experiência limpa e clara.
    - **titulos**: também utilizado para melhorar a interface com o usuário, construindo um terminal organizado.
    - **menu_geral**: o menu geral recebe como parâmetro um título e o dicionário. Assim, ele percorre o dicionário onde pega a chave (número da opção) e os valores (descrição e a função associada a ela). No menu exibido ao usuário, mostra apenas o número e a descrição, ignorando a função (através do uso de _ ). Dessa forma, a função só é executada quando o usuário digitar a opção desejada.
    - **verificar_participantes**: a função verifica, através de um filter, se a chave do participante está na lista de participantes do evento, retornando um novo dicionário apenas com os participantes inscritos naquele evento.
    - **ler_id**: ler id é usada sempre que for requisitado um id do usuário. A função tem como objetivo verificar se o número digitado é do tipo esperado, eliminando possíveis erros de valor.
    - **existencia**: recebe um id digitado pelo usuário e um dicionário como parâmetro. Se o id existir dentro do dicionário percorrido, o valor é retornado, caso contrário, exibe uma mensagem de código não encontrado.
    - **tratar_data**: esse campo recebe uma data e verifica se a mesma foi digitada no formato que deveria. O strptime é usado para converter string em data/hora, sendo um método da classe datetime. Os formatos %d, %m e %Y são respectivamente usados para que o python identifique o um dia com dois dígitos, mês com dois dígitos e ano com quatro dígitos. Caso contrário, exibe uma mensagem de data inválida.
    - **tratar_email**: visto que o e-mail do participante deve ser único, a função recebe o e-mail e por meio de um set verifica se ele já consta no campo e-mail no dicionário de algum participante e se constar, exibe uma mensagem para que o usúario digite outro.
    - **sair_tela**: para melhorar a navegação e garantir que os dados e mensagens sejam mostrados corretamente, foi criada uma função para que o usuário determine a hora que quer sair da mesma.

## Desenvolvido por

    Maria Luisa Ribeiro Martins Latta  
    Instituto Federal de Mato Grosso do Sul – Campus Três Lagoas  
    Disciplina: Algoritmos 1
