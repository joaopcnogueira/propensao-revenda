# Tutorial Deploy na Google Cloud Platform
1. Abrir uma conta na GCP
2. Criar uma VM (instância) Ubuntu-20.04 no Google Compute Engine
    1. `Menu de navegação` > `Compute Engine` > `Instância de VM` > `Criar Instância`;
    2. Em `Nome`, atribua um nome a sua máquina virtual (VM) caso deseje;
    2. Em `Firewall`, marcar as caixas `Permitir tráfego HTTP` e `Permitir tráfego HTTPS`;
    3. Clicar em `Criar`.
3. Liberar as portas `8000` (fastapi) e `8501` (streamlit)
    1. `Mais ações` (3 pontinhos) > `Ver detalhes da rede`;
    2. Em `Detalhes da interface de rede`, clicar no valor `default` no campo `Rede`;
    3. Em `Regras de Firewall` > `default-allow-http`, clicar em `Editar`;
    4. Em `Portas e protocolos especificados` > `tcp`, digitar as portas: 80, 8000, 8501 e clicar em `SALVAR`;
    5. Volte para a página anterior e vá em `default-allow-https` > `Editar`;
    6. Em `Portas e protocolos especificados` > `tcp`, digitar as portas: 443, 8000, 8501 e clicar em `SALVAR`;
    7. Voltar para a tela das VMs, clicando no `Menu de navegação` > ` Compute Engine` > `Instância de VM`.

4. Abrir um SSH (terminal)
    1. Em `Conectar`, clicar em `SSH`;
    2. Executar os comandos no script `deploy.sh`.

5. Executando as aplicações
    1. Para executar as aplicações, primeiro tem que buscar o IP da máquina virtual. Navegue até `Menu de navegação` > ` Compute Engine` > `Instância de VM`, e copie o IP da máquina virtual.
    2. Com o IP em mãos, abra o seu navegador e digite os seguintes endereços:
        - Para executar a API: `http://IP_DA_MAQUINA_VIRTUAL:8000/docs`
        - Para executar a Web App: `http://IP_DA_MAQUINA_VIRTUAL:8501`
