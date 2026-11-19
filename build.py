#!/usr/bin/env python3
"""Gera o index.html final a partir de src/index.html, embutindo o logo no arquivo."""
import base64
import pathlib

raiz = pathlib.Path(__file__).parent
fonte = (raiz / "src" / "index.html").read_text(encoding="utf-8")
logo = "data:image/png;base64," + base64.b64encode((raiz / "assets" / "logo.png").read_bytes()).decode()
saida = fonte.replace("__LOGO__", logo)

if "__KB__" in saida:  # só a versão 0.1.0 mostrava o próprio peso na página
    kb = round(len(saida.encode("utf-8")) / 1024 / 5) * 5
    saida = saida.replace("__KB__", str(kb)).replace("__PCT__", f"{kb / 3000 * 100:.1f}")

(raiz / "index.html").write_text(saida, encoding="utf-8")
print(f"index.html gerado: {len(saida.encode('utf-8')) / 1024:.0f} KB")
