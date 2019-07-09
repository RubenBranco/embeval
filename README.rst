EmbEval
=======

EmbEval is a framework that aims to provide a way to evaluate
an arbitrary amount of word embeddings in an arbitrary amount
of tasks, in parallel.

To aid with the interpretability of the results, embeval
resorts to graphs to visualize the performance of the different
type of embeddings across each task.

Getting Started
---------------

Installation
^^^^^^^^^^^^

Install embeval with pip:

.. code:: bash

    pip3 install embeval

Usage (Command Line)
^^^^^^^^^^^^^^^^^^^^

.. code:: bash

   embeval --help
       Usage: embeval [OPTIONS] COMMAND [ARGS]...

       Options:
           --help  Show this message and exit.

       Commands:
           semantic-similarity

    embeval semantic-similarity --help
        Usage: embeval semantic-similarity [OPTIONS] EMBEDDING_DIR TESTSET_DIR

        Options:
            --workers INTEGER               Number of worker processes to use.
            --output_path TEXT              Path to write output files to.
            --output_format [text|graph|both]
            --help                          Show this message and exit.

    embeval semantic-similarity --output_path output/ embeddings/ testsets/

Using/Extending EmbEval
-----------------------

To extend the code to include tasks not provided in the current implementation (contributions would be most welcome), n concepts must be implemented:

- Command (See `Semantic Similarity Command`_) -- This is what will make your task available under the CLI and also will *command* the flow of execution when called upon. `Click`_ is used as the CLI package. The entrypoint for an extended application must import the main cli object and register all the available commands (See `main`_).

- Processing Pipeline (See `generics`_ and `Semantic Similarity Pipeline`_ -- This is where the producer, processor and consumer are implemented to execute tasks. The implementation makes use of the library and methodology of `pseq`_.

- Store (See `Semantic Similarity Store`_) -- Simple object to keep track of evaluation results obtained during the processing pipeline.

- Task (See `Semantic Similarity Task`_) -- A task object which encapsulates needed information to be shared in the pipeline, such as paths to files.

- Visualization (See `text visualization`_) -- Defines a method of visualization.

Plans
-----

- ☐ Finish Semantic Similarity visualization.
- ☐ Integrate GLUE tasks via `jiant framework`_.

License
-------

Distributed under GPL-3.0 License. See the `LICENSE`_ file for details.

.. _LICENSE: https://github.com/RubenBranco/embeval/blob/master/LICENSE
.. _Semantic Similarity Command: https://github.com/RubenBranco/embeval/blob/master/src/embeval/core/commands/semantic_similarity.py
.. _Click: https://click.palletsprojects.com/en/7.x/
.. _generics: https://github.com/RubenBranco/embeval/blob/master/src/embeval/core/processing/generics.py
.. _Semantic Similarity Pipeline: https://github.com/RubenBranco/embeval/blob/master/src/embeval/core/processing/semantic_similarity.py
.. _pseq: https://github.com/luismsgomes/pseq
.. _Semantic Similarity Store: https://github.com/RubenBranco/embeval/blob/master/src/embeval/core/stores/semantic_similarity.py
.. _Semantic Similarity Task: https://github.com/RubenBranco/embeval/blob/master/src/embeval/core/tasks/semantic_similarity.py
.. _text visualization: https://github.com/RubenBranco/embeval/blob/master/src/embeval/core/visualization/text.py
.. _main: https://github.com/RubenBranco/embeval/blob/master/src/embeval/main.py
.. _jiant framework: https://github.com/nyu-mll/jiant
