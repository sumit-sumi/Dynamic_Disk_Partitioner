#ifndef PARTITIONER_H
#define PARTITIONER_H

void init_partitions();
int create_partition(int size);
int delete_partition(int index);
void get_partitions(int *output);

#endif