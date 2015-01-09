#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<stdlib.h>

int main (int argc, char *argv[]){
	pid_t pid;
	int cnt = 0;

	pid = fork();
	pid = fork();

	printf("pid  is %d\n", pid);
//
//	if(pid == -1){
//		perror("fork error");
//	}else if(pid == 0){
//		printf("The returned value is %d\nIn child process!!\nMy PID is %d\n", pid, getpid());
//		cnt ++;
//	}else{
//		printf("The returned value is %d\nIn father process!!\nMy PID is %d\n", pid, getpid());
//		cnt ++;
//	}
//	printf("cnt = %d\n", cnt);

	return 0;
}
