import streamlit as st

st.set_page_config(page_title="Projeto Streamlit", layout="wide")
st.markdown("# Rituais Satânicos")

def main():
    abas = st.tabs([
        "Candidatos",
        "Cadastrar Candidatos",
        "Editar",
        "Deletar"

    ])

    with abas[0]:
        st.title("Candidatos")

    with abas[1]:
        st.title("Cadastrar Candidatos")

        with st.form(key='add_candidato', clear_on_submit=True):
            nome = st.text_input("Nome", placeholder="Nome")
            email = st.text_input("Email", placeholder="Email")
            idade = st.number_input("Idade", placeholder="Idade", format="%d", step=1)
            telefone = st.number_input("Telefone", placeholder="Telefone", format="%d", step=1)
            oferenda = st.selectbox("Selecione a Oferenda", options=[
                "Recém Nascido", "Cabra", "Mulher Virgem", "Dinheiro"
            ])
            btn_cadastrar = st.form_submit_button("Cadastrar Candidatos")

            data_candidato = {
                "nome": nome,
                "email": email,
                "idade": idade,
                "telefone": telefone,
                "oferenda": oferenda
            }

            st.write(data_candidato)

    with abas[2]:
        st.title("Editar")

    with abas[3]:
        st.title("Deletar")    

main()
