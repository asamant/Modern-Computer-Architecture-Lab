run matrix -O3
cd ./output-matrix.c
gprof a.out gmon-nocache.out > gmon-nocache.txt
pcntl matrix.s > pcntl.txt