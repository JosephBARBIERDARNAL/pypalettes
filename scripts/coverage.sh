uv run coverage run --source=pypalettes -m pytest
uv run coverage report -m
uv run coverage xml
uv run genbadge coverage -i coverage.xml
rm coverage.xml
mv coverage-badge.svg docs/coverage-badge.svg
