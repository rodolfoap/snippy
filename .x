case "$1" in
	u)	sudo /usr/bin/python3 -m pip uninstall -y snippy
		;;
	i)	sudo /usr/bin/python3 -m pip install .
		;;
	e)	vi -p snippy/tools.py tests/test1.py snippy/experimental/pretty.py bin/snippy Makefile setup.py requirements.txt README.md .x
		;;
	'')	sudo /usr/bin/python3 -m pip show -f snippy
		;;
esac
