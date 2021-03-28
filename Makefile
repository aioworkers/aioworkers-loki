
all: aioworkers_loki
	isort $<
	black $<
	mypy --ignore-missing-imports $<
