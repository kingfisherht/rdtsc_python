all: rdtsc.c
	gcc rdtsc.c -fPIC -shared -o rdtsc.so

clean:
	rm rdtsc.so
