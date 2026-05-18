import os
import uuid
from bio_project.core.blast_engines import run_local_blast

def main():
    print("🧬 BIO-SCANNER: MODO LOCAL")
    print("Busca en tu base de datos propia (database/sequences.fasta)\n")
    
    sequence = input("DNA Sequence > ").strip().upper()
    if not sequence: return

    # Crear temp query
    os.makedirs("bio_project/queries", exist_ok=True)
    query_path = f"bio_project/queries/local_query_{uuid.uuid4().hex[:6]}.fasta"
    with open(query_path, "w") as f:
        f.write(f">query\n{sequence}")

    try:
        results = run_local_blast(query_path)
        if not results:
            print("[!] No se encontraron coincidencias locales.")
        else:
            print(f"\n{'ID SUJETO':<20} | {'IDENTIDAD':<10} | {'E-VALUE'}")
            print("-" * 45)
            for line in results[:5]:
                parts = line.split("\t")
                print(f"{parts[1]:<20} | {parts[2]:<10}% | {parts[10]}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
