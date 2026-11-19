# Site da MACH Estúdio

Página única da MACH Estúdio: sites sob medida, com animação de verdade.

## O que tem aqui

| Caminho | O que é |
| --- | --- |
| `index.html` | O site pronto, em um arquivo só. É este que vai para a hospedagem. |
| `src/index.html` | O código-fonte. É aqui que se edita. |
| `assets/logo.png` | O logo, embutido no site na hora de gerar. |
| `build.py` | Gera o `index.html` a partir do código-fonte. |
| `CHANGELOG.md` | O que mudou em cada versão. |

## Como editar

1. Altere `src/index.html`.
2. Rode `python3 build.py` para gerar o `index.html`.
3. Abra o `index.html` por um servidor local (`python3 -m http.server`) e confira no celular e no computador.

O site não usa biblioteca externa: as duas cenas 3D são WebGL escrito à mão. A única coisa carregada de fora é a fonte Inter, do Google Fonts.

## Como versionar

O projeto segue versionamento semântico (`MAIOR.MENOR.CORREÇÃO`):

- **Correção** (`0.4.0` → `0.4.1`): ajuste que não muda o que o site faz, como um texto ou um bug.
- **Menor** (`0.4.0` → `0.5.0`): seção ou animação nova.
- **Maior** (`0.x` → `1.0.0`): reservado para o lançamento no domínio oficial, e depois para reformulações.

A cada versão:

```bash
python3 build.py
git add -A
git commit -m "feat: descrição curta do que mudou"
git tag -a v0.5.0 -m "v0.5.0: descrição curta"
```

E acrescente a entrada no `CHANGELOG.md` antes do commit.

## Como ver ou voltar para uma versão antiga

```bash
git tag                 # lista as versões
git checkout v0.2.0     # abre o projeto como estava nessa versão
git checkout main       # volta para a mais recente
```

## Como enviar para o GitHub

Crie um repositório vazio no GitHub e rode, trocando o endereço pelo seu:

```bash
git config user.name "Seu nome"
git config user.email "seu-email@exemplo.com"
git remote add origin https://github.com/SEU-USUARIO/mach-site.git
git push -u origin main --tags
```
