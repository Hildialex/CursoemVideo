function tabuada() {
    let resp = 0
    let txtNum = document.getElementById("numero").value
    let num = Number(txtNum)
    let escreve = ''
    let saida = document.querySelector("fieldset#resp")
    if (txtNum.length == 0) {
        window.alert('ERRO Digite um número!')
    } else {
        for (let i = 0; i <= 10; i++) {
            let conta = document.createElement("li")
            resp = num * i
            escreve = `${i} X ${num} = ${resp}`
            let linha = document.createElement("br")
            conta = document.createTextNode(escreve)
            saida.appendChild(conta)
            saida.appendChild(linha)
            console.log(`${escreve} escreve`)
            console.log(conta)
        }
    }
} 
/*
Solucao Gunabara
function tabuada(){
    let num = document.getElementById("txtn")
    let tab = document.getElementById("seltab")
    if(num.value.length == 0){
        window.alert('Por favor, digite um numero')
    }else{
        let n = Number(num.alert)
        let c = 1
        tab.innerHTML= ''
        while(c <= 10){
            let item = document.createElement('option')
            item.text = `${n} x ${c} = ${n*c}`
            tab.appendChild(item)
            c++
        }
    }
}
*/