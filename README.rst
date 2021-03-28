aioworkers-loki
===============

.. image:: https://github.com/aioworkers/aioworkers-loki/workflows/Tests/badge.svg
  :target: https://github.com/aioworkers/aioworkers-loki/actions?query=workflow%3ATests

.. image:: https://codecov.io/gh/aioworkers/aioworkers-loki/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aioworkers/aioworkers-loki

.. image:: https://img.shields.io/pypi/v/aioworkers-loki.svg
  :target: https://pypi.org/project/aioworkers-loki
  :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/aioworkers-loki.svg
  :target: https://pypi.org/project/aioworkers-loki
  :alt: Python versions


Use
---

.. code-block:: yaml

    logging:
      root:
        handlers: [loki]
      handlers:
        loki:
          host: localhost:3100


Development
-----------

Install dev requirements:


.. code-block:: shell

    poetry install


Run linters:

.. code-block:: shell

    make
