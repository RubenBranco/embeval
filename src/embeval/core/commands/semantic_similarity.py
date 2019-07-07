from multiprocessing import Queue
import os
import pickle

import click
from pseq.poly import PolymorphicParallelSequenceProcessor

from embeval.core.processing.semantic_similarity import SemanticSimilarityProducer, SemanticSimilarityProcessor, SemanticSimilarityConsumer
from embeval.core.commands import cli
from embeval.core.stores.semantic_similarity import SemanticSimilarityStore
from embeval.core.tasks.semantic_similarity import SemanticSimilarityTask
from embeval.core.visualization.text import semantic_similarity_text


def restore_store():
    store_fname = os.path.join(os.getcwd(), "tmp_store.pkl")

    with open(store_fname, "rb") as fr:
        store = pickle.load(fr)
    os.remove(store_fname)

    return store


def generate_text_output(store, output_path):
    semantic_similarity_text(store, output_path)


def generate_graph_output(store, output_path):
    raise NotImplementedError


def generate_output(store, output_path, output_format):
    if output_format in ["text", "both"]:
        generate_text_output(store, output_path)
    if output_format in ["graph", "both"]:
        generate_graph_output(store, output_path)


@click.command()
@click.argument('embedding_dir')
@click.argument('testset_dir')
@click.option("--workers", default=2, help="Number of worker processes to use.")
@click.option("--output_path", default=os.path.join(os.getcwd(), "evaluation"), help="Path to write output files to.")
@click.option("--output_format", default="both", type=click.Choice(['text', 'graph', 'both']))
def semantic_similarity(
    embedding_dir,
    testset_dir,
    workers,
    output_path,
    output_format
    ):

    q = Queue()
    q.put(SemanticSimilarityTask(embedding_dir, testset_dir))

    processor = PolymorphicParallelSequenceProcessor(q, workers)
    processor.register(
        SemanticSimilarityProducer(),
        SemanticSimilarityProcessor(),
        SemanticSimilarityConsumer(SemanticSimilarityStore()),
    )
    processor.start()
    processor.join()

    store = restore_store()
    generate_output(store, output_path, output_format)
