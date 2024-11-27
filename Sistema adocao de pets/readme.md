# Sistema adoção de pets

# Visualização

## Deploy
***Ferramenta utilizada para Deploy: Render***

<p align="center">
  <img alt="Preview do deploy feito." src=".images/deploy.png" width="100%">
</p>

<p align="center">
  <img alt="Preview do deploy feito." src=".images/deployed.png" width="100%">
</p>

## Pytest
<p align="center">
  <img alt="Preview dos testes bem sucedidos." src=".images/pytest.png" width="100%">
</p>

## Organização dos Arquivos
<p align="center">
  <img alt="Preview da organização dos arquivos." src=".images/files.png" width="100%">
</p>

---

## 📋 Descrição do Projeto

Este repositório foi desenvolvido para demonstrar como estruturar um projeto utilizando:

- **Ambientes virtuais** para isolar dependências e garantir consistência entre diferentes máquinas.
- **Configuração do Pylint** para melhorar a qualidade do código e seguir boas práticas.
- **Padrão MVC** para separar responsabilidades e melhorar a organização do código.
- **Integração com o VSCode**, configurando corretamente as ferramentas essenciais para desenvolvimento.

---

## ⚙️ Configuração do Ambiente

### 1. Criação e Ativação do Ambiente Virtual

1. **Instale o `virtualenv`**:
   ```bash
   pip install virtualenv

2. Crie o ambiente virtual:
   ```bash
   python -m venv venv
   
3. Ative o ambiente virtual (Windows):
   ```bash
   .\venv\Scripts\activate

4. Selecione o interpretador Python no VSCode (Pressione Ctrl + P):
   ```mathematica
   > Select Interpreter
- Escolha o ambiente virtual criado (venv).

---

## 🔍 Configuração do Pylint
### Pylint, fornece uma análise de código
1. Instalação
```bash
pip install pylint
```
2. Listar bibliotecas do venv em um arquivo (para windows):
```bash
pip freeze > requirements.txt
```
3. Instalar todas as dependencias de uma vez:
```bash
pip install -r requirements.txt
```
### Instale a extensão no VsCode do Pylint.

---

### Forçar o vscode entender o pylint:
1. Criar uma pasta ".vscode" e dentro dela um "settings.json"
```json
{
   "python.linting.enabled": true,
   "python.linting.pylintEnabled": true
}
```

## Configurar Pylint para windows:
```bash
pylint --generate-rc-file | out-file -encoding utf8 .pylintrc
```
## ou
```bash
pylint --generate-rcfile > .pylintrc
```

### Desativar algumas configurações chatas do pylint:
**No arquivo .pylintrc que criou anteriormente faça:**
```bash
[MAIN]

disable=
    C0114,  # Missing module docstring
    C0115,  # Missing class docstring
    C0116,  # Missing function or method docstring
    W0703,  # Catching too general exception
    W0311,  # Bad identation
    C0209,  # String formatting using f-string instead of `%` or `.format()`
    C0303,  # Trailing whitespace
    C0304,  # Final new line missing
    E0015,  # Python syntax error
```
### Testar o Pylint:
```bash
pylint "nome seu arquivo python"
```

---

## Pre-commit

1. Instalar
```bash
pip install pre-commit
```
2. Configuração pre-commit:
- criar arquivo ".pre-commit-config.yaml" e colocar:
```bash
repos:
  - repo: local
    hooks:
      - id: pylint
        name: pylint
        entry: pylint
        language: system  # Usar o pylint do sistema
        types: [python]
        args:
          - "--disable=R,C"  # Desativa categorias de mensagens específicas
          - "--rcfile=.pylintrc"  # Corrigido: arquivo de configuração do pylint
          - "--load-plugins=pylint.extensions.docparams"  # Carrega o plugin docparams
```
3. Rodar o comando:
```bash
pre-commit install
```

