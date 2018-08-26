cover:
	make lint
	make cover_tests

lint:
	flake8 --max-line-length=100 BinaryTree tests

cover_tests:
	py.test -s  --cov-config .coveragerc --cov BinaryTree \
	--no-cov-on-fail \
	--cov-fail-under=100 \
	tests