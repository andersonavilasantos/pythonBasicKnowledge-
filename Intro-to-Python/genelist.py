import sys

def get_genes(infile, outfile):
    """
    Function to extract a list of genes and write to file
    """
    gene_list = []
    with open(infile) as gene:
        tag = False
        for line in gene:
            if line.startswith('name'):
                tag = True
                continue
            if tag:
                items = line.split()
                if len(items) > 0:
                    gene_list.append(items[0])
    gene_list = gene_list[1:-7]
    with open(outfile, 'w') as out:
        for i in gene_list:
            out.write(i + '\n')
    return True

# Protege para só executar via linha de comando
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python genelist.py <input_file> <output_file>")
    else:
        infile = sys.argv[1]
        output = sys.argv[2]
        get_genes(infile, output)
