import subprocess
import os
import logging
from Bio.Blast import NCBIWWW, NCBIXML

def run_local_blast(query_file, db_path="bio_project/blastdb/mydb"):
    """
    Motor local: Usa el binario blastn instalado en el sistema.
    """
    output_file = f"bio_project/results/local_res.txt"
    os.makedirs("bio_project/results", exist_ok=True)
    
    command = [
        "blastn",
        "-query", query_file,
        "-db", db_path,
        "-out", output_file,
        "-outfmt", "6",
        "-task", "blastn-short"
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"BLAST Local Error: {result.stderr}")
        
    if os.path.exists(output_file):
        with open(output_file) as f:
            return f.readlines()
    return []

def run_remote_blast(sequence):
    """
    Motor global: Usa la API de NCBI (Biopython).
    """
    print("\n[📡] Conectando con NCBI (Maryland, USA)...")
    result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
    blast_record = NCBIXML.read(result_handle)
    return blast_record.alignments
