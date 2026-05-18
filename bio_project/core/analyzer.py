from Bio.Seq import Seq

def calculate_gc_content(sequence):
    """Calcula el porcentaje de Guanina y Citosina en la secuencia."""
    if not sequence: return 0.0
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def translate_dna(sequence):
    """Traduce una secuencia de ADN a proteína (aminoácidos)."""
    try:
        dna_seq = Seq(sequence.upper())
        # to_stop=True detiene la traducción en el primer codón de parada
        protein_seq = dna_seq.translate(to_stop=True)
        return str(protein_seq)
    except Exception as e:
        return f"Error en traducción: {e}"

def analyze_sequence(sequence):
    """Realiza un análisis funcional completo de la secuencia."""
    analysis = {
        "length": len(sequence),
        "gc_content": calculate_gc_content(sequence),
        "protein": translate_dna(sequence)
    }
    return analysis
