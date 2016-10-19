run: db_builder.py
	make clean
	python db_builder.py
	python get_averages.py

clean:
	make -i cleanH

cleanH:
	rm discobandit.db	
	rm *~	

