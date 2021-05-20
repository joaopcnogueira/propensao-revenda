# Tutorial Deploy na Amazon Web Service

### 1. Abrir uma conta na AWS

As seguintes informações serão solicitadas no momento da criação da conta:

- E-mail
- Tipo de conta (selecione para uso Pessoal)
- Nome completo
- Número de telefone valido (será enviado uma mensagem para validar a conta)
- País, Endereço, Cidade, Estado, Código Postal
- Número de cartão de crédito
- CPF

A instância que iremos criar tem o perfil de free tier, ou seja, nenhuma cobrança será realizada dentro do período de 12 meses, porém é importante verificar as regras e quais os serviços que o free tier permite utilizar. Acesse https://aws.amazon.com/pt/free/ para maiores informações.

Para criar a conta, clique em: https://portal.aws.amazon.com/billing/signup#/start

### 2. Criar uma instância micro (free tier)

Após a criação da conta, faça o login em https://console.aws.amazon.com/

Utilize o e-mail e a senha definido no passo 1 para realizar o login. Pode ser solicitado alguma verificação de segurança.

Após o login realizado clique em **Launch a virtual machine** conforme imagem abaixo:



<img src="tutoriais/imagens/aws_01.png" style="zoom:50%;" />

**Caso apareça uma mensagem informando que o serviço está quase pronto é por que a AWS define um período máximo de 24 horas para que os serviços estejam disponíveis, porém é provável que após alguns minutos tudo esteja pronto para uso.**

Caso, já esteja tudo pronto, a seguinte tela irá aparecer.

<img src="tutoriais/imagens/aws_02.png" style="zoom:50%;" />

Digite **Ubuntu** no campo da pesquisa e depois selecione **Ubuntu Server 20.04 LTS (HVM), SSD Volume Type**, por fim clique em **Select**.

Na próxima etapa selecione o tipo de instância que será criada. 

<img src="tutoriais/imagens/aws_03.png" style="zoom:50%;" />

Selecione a **t2.micro** que é elegível para o nível gratuito. Clique em **Next: Configure Instance Details**.

Nessa etapa não precisa alterar nenhuma informação, basta clicar em **Next: Add Storage**.

<img src="tutoriais/imagens/aws_04.png" style="zoom:55%;" />

Altere o valor de 8 para **30 GiB **de armazenamento. Não adicione mais do que 30, pois é o limite para o nível gratuito. Por fim, clique em **Next: Add Tags**.

<img src="tutoriais/imagens/aws_05.png" style="zoom:55%;" />

Adicione uma Tag: na coluna **key** adicione o valor `Nome` e na coluna **value** adicione o valor `deploy_modelos` (ou qualquer outro nome). 

Clique em **Next: Configure Security Group**.

Nessa etapa será necessário adicionar diversas portas para que possamos acessar os serviços que iremos executar. Preencha conforme a imagem abaixo. Clique em **Add Rule** para adicionar novas linhas.

<img src="tutoriais/imagens/aws_06.png" style="zoom:55%;" />

A tabela abaixo apresenta os tipos e a porta que deve ser utilizada

| Type       | Port Range |
| ---------- | ---------- |
| SSH        | 22         |
| Custom TCP | 8000       |
| Custom TCP | 8501       |
| HTTP       | 80         |
| HTTPS      | 443        |

Clique em **Review and Launch**.

Na próxima tela será apresentado uma visão geral de todas as configurações realizadas, basta clicar em **Launch**.

O último passo será criar uma chave de acesso que será útil para acessar a instancia via SSH. Crie um nome e faça o download da chave. Salve em um lugar seguro.

<img src="tutoriais/imagens/aws_07.png" style="zoom:55%;" />

Após clique em **Launch Instances**. A seguinte tela irá aparecer:

<img src="tutoriais/imagens/aws_08.png" style="zoom:55%;" />

Clique em **View Instances** para finalizar.

### 3. Acessar a instância

Na página das instancias, clique na caixa de seleção do lado esquerdo do nome que foi adicionado para visualizar as informações sobre a instancia criada. Conforme ilustrado na imagem abaixo.

<img src="tutoriais/imagens/aws_09.png" style="zoom:55%;" />

Anote o IP Publico (**Public IP**) pois iremos utilizar nos próximos passos.

Por fim, iremos acessar o terminal da instancia criada para instalar e configurar a implantação da API e do Web App. Para isso, clique com o botão direito em cima da linha da instancia que criamos e clique em **Connect** conforme imagem abaixo:

<img src="tutoriais/imagens/aws_10.png" style="zoom:55%;" />

Uma nova janela será aberta, com qual tipo de acesso será feito. Clique em **EC2 Instance Connect** e depois clique em **Connect**. 

<img src="tutoriais/imagens/aws_11.png" style="zoom:55%;" />

Um nova aba será aberta com o terminal disponível, conforme imagem abaixo.

<img src="tutoriais/imagens/aws_12.png" style="zoom:75%;" />

Ótimo, já podemos seguir com os próximos passos!



### 4. Faça o clone do código fonte

Na janela que abriu no navegador, com acesso ao terminal, execute os comandos abaixo:

```bash
git clone https://github.com/joaopcnogueira/propensao-revenda.git
```

```bash
cd propensao-revenda
```

```bash
bash deploy_aws.sh
```

Aguarde a instalação e configuração das bibliotecas necessárias. Se algum erro aparecer, digite `Ctrl + C` e finalize a execução. Tente rodar novamente o comando `bash deploy_aws.sh`.

Após a finalização da instalação, deixe essa janela aberta e acesse os serviços em novas janelas:

- Em um nova aba do navegador, digite `http://IP_DA_INSTANCIA:8000/docs` para executar a API
- Em um nova aba do navegador, digite  `http://IP_DA_INSTANCIA:8501` para executar a Web App

### 5. Finalize a instancia após os testes

Para não ocasionar custos, termine a instancia que foi criada.  Para isso, na lista de instancias, clique com o botão direto em cima da instancia que deseja terminar e clique em **Terminate Instance**, conforme imagem abaix.

<img src="tutoriais/imagens/aws_13.png" style="zoom:75%;" />

Uma mensagem de confirmação irá aparecer. Clique em **Terminate** para confirmar.

<img src="tutoriais/imagens/aws_14.png" style="zoom:75%;" />



**ATENÇÃO: isso irá deletar e remover todas as instalações e configurações. Caso deseje testar novamente, será necessário executar esse tutorial novamente (Passos 2 até 5).**





