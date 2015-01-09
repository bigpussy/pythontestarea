#include <unistd.h>
int main()
{ 
	int i;
	while(1)
	{
		for(i = 0; i < 9600000; i++);
			Sleep(10);
	}

	return 0;
}