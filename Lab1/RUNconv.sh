run convolution_3x3 -O3
cd ./output-convolution_3x3.c
gprof a.out gmon-nocache.out > gmon-nocache.txt
pcntl convolution_3x3.s > pcntl.txt