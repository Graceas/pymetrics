from collections import defaultdict
from time import time


class Metrics:
    metrics = defaultdict(dict)
    metrics_collect = defaultdict(dict)
    metrics_all = defaultdict(int)

    @staticmethod
    def start(name, partition: int):
        Metrics.metrics[partition][name] = time()

    @staticmethod
    def end(name, partition: int):
        diff = time() - Metrics.metrics[partition][name]
        if name not in Metrics.metrics_collect[partition]:
            Metrics.metrics_collect[partition][name] = 0

        Metrics.metrics_collect[partition][name] += diff
        Metrics.metrics_all[name] += diff
        del Metrics.metrics[partition][name]
        return diff

    @staticmethod
    def clear():
        Metrics.metrics = defaultdict(dict)
        Metrics.metrics_collect = defaultdict(dict)
        Metrics.metrics_all = defaultdict(int)


def metrics(func, name, partition):
    def wrapper():
        Metrics.start(name, partition)
        func()
        Metrics.end(name, partition)

    return wrapper
