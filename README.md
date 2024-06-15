# Pilar Hiring Challenge

> Construir uma API em Python que possua duas rotas de requisição do tipo POST, sendo uma para contar a quantidade de vogais nas palavras recebidas atraves da requisição, e outra recebe uma lista de palavras e ordená-la com base na informação recebida via API sobre o tipo de ordenação (crescente ou decrescente), em resumo.

## Como testar e como rodar localmente o projeto?
No email enviado contém um arquivo postman com as requisições para facilitar execução já configurado com a rota da aplicação deployada diretamente na AWS. Mas podemos executar o projeto facilmente seguindo os passos abaixo:

Se preferir pode utilizar versão hospedada:
[http://pilar.waldrey.com/](http://pilar.waldrey.com/)

```shell
cp .env .env.example
docker build -t pilar_python .
docker run -d --name pilar_words -p 8080:80 pilar_python
```

Logo apos executar os comandos em seu _docker desktop_ deve aparecer o container ativo.
![image](https://github.com/waldrey/pilar/assets/43473539/9a6fed44-b911-42e8-81af-1a8a5fad4c8e)

## Pipeline
Primeiramente construi uma **branch rule** para conseguimos realizar o deploy/merge da aplicação somente se a primeira etapa _Build Image & Code Quality_ fosse realizada com sucesso. 
O lint é obrigatório a passar sem falha e todos os testes precisam passarem. Caso ainda esteja em uma branch diferente de _main_ o deploy não é ativado, somente quando é realizado commit/merge para **main**. Na seção abaixo falamos mais sobre infraestrutura e contém mais detalhes de como funciona passo a passo para realização do deploy na AWS.

## Infraestrutura
Explicando um pouco sobre a infraestrutura construída na AWS para realização do deploy. A ideia foi utilizar **Amazon ECS** como servidor para a aplicação, já que a AWS faz a gestão dos pods/nodes do Kubernetes para nós com facilidade, sem precisarmos configurar todo nosso **yaml** para memória, CPU, probes e estratégia de deploy.

Abaixo temos um diagrama da infraestrutura construída, resumidamente mostrando o caminho que o usuário final realiza para conseguir acessar nossa API. Também o caminho de como é realizado o deploy da aplicação assim que uma _Pull Request_ é mergeada para a branch **main**.

Neste projeto, utilizamos as seguintes ferramentas da AWS:

1. **Amazon ECR** (Utilizamos para salvar a imagem docker com novo código da aplicação);
2. **Amazon ECS/Fargate** (Criamos um cluster simples .5CPU & 1GB Memória para receber os serviços fargate onde está nossa aplicação rodando);
3. **VPC** (Uma rede simples com uma URL pública exposta para fazer conexão com nosso dominio configurado através do Route 53);
4. **Route 53** (Usamos para criar subdominio apontando para novo IP público a cada deploy realizado pela pipeline).

![image](https://github.com/waldrey/pilar/assets/43473539/c3883993-640f-4a77-9fed-280b6d5ff087)
