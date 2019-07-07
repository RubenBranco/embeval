import os

import gensim

from embeval.core.tasks.semantic_similarity import SemanticSimilarityTask, SemanticSimilarityTaskData
from embeval.core.processing.generics import EmbEvalProducer, EmbEvalProcessor, EmbEvalConsumer
from embeval.core.stores.semantic_similarity import SemanticSimilarityStore


class SemanticSimilarityProducer(EmbEvalProducer):
    def init(self):
        pass

    def produce(self, job):
        assert os.path.isdir(job.embedding_dir)
        assert os.path.isdir(job.testset_dir)

        for embedding_file in os.listdir(job.embedding_dir):
            yield self.get_task_data_class()(
                job.embedding_dir,
                embedding_file,
                job.testset_dir,
            )

    def get_task_class(self):
        return SemanticSimilarityTask

    def get_task_data_class(self):
        return SemanticSimilarityTaskData


class SemanticSimilarityProcessor(EmbEvalProcessor):
    def __init__(self):
        self.model = None

    def prepare(self, task_data):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(
            os.path.join(task_data.embedding_dir, task_data.embedding_file),
            binary=task_data.embedding_file.endswith('.bin'),
        )

    def evaluate(self, task_data):
        for testset in os.listdir(task_data.testset_dir):
            testset_name = os.path.splitext(os.path.basename(testset))[0]
            pearson, spearman, oov = self.model.evaluate_word_pairs(
                os.path.join(task_data.testset_dir, testset),
            )
            task_data.results[testset_name] = dict(
                pearson=pearson,
                spearman=spearman,
                oov=oov,
            )


class SemanticSimilarityConsumer(EmbEvalConsumer):
    pass
