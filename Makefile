PID = 0

.PHONY: install run rm_qq clean

install:
	pip3 install -U pipenv
	pipenv --three
	pipenv update

run:
	pipenv run qqbot -b .

rm_qq:
	rm "qq(pid${PID})"

clean:
	rm *.pickle
	rm *.db
