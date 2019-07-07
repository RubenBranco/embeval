import os


class SemanticSimilarityStore(object):
    def __init__(self):
        self.results = dict()

    def register(self, task_data):
        for testset in task_data.results:
            if testset not in self.results:
                self.results[testset] = dict()
            embedding_name = os.path.splitext(os.path.basename(task_data.embedding_file))[0]
            self.results[testset][embedding_name] = task_data.results[testset]
