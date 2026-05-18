import logging
from bio_project.core.blast_engines import run_remote_blast

# Configurar logs
logging.basicConfig(filename="bio_project/logs/remote.log", level=logging.INFO)

def main():
    print("🌍 BIO-SCANNER: MODO GLOBAL (NCBI)")
    print("Escaneando contra toda la base de datos mundial...\n")
    
    sequence = input("DNA Sequence > ").strip().upper()
    if not sequence: return

    try:
        alignments = run_remote_blast(sequence)
        if not alignments:
            print("[!] Sin coincidencias globales.")
            return

        print("\n✅ RESULTADOS GLOBALES:\n")
        print(f"{'ORGANISMO':<55} | {'E-VALUE'}")
        print("-" * 65)
        
        for align in alignments[:8]:
            hsp = align.hsps[0]
            print(f"{align.title[:53]:<55} | {hsp.expect:.1e}")
            logging.info(f"Global Hit: {align.title} | E-value: {hsp.expect}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
