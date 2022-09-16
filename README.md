<ol>
  <li>Instale o python</li>

  <li>Entre no terminal e execute:
    <code>python -m pip install --upgrade pip</code>
  </li>

  <li>Baixe este projeto e descompacte o conteudo em uma pasta <code>teste_streamlit</code>. Entre na pasta.</li>

  <li>Execute:
    <code>pip install -r requirements.txt --upgrade</code>
  </li>

  <li>Execute:
    <code>streamlit run app.py</code>
  </li>
<ol>

## Estrutura do repositorio 
| Folder/Code | Content |
| ------------- | ------------- |
| .streamlit | Contém o confiq.toml para definir certos parâmetros de design |
| data | Contém os dados  no formato CSV |
| app.py |	Contém o aplicativo Streamlit real |
| requirements.txt | Contém todos os requisitos (necessários para compartilhamento Streamlit) |