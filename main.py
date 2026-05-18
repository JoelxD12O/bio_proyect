import os
import sys
import time
from bio_project.core.blast_engines import run_local_blast, run_remote_blast
from bio_project.core.history_manager import save_to_history, get_history
from bio_project.core.analyzer import analyze_sequence

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    print("""
            ⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀
            ⢸⡇⠈⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣻⠁⢈⡇
            ⠈⣧⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⣸⠃
            ⠀⠘⢧⡀⠘⢷⣶⠶⠶⠶⠶⠶⠶⠶⠶⢶⡾⠋⠀⣴⠋
            ⠀⠀⠈⠻⣦⡀⠈⠳⣤⡀⠀⠀⢀⣠⠞⠋⢀⣠⠞⠁
            ⠀⠀⠀⠀⠈⠙⢦⣀⠀⠙⠷⣶⡋⠁⢀⡴⠛⠁
            ⠀⠀⠀⠀⠀⠀⢀⣹⠷⢦⣀⠀⠙⠻⣯⡀
            ⠀⠀⠀⠀⢠⡶⠋⠀⣀⡴⠟⠛⢦⣄⠀⠙⠷⣄
            ⠀⠀⠀⡴⠋⠀⣠⠞⠁⠀⠀⠀⠀⠈⠻⣦⠀⠘⢧⡀
            ⠀⠀⣼⠁⢀⡼⠗⠒⠒⠒⠒⠒⠒⠒⠒⠚⢷⡀⠈⢷
            ⠀⢰⡇⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠸⡇
            ⠀⢸⠁⠀⣿⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⣾⠀⠀⡇
            ⠀⠸⡇⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⢠⡇
            ⠀⠀⢻⡀⠈⢷⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⡼⠁⢀⡾
            ⠀⠀⠈⢻⣄⠀⠻⣦⡀⠀⠀⠀⠀⢀⣠⠟⠁⢠⡾⠁
            ⠀⠀⠀⠀⠙⢷⣄⠀⠙⠶⣄⣠⠶⠋⠁⢀⡴⠋
            ⠀⠀⠀⠀⠀⠀⠉⢳⣦⠶⠋⠁⢀⣤⡞⠋
            ⠀⠀⠀⠀⠀⣠⠶⠋⠁⣀⡴⢾⣏⠀⠙⠳⣤⡀
            ⠀⠀⠀⣠⠞⠁⢀⣤⠞⠉⠀⠀⠈⠛⢦⡀⠈⠛⣦
            ⠀⢀⡾⠁⢀⣴⣯⣤⣤⣤⣤⣤⣤⣤⣤⣽⣦⡀⠈⢳⡀
            ⠀⣾⠁⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⢿⡀
            ⠀⡇⠀⣼⣁⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿⠀⢸⡇
            ⠀⠳⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠶⠞⠃
    """)
    print("=" * 60)
    print("      BIOPROJECT: PROFESSIONAL GENOMIC SCANNER 🧬")
    print("=" * 60)

def get_sequence_input():
    """
    Sub-menú para elegir entre secuencias predefinidas o entrada manual.
    """
    presets = {
        "1": ("Gen Insulina (Humano)", "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCC"),
        "2": ("Gripe Aviar H5N1 (Fragmento HA)", "ATGGAGAAAATAGTGCTTCTTTTTGCAATAGTCAGTCTTGTTAAAAGTGATCAGATTTGCATTGGTTACCATGCAAACAACTCGACAGAGCAGGTTGACACAATAATGGAAAAGAACGTTACTGTTACACATGCCCAAGACATACTGGAAAAG"),
        "3": ("SARS-CoV-2 (Proteína Spike partial)", "ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAATTACCCCCTGCATACACTAATTCTTTCACACGTGGTGTTTATTACCCTGACAAAGTTTTCAGATCCTCAGTTTTACATTCAACT")
    }

    print("\n--- FUENTE DE SECUENCIA ---")
    print(" 1. Usar Gen Insulina (Humano)")
    print(" 2. Usar Gripe Aviar H5N1")
    print(" 3. Usar SARS-CoV-2")
    print(" 4. Ingresar secuencia manualmente")
    print(" 5. Volver")
    
    choice = input("\nSeleccione una fuente: ").strip()
    
    if choice in presets:
        name, seq = presets[choice]
        print(f"\n[INFO] Seleccionado: {name}")
        return seq
    elif choice == "4":
        return input("\nDNA Sequence > ").strip().upper()
    else:
        return None

def menu_local_scan():
    clear_screen()
    show_header()
    print("[ MODO LOCAL: Búsqueda en Base de Datos Propia ]")
    
    sequence = get_sequence_input()
    if not sequence: return

    print("\n⌛ Ejecutando BLAST Local...")
    try:
        # Crear temp file para el motor local
        os.makedirs("bio_project/queries", exist_ok=True)
        temp_query = f"bio_project/queries/temp.fasta"
        with open(temp_query, "w") as f:
            f.write(f">query\n{sequence}")

        lines = run_local_blast(temp_query)
        
        results_to_log = []
        if lines:
            print(f"\nEXITO: Se encontraron {len(lines)} coincidencias:")
            print(f"{'SUJETO':<25} | {'IDENTIDAD':<10} | {'E-VALUE'}")
            print("-" * 55)
            for line in lines[:5]:
                p = line.split("\t")
                print(f"{p[1]:<25} | {p[2]:<10}% | {p[10]}")
                results_to_log.append({"id": p[1], "identity": p[2], "e_value": p[10]})
        else:
            print("\n[!] No se encontraron coincidencias locales.")
        
        save_to_history("LOCAL", sequence, results_to_log)
        
    except Exception as e:
        print(f"\n[ERROR] Escaneo local: {e}")
    
    input("\nPresione ENTER para continuar...")

def menu_global_scan():
    clear_screen()
    show_header()
    print("[ MODO GLOBAL: Conexión con NCBI Worldwide ]")
    
    sequence = get_sequence_input()
    if not sequence: return

    print("\n[BUSCANDO] Conectando con servidores NCBI (Maryland, USA)")
    print("Esperando respuesta de la cola (30-90 seg)...")
    print("="*50 + "\n")

    try:
        alignments = run_remote_blast(sequence)
        
        results_to_log = []
        if alignments:
            print("\nRESULTADOS ENCONTRADOS:\n")
            print(f"{'ORGANISMO':<50} | {'E-VALUE'}")
            print("-" * 65)
            for align in alignments[:5]:
                hsp = align.hsps[0]
                org = align.title[:48]
                print(f"{org:<50} | {hsp.expect:.1e}")
                results_to_log.append({"org": align.title, "e_value": str(hsp.expect)})
        else:
            print("\n[!] No se encontraron coincidencias a nivel mundial.")
            
        save_to_history("GLOBAL", sequence, results_to_log)
        
    except Exception as e:
        print(f"\n[ERROR] Conexión remota: {e}")
    
    input("\nPresione ENTER para continuar...")

def menu_history():
    clear_screen()
    show_header()
    print("[ HISTORIAL DE BÚSQUEDAS (Formato JSON) ]\n")
    
    history = get_history()
    if not history:
        print("El historial está vacío.")
    else:
        for i, entry in enumerate(reversed(history[-10:])): # Últimos 10
            dt = entry["timestamp"].replace("T", " ")[:19]
            print(f"{i+1}. [{dt}] TIPO: {entry['type']}")
            print(f"   QUERY: {entry['query'][:50]}...")
            print(f"   RECUENTO: {entry['results_count']} hits encontrados.")
            print("-" * 40)
            
    input("\nPresione ENTER para volver al menú...")

def menu_analysis():
    clear_screen()
    show_header()
    print("[ LABORATORIO DE ANÁLISIS DETALLADO ]")
    
    sequence = get_sequence_input()
    if not sequence: return

    print("\n--- INICIANDO ANÁLISIS FUNCIONAL ---")
    data = analyze_sequence(sequence)
    
    print(f"\nLONGITUD:   {data['length']} nucleótidos")
    print(f"CONTENIDO GC: {data['gc_content']:.2f}%")
    print(f"\nTRADUCCIÓN A PROTEÍNA (Aminoácidos):")
    print(f"{data['protein'] if data['protein'] else '[Codón de parada al inicio o secuencia no codificante]'}")
    
    # Explicación científica rápida
    print("\n--- NOTAS CIENTÍFICAS ---")
    if data['gc_content'] > 60:
        print("* Alto contenido GC: Sugiere una secuencia muy estable, típica de algunos extremófilos o virus.")
    elif data['gc_content'] < 40:
        print("* Bajo contenido GC: Común en regiones regulatorias o genomas específicos de bacterias.")
    
    print(f"* Proteína: Se han generado {len(data['protein'])} aminoácidos funcionales antes del primer STOP.")

    input("\nPresione ENTER para volver al menú...")

def main():
    while True:
        clear_screen()
        show_header()
        print(" 1. Escaneo LOCAL (Base de datos propia)")
        print(" 2. Escaneo GLOBAL (NCBI Worldwide)")
        print(" 3. Analizar secuencia DETALLADAMENTE")
        print(" 4. Ver Historial de Búsquedas (Logs JSON)")
        print(" 5. Salir")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            menu_local_scan()
        elif opcion == "2":
            menu_global_scan()
        elif opcion == "3":
            menu_analysis()
        elif opcion == "4":
            menu_history()
        elif opcion == "5":
            print("\n¡Hasta luego bioinformático! 🧬")
            break
        else:
            print("\n[!] Opción no válida.")
            time.sleep(1)

if __name__ == "__main__":
    main()
