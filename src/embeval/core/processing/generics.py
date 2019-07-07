import os
import pickle

from pseq.poly import JobProducer
from pseq.core import Consumer, Processor


class EmbEvalProducer(JobProducer):
    def get_job_class(self):
        """
            Adapting pseq method to word embedding
            terminology.
        """
        return self.get_task_class()

    def get_task_class(self):
        raise NotImplementedError

    def get_data_class(self):
        """
            Adapting pseq method to word embedding
            terminology.
        """
        return self.get_task_data_class()

    def get_task_data_class(self):
        raise NotImplementedError


class EmbEvalProcessor(Processor):
    def process(self, task_data):
        self.prepare(task_data)
        self.evaluate(task_data)

    def prepare(self, task_data):
        raise NotImplementedError

    def evaluate(self, task_data):
        raise NotImplementedError


class EmbEvalConsumer(Consumer):
    def __init__(self, eval_store):
        self.eval_store = eval_store

    def consume(self, task_data, _, e):
        self.eval_store.register(task_data)

    def shutdown(self):
        with open(os.path.join(os.getcwd(), "tmp_store.pkl"), "wb") as fw:
            pickle.dump(self.eval_store, fw)
