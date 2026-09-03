import os
import uuid
import shutil
from fastapi import UploadFile, HTTPException

EXTENSOES_PERMITIDAS = {".jpg", ".jpeg", ".png", ".webp"}
DIRETORIO_BASE_UPLOADS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads")


def salvar_imagem(arquivo: UploadFile, subpasta: str) -> str:
    """
    Valida e salva um arquivo de imagem em backend/uploads/<subpasta>/
    Retorna a URL relativa da imagem (ex: /uploads/empresas/nome_arquivo.png).
    """
    if not arquivo or not arquivo.filename:
        raise HTTPException(status_code=400, detail="Nenhum arquivo enviado.")

    # Obter e validar extensão
    extensao = os.path.splitext(arquivo.filename)[1].lower()
    if extensao not in EXTENSOES_PERMITIDAS:
        raise HTTPException(
            status_code=400,
            detail=f"Formato de imagem inválido. Formatos permitidos: {', '.join(EXTENSOES_PERMITIDAS)}"
        )

    # Diretório de destino
    diretorio_destino = os.path.join(DIRETORIO_BASE_UPLOADS, subpasta)
    os.makedirs(diretorio_destino, exist_ok=True)

    # Gerar nome único para o arquivo
    nome_arquivo = f"{uuid.uuid4()}{extensao}"
    caminho_completo = os.path.join(diretorio_destino, nome_arquivo)

    # Gravar arquivo
    try:
        with open(caminho_completo, "wb") as buffer:
            shutil.copyfileobj(arquivo.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao salvar arquivo de imagem: {str(e)}")
    finally:
        arquivo.file.close()

    # Retorna o path acessível pela rota estática /uploads/<subpasta>/<arquivo>
    return f"/uploads/{subpasta}/{nome_arquivo}"
