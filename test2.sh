
export PRJ_ICDIR=/home/liuyunqi/tree/pcpp
./fexpand -i ./fexpand_test/test2/top.f -o res.o -D SUB3 -D SUB1 -D OPEN_SUB
./fexpand -i ./fexpand_test/test2/top.f -o res_v.o -D SUB3 -D SUB1 -D OPEN_SUB -oh res_vhd.o