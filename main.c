#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#define TIMES 5
int main(){
  int i;
  double r;
  srand((unsigned)time(NULL));
  for(i=0;i<TIMES;i++){
    r=(double)rand()/(double)RAND_MAX;
    if(r<0.3)printf("あぁ〜 ");
    else if(r<0.5)printf("そっかそか ");
    else if(r<0.7)printf("なるほど，");
    else if(r<0.8)printf("確かに ");
    else if(r<0.9)printf("マジっすか！");
    else printf("いやいやいや... ");
  }
  printf("\n");
}
