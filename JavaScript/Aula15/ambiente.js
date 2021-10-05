let num = [29,23,12,1,2,3,4,5]
//Adiciona na ultima posicao
num.push(9)
//tamanho
num.length
//Ordenar ordem crescente
num.sort()
//Percorrer vetor no javaScript
for(let pos in num){console.log(num[pos])}
//Buscar valores
num.indexOf(23)
console.log(`Nosso vetor [ ${num} ] `)
//Recursividade
function fatorial(n){
    if(n==1){
        return 1
    }else{
        return n * fatorial(n-1)
    }
}