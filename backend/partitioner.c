#include <stdio.h>
#include <stdlib.h>

#define MAX_PARTITIONS 10
#define DISK_SIZE 1000

typedef struct
{
    int start;
    int size;
    int used;
} Partition;

Partition partitions[MAX_PARTITIONS];

void init_partitions()
{
    for (int i = 0; i < MAX_PARTITIONS; i++)
    {
        partitions[i].used = 0;
    }
}

int create_partition(int size)
{
    int current = 0;
    for (int i = 0; i < MAX_PARTITIONS; i++)
    {
        if (!partitions[i].used)
        {
            int start = 0;
            for (int j = 0; j < MAX_PARTITIONS; j++)
            {
                if (partitions[j].used)
                {
                    int end = partitions[j].start + partitions[j].size;
                    if (end > start)
                        start = end;
                }
            }
            if (start + size <= DISK_SIZE)
            {
                partitions[i].start = start;
                partitions[i].size = size;
                partitions[i].used = 1;
                return i;
            }
            else
            {
                return -2;
            }
        }
    }
    return -1;
}

int delete_partition(int index)
{
    if (index < 0 || index >= MAX_PARTITIONS || !partitions[index].used)
    {
        return -1;
    }
    partitions[index].used = 0;
    return 0;
}

void get_partitions(int *output)
{
    for (int i = 0; i < MAX_PARTITIONS; i++)
    {
        output[i * 3] = partitions[i].used;
        output[i * 3 + 1] = partitions[i].start;
        output[i * 3 + 2] = partitions[i].size;
    }
}