#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    int i;
    pid_t pid;

    for (i = 0; i < 5; i++)
    {
        pid = fork();

        if (pid > 0)
        {
            printf("Zombie process created, PID: %d\n", pid);
        }
        else if (pid == 0)
        {
            exit(0);
        }
        else
        {
            perror("Fork error");
            return (1);
        }
    }

    infinite_while();

    return (0);
}
