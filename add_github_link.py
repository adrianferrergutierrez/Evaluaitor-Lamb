import os

tfg_path = '/home/adrif/Evaluaitor-Lamb/docs/TFG.tex'
try:
    with open(tfg_path, 'r', encoding='utf-8') as f:
        tex_content = f.read()

    repo_annex = """\\appendix

\\chapter{Codi Font i Repositori}
\\label{annex:repositori}
El codi font complet d'aquest projecte, incloent-hi totes les versions de la documentació, l'historial de desenvolupament, els tests i els resultats d'avaluació complets, està publicat en obert i és accessible al següent repositori de GitHub:

\\begin{center}
    \\url{https://github.com/adrianferrergutierrez/Evaluaitor-Lamb}
\\end{center}
"""
    # Replace the \appendix command with \appendix + the new chapter
    tex_content = tex_content.replace("\\appendix", repo_annex)

    with open(tfg_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print("Success")
except Exception as e:
    print(f"Error: {e}")
