#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    
    while(n!=0 && m!=0){
        int vetor[n];
        int i, j, temp, mod;
        
        for(i=0;i<n;i++){
            scanf("%d", &vetor[i]);
        }
        
        for(i=1;i<n;i++){
            temp = vetor[i];
            mod = vetor[i] % m;
            j = i-1;
            while(j>-1 && vetor[j]%m >= mod){
                
                if(vetor[j]%m == mod){  
                    if(vetor[j] % 2 == 0 && temp % 2 != 0){
                        
                        vetor[j+1] = vetor[j];
                        vetor[j] = temp;                    
                        
                    }else if(vetor[j] % 2 != 0 && temp % 2 != 0 && vetor[j] < temp ){
                        
                        vetor[j+1] = vetor[j];
                        vetor[j] = temp;                    
                        
                    }else if(vetor[j] % 2 == 0 && temp % 2 == 0 && vetor[j] > temp){
                        
                        vetor[j+1] = vetor[j];
                        vetor[j] = temp;                    
                    }
                }else{
                    
                    vetor[j+1] = vetor[j]; 
                    vetor[j] = temp;                        
                    
                }
                j--;
            }
        }
        
        printf("%d %d\n", n, m);
        for(i=0;i<n;i++){
            printf("%d\n", vetor[i]);
        }
        scanf("%d %d", &n, &m);
    }    
    printf("%d %d\n", n, m);
    return 0;
}