case "$1" in
	u)	sudo /usr/bin/python3 -m pip uninstall -y snippy
		;;
	i)	sudo /usr/bin/python3 -m pip install .
		;;
	t)	make test;
		;;
	e)	vi -p snippy/__init__.py tests/test1.py snippy/experimental/__init__.py snippy/tensorflow/__init__.py bin/snippy.example Makefile setup.py requirements.txt README.md .x
		;;
	'')	sudo /usr/bin/python3 -m pip show -f snippy
		;;
esac
