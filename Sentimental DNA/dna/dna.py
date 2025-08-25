import csv
import sys

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i + count * sub_len : i + (count + 1) * sub_len] == subsequence:
            count += 1
        if count > longest_run:
            longest_run = count

    return longest_run

def main():
    # Verifica os argumentos da linha de comando
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    database_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    # Lê a base de dados CSV
    with open(database_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        individuals = list(reader)
        str_sequences = reader.fieldnames[1:]  # ignora o campo 'name'

    # Lê a sequência de DNA
    with open(sequence_filename) as file:
        dna_sequence = file.read().strip()

    # Computa os maiores números de repetições consecutivas para cada STR
    str_counts = {}
    for str_seq in str_sequences:
        str_counts[str_seq] = longest_match(dna_sequence, str_seq)

    # Verifica correspondência com algum indivíduo
    for person in individuals:
        match = all(int(person[str_seq]) == str_counts[str_seq] for str_seq in str_sequences)
        if match:
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()
