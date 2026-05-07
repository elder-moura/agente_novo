# 🤖 Multi-Agent Tech Orchestrator (M.A.T.O)

Este projeto é uma aplicação de **Inteligência Artificial Multi-Agente** que utiliza o framework **CrewAI** para orquestrar especialistas autônomos em diferentes domínios, como Tecnologia, Contabilidade e Engenharia de Software.

A aplicação permite que o usuário interaja com uma equipe de agentes através de uma interface web dinâmica, onde cada agente assume um papel (persona) específico para realizar pesquisas profundas e sínteses técnicas.

## 🚀 Funcionalidades

- **Orquestração de Agentes:** Utiliza o CrewAI para gerenciar a colaboração entre um Agente Especialista (Pesquisador) e um Agente Redator.
- **Perfis Dinâmicos:** O usuário pode alternar a "personalidade" e o domínio de conhecimento dos agentes (ex: de um Contador para um Desenvolvedor).
- **Interface Web:** Desenvolvido com **Streamlit** para uma experiência de usuário fluida e intuitiva.
- **Baixa Latência:** Integrado à API da **Groq**, utilizando modelos de linguagem de última geração (Llama 3) com alta velocidade de processamento.
- **Configuração de Precisão:** Implementação de controle de temperatura do modelo para garantir respostas técnicas e reduzir alucinações.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **CrewAI:** Framework para orquestração de agentes.
- **Streamlit:** Framework para interface web.
- **LangChain:** Integração com modelos de linguagem.
- **Groq Cloud:** Infraestrutura de processamento de LLM.
- **GitHub Codespaces:** Ambiente de desenvolvimento e deploy em nuvem.

## 📋 Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-seu-repositorio.git](https://github.com/seu-usuario/nome-do-seu-repositorio.git)
    cd SEU_REPOSITORIO
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute a aplicação:**
    ```bash
    python -m streamlit run app_agentes.py
    ```

## 🧠 Arquitetura do Sistema

O sistema opera em um fluxo sequencial:
1. **Input:** O usuário define o tema e o perfil do especialista.
2. **Pesquisa:** O Agente Especialista utiliza seu *backstory* e *goal* para minerar informações técnicas.
3. **Redação:** O Agente Redator processa os dados e formata um relatório em Markdown seguindo normas técnicas.
4. **Output:** O sistema disponibiliza o relatório para leitura na tela e download.

---
Desenvolvido por Elder Moura como parte de estudos em Inteligência Artificial e Sistemas Distribuídos.
