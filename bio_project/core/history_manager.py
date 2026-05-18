import json
import os
import datetime

LOG_FILE = "bio_project/logs/history.json"

def save_to_history(scan_type, query, results):
    """
    Guarda el registro de la búsqueda en un archivo JSON.
    """
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    # Cargar historial existente
    history = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except (json.JSONDecodeError, IOError):
            history = []

    # Crear nueva entrada
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "type": scan_type,
        "query": query,
        "results_count": len(results),
        "top_hits": results[:3] # Guardamos solo los 3 mejores para no saturar el JSON
    }
    
    history.append(entry)
    
    # Guardar de nuevo
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def get_history():
    """
    Retorna el historial completo desde el JSON.
    """
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []
