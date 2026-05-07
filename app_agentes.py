import streamlit as st
from crewai import Agent, Task, Crew, Process
import os

# ==========================================================
# 1. CONFIGURAÇÃO DA INTERFACE E ESTADO DA SESSÃO
# ==========================================================
st.set_page_config(page_title="Multi-Agent Factory", layout="wide")

# Inicializa o histórico do resultado na memória do navegador
if "resultado_final" not in st.session_state:
    st.session_state.resultado_final = ""

st.title("🤖 Multi-Agent Orchestrator Factory")
st.markdown("Selecione o perfil do especialista e defina o tema da pesquisa.")

# ==========================================================
# 2. BARRA LATERAL (CONFIGURAÇÕES)
# ==========================================================
with st.sidebar:
    st.header("⚙️ Configurações")
    groq_key = st.text_input("Groq API Key", type="password", help="Insira sua chave gsk_...")
    
    modelo_selecionado = st.selectbox(
        "Cérebro do Agente (LLM)",
        ["groq/llama-3.3-70b-versatile", "groq/llama3-8b-8192"]
    )

    st.divider()
    
    # SELEÇÃO DE PERFIL DINÂMICO
    st.header("👤 Perfil do Especialista")
    perfil_selecionado = st.selectbox(
        "Agir como:",
        ["Analista de Tecnologia", "Contador Consultor", "Engenheiro de Software", "Especialista em Marketing"]
    )

    # MAPA DE PERSONALIDADES
    perfis_config = {
        "Analista de Tecnologia": {
            "role": "Analista de Tecnologia Sênior",
            "backstory": "Especialista em hardware, tendências de IA e métricas de desempenho técnico."
        },
        "Contador Consultor": {
            "role": "Consultor Contábil e Tributário",
            "backstory": "Especialista em legislação brasileira, análise de balanços e planejamento fiscal."
        },
        "Engenheiro de Software": {
            "role": "Arquiteto de Sistemas Full Stack",
            "backstory": "Especialista em Clean Code, escalabilidade, segurança e padrões de projeto modernos."
        },
        "Especialista em Marketing": {
            "role": "Estrategista de Growth Marketing",
            "backstory": "Especialista em comportamento do consumidor, SEO, tráfego pago e branding digital."
        }
    }

    # BOTÃO DE LIMPAR MEMÓRIA
    if st.button("🗑️ Limpar Memória/Sessão"):
        st.session_state.resultado_final = ""
        st.rerun()

# ==========================================================
# 3. ÁREA PRINCIPAL
# ==========================================================
tema_usuario = st.text_input(f"O que o {perfil_selecionado} deve analisar?", 
                            placeholder="Digite o tema ou problema aqui...")

if st.button("🚀 Iniciar Processo"):
    if not groq_key:
        st.error("⚠️ Por favor, insira sua chave da Groq na barra lateral.")
    elif not tema_usuario:
        st.warning("⚠️ Digite um tema para a pesquisa.")
    else:
        try:
            with st.status(f"Integrando Agentes ({perfil_selecionado})...", expanded=True) as status:
                os.environ["GROQ_API_KEY"] = groq_key
                
                config = perfis_config[perfil_selecionado]

                # AGENTE 1: O Especialista Escolhido
                agente_especialista = Agent(
                    role=config["role"],
                    goal=f'Realizar uma análise técnica e profunda sobre: {tema_usuario}',
                    backstory=config["backstory"],
                    llm=modelo_selecionado,
                    verbose=True
                )

                # AGENTE 2: O Redator (Sempre focado em formatar a saída)
                redator = Agent(
                    role='Redator Científico',
                    goal='Sintetizar as descobertas em um relatório estruturado e profissional',
                    backstory='Especialista em redação técnica, clareza textual e normas ABNT.',
                    llm=modelo_selecionado,
                    verbose=True
                )

                # TAREFAS
                tarefa_pesquisa = Task(
                    description=f'Analise detalhadamente o tema "{tema_usuario}" sob a perspectiva de um {perfil_selecionado}.',
                    expected_output='Um relatório técnico com pontos principais e recomendações.',
                    agent=agente_especialista
                )

                tarefa_escrita = Task(
                    description='Formate a análise anterior em um documento Markdown elegante e profissional.',
                    expected_output='Relatório final completo em Markdown.',
                    agent=redator
                )

                # EXECUÇÃO
                equipe = Crew(
                    agents=[agente_especialista, redator],
                    tasks=[tarefa_pesquisa, tarefa_escrita],
                    process=Process.sequential
                )

                resultado = equipe.kickoff()
                st.session_state.resultado_final = resultado
                status.update(label="✅ Concluído!", state="complete", expanded=False)

        except Exception as e:
            st.error(f"Erro na execução: {e}")

# EXIBIÇÃO DOS RESULTADOS
if st.session_state.resultado_final:
    st.divider()
    st.subheader(f"📄 Relatório Final: {perfil_selecionado}")
    st.markdown(st.session_state.resultado_final)
    
    st.download_button(
        label="📥 Baixar Documento",
        data=str(st.session_state.resultado_final),
        file_name=f"analise_{perfil_selecionado.replace(' ', '_')}.md",
        mime="text/markdown"
    )