"""
Lógica das recomendações do Desenrola.

Não mexe no banco: só lê os usuários e compara as habilidades.
Cada campo (habilidadeEnsina / habilidadeAprende) pode ter mais de uma
habilidade separada por vírgula, ponto e vírgula ou barra. Ex.: "Python, Inglês".
A comparação ignora maiúsculas, minúsculas e acentos ("Ingles" = "inglês").
"""
import re
import unicodedata

from .models import Usuario


def normalizar(texto):
    """'  Inglês ' -> 'ingles'"""
    texto = unicodedata.normalize("NFD", texto or "")
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return " ".join(texto.lower().split())


def separar_habilidades(campo):
    """'Python, Inglês' -> {'python': 'Python', 'ingles': 'Inglês'}
    A chave é o texto normalizado; o valor é o texto original, para exibir."""
    habilidades = {}
    for parte in re.split(r"[,;/]", campo or ""):
        parte = parte.strip()
        if parte:
            habilidades.setdefault(normalizar(parte), parte)
    return habilidades


def recomendar(usuario):
    """Devolve três listas de recomendações para o usuário informado.

    - troca_perfeita: a pessoa ensina o que você quer aprender
                      E quer aprender o que você ensina
    - ensinam_voce:   a pessoa ensina o que você quer aprender
    - aprendem_voce:  a pessoa quer aprender o que você ensina

    Cada item é um dicionário com a pessoa e as habilidades em comum.
    Quem já está em "troca perfeita" não repete nas outras listas.
    """
    ensino_a = separar_habilidades(usuario.habilidadeEnsina)
    aprende_a = separar_habilidades(usuario.habilidadeAprende)

    troca_perfeita, ensinam_voce, aprendem_voce = [], [], []

    for outro in Usuario.objects.exclude(pk=usuario.pk):
        ensino_b = separar_habilidades(outro.habilidadeEnsina)
        aprende_b = separar_habilidades(outro.habilidadeAprende)

        # B ensina algo que A quer aprender
        voce_aprende = [ensino_b[k] for k in ensino_b if k in aprende_a]
        # B quer aprender algo que A ensina
        voce_ensina = [aprende_b[k] for k in aprende_b if k in ensino_a]

        if not voce_aprende and not voce_ensina:
            continue

        item = {
            "usuario": outro,
            "voce_aprende": voce_aprende,
            "voce_ensina": voce_ensina,
            "pontos": len(voce_aprende) + len(voce_ensina),
        }
        if voce_aprende and voce_ensina:
            troca_perfeita.append(item)
        elif voce_aprende:
            ensinam_voce.append(item)
        else:
            aprendem_voce.append(item)

    def ordenar(lista):
        return sorted(lista, key=lambda i: (-i["pontos"], i["usuario"].nome.lower()))

    return {
        "troca_perfeita": ordenar(troca_perfeita),
        "ensinam_voce": ordenar(ensinam_voce),
        "aprendem_voce": ordenar(aprendem_voce),
    }
