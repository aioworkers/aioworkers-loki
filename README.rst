aioworkers-loki
===============

.. image:: https://img.shields.io/pypi/v/aioworkers-loki.svg
  :target: https://pypi.org/project/aioworkers-loki
  :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/aioworkers-loki.svg
  :target: https://pypi.org/project/aioworkers-loki
  :alt: Python versions

About
=====

Integration with `grafana loki <https://grafana.com/docs/loki/latest/>`_.
Works on `python-logging-loki <https://pypi.org/project/python-logging-loki>`_

Use
---

.. code-block:: yaml

    logging:
      version: 1
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
