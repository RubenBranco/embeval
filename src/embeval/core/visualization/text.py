import os

from terminaltables import AsciiTable


def add_headers(table, store):
    headers = ["Testset / Embedding"]
    embeddings = sorted(list(store.results[list(store.results.keys())[0]].keys()))
    headers.extend(embeddings)
    table.append(headers)


def add_results(table, store, metric):
    for testset in store.results:
        line = [testset]
        for embedding in sorted(list(store.results[testset].keys())):
            if metric == "pearson":
                line.append(
                    round(store.results[testset][embedding]['pearson'][0], 2)
                )
            else:
                line.append(
                    round(store.results[testset][embedding]['spearman'].correlation, 2)
                )
        table.append(line)

def semantic_similarity_text(store, output_path):
    assert store.results

    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    spearman_table_data = []
    add_headers(spearman_table_data, store)
    pearson_table_data = []
    add_headers(pearson_table_data, store)

    add_results(spearman_table_data, store, "spearman")
    add_results(pearson_table_data, store, "pearson")

    with open(os.path.join(output_path, "results.txt"), "w") as fw:
        fw.write("*** Spearman's rank correlation coefficient ***\n")
        fw.write(AsciiTable(spearman_table_data).table + "\n\n")
        fw.write("*** Pearson correlation coefficient ***\n")
        fw.write(AsciiTable(pearson_table_data).table + "\n\n")
