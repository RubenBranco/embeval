class SemanticSimilarityTask(object):
    def __init__(self, embedding_dir, testset_dir):
        self.embedding_dir = embedding_dir
        self.testset_dir = testset_dir


class SemanticSimilarityTaskData(object):
    def __init__(self, embedding_dir, embedding_file, testset_dir):
        self.embedding_dir = embedding_dir
        self.embedding_file = embedding_file
        self.testset_dir = testset_dir
        self.results = dict()
