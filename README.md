# Gerenciador de Eventos — Projeto Final de Algoritmos

O sistema consiste em um gerenciador de eventos, tendo como funcionalidades principais, o gerenciamento de eventos, o gerenciamento de participantes e os relatórios e estatísticas.

## Estrutura do Projeto

Dividi as funcionalidades em arquivos distintos referentes a cada área:
- `participante.py`: cadastro, listagem, busca, atualização, inscrição e remoção;
- `evento.py`: cadastro, listagem, participantes do evento, remoção, alteração, filtro e agrupamento;
- `estatisticas.py`: estatísticas e relatórios, como: participantes mais ativos, média de participante por tema, eventos com poucos participantes, temas frequentes, resumo geral do sistema e eventos populares;
- `temas.py`: temas disponíveis para eventos e preferências;
- `menu.py`: menus e navegação;
- `dados.py`: dicionários com dados de eventos e participantes para falicitar o teste;
- `util.py`: funções utilitárias reutilizáveis.

## Funcionalidades úteis:
Como já mencionado, o arquivo util.py contém funcionalidades que são importantes no sistema e que foram colocadas em uma função devido a necessidade de ser utilizada regularmente.
    
Nele constam funções como:
- **`ler_opcao`**:: Utilizada em menus para ler a opção que o usuário deseja executar, recebendo como parâmetro um limite superior (`lim_sup`), sendo o número de opções que o usuário pode escolher, de 0 até o limite, onde o número 0 é utilizado para voltar à sessão anterior.
- **`limpar_tela`**: Usado para melhorar a interface com o usuário, permitindo uma experiência limpa e clara.
- **`titulos`**: Também utilizado para melhorar a interface com o usuário, construindo um terminal organizado.
- **`menu_geral`**: O menu geral recebe como parâmetro um título e o dicionário. Assim, ele percorre o dicionário onde pega a chave (número da opção) e os valores (descrição e a função associada a ela). No menu exibido ao usuário, mostra apenas o número e a descrição, ignorando a função (através do uso de _ ). Dessa forma, a função só é executada quando o usuário digitar a opção desejada, chamando-a através de `funcao()`.
- **`verificar_participantes`**: A função verifica, através de um filter, se a chave do participante está na lista de participantes do evento, retornando um novo dicionário apenas com os participantes inscritos naquele evento.
- **`ler_id`**: Ler id é usada sempre que for requisitado um id para o usuário. A função tem como objetivo verificar se o número digitado é do tipo esperado, eliminando possíveis erros de valor.
- **`existencia`**: Recebe um id digitado pelo usuário e um dicionário como parâmetro. Se o id existir dentro do dicionário percorrido, o valor é retornado, caso contrário, exibe uma mensagem de código não encontrado.
- **`tratar_data`**: Esse campo recebe uma data e verifica se a mesma foi digitada no formato que deveria. O strptime é usado para converter string em data/hora, sendo um método da classe datetime. Os formatos %d, %m e %Y são respectivamente usados para que o python identifique um dia com dois dígitos, mês com dois dígitos e ano com quatro dígitos. Caso contrário, exibe uma mensagem de data inválida.
- **`tratar_email`**: Visto que o e-mail do participante deve ser único, essa função recebe o e-mail e por meio de um set verifica se ele já consta no campo e-mail no dicionário de algum participante, e se constar, exibe uma mensagem para que o usúario digite outro. Além disso, impede que o usuário deixe o campo vazio.
- **`sair_tela`**: Para melhorar a navegação e garantir que os dados e mensagens sejam mostrados corretamente, foi criada uma função para que o usuário determine a hora que quer sair da mesma.
- **`- ler_campo_obrigatorio`**: Impede que o usuário deixe vazio os campos obrigatórios de: nome do evento, nome do participante e e-mail. 

## Participantes:
As funções relacionadas aos participantes, como cadastro, listagem, busca, atualização, inscrição e remoção, são em sua maioria, realizadas através de um ID, criado por uma variável global. O uso da variável foi um meio de garantir que cada participante tenha um identificador único. Dessa forma, mesmo que um participante seja excluído, o ID não poderá ser reutilizado e os outros participantes não sofrerão alterações. 
O uso do ID gerado automaticamente foi pensado para garantir que o sistema seja prático. O CPF embora único, exige validações específicas e lida com dados sensíveis. Enquanto isso, o ID referencia o participante com segurança, realiza buscas diretas e garante unicidade sem expor informações pessoais.

## Eventos:
As funções realizadas em eventos como cadastro, listagem, participantes do evento, remoção, alteração, filtro e agrupamento por tema, também utilizam um ID numérico único. Apesar do sistema garantir que o nome do evento seja único, seu uso como chave foi evitado para permitir alterações futuras no nome do evento sem erros, além de cadastro de nomes parecidos e facilidade na referência aos eventos.
Da mesma forma como em participantes, a variável global também foi utilizada em eventos para garantir códigos únicos e sequenciais, contando ainda com: 
- **validações de data**: para não permitir que o evento seja cadastrado em datas passadas;
- **validação de horários**: foi determinado um período comercial e os eventos só podem acontecer nesse intervalo; 
- **tema central**: cada evento tem seu tema central.
> O sistema foi projetado para aceitar apenas um tema central por evento, não permitindo a associação de múltiplos temas.

## Estatísticas e Relatórios

O módulo `estatisticas.py` tem como objetivo gerar **informações úteis a partir dos cadastros e inscrições realizadas**.

Entre as funcionalidades disponíveis, estão:

- **Participantes mais ativos**: lista os participantes inscritos em mais de um evento.
- **Média de participantes por tema**: calcula a média de inscritos em eventos agrupados por tema.
- **Eventos com poucos participantes**: exibe eventos com menos de dois inscritos, para possível cancelamento.
- **Temas frequentes**: identifica os temas mais usados nos eventos cadastrados.
- **Resumo geral**: mostra uma visão ampla com o total de participantes, eventos e temas.
- **Eventos mais populares**: ordena e exibe os 5 eventos com mais participantes.

> O objetivo dessa seção é **prover insights rápidos e relevantes** para o organizador dos eventos.

## Desenvolvido por

    Maria Luisa Ribeiro Martins Latta  
    Instituto Federal de Mato Grosso do Sul – Campus Três Lagoas  
    Disciplina: Algoritmos 1
