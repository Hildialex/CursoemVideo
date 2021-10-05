let txtValor = document.querySelector("#txtvalor")
let lista = document.querySelector("#resp")
let resp = document.querySelector("#resp2")
let valores = []

function isNumero(n) {
    if (Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}
function inLista(n, l) {
    if (l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}
function adicionar() {
    let opt = document.createElement("option")
    if (isNumero(txtValor.value) && !inLista(txtValor.value, valores)) {
        valores.unshift(Number(txtValor.value))
        opt.textContent = `Valor ${txtValor.value} adicionado`
        lista.appendChild(opt)
        resp.innerHTML = ''
    } else {
        window.alert('Número branco, inválido ou já encontrado na lista!')
    }
    txtValor.value = ''
    txtValor.focus()
}
function verificar() {
    if (valores.length == 0) {
        window.alert('Adicione valores primeiramente')
    } else {
        let tot = valores.length
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0 
        for(let pos in valores){
            soma += valores[pos]
            if(maior < valores[pos]){
                maior = valores[pos]
            }
            if(menor > valores[pos]){
                menor = valores[pos]
            }
            media = soma/tot
        }
        resp.innerHTML = ''
        resp.innerHTML = `<p> Ao todo, foram adicionados ${tot} números.</p>`
        resp.innerHTML += `<p> O maior valor foi: ${maior}.</p>`
        resp.innerHTML += `<p> O menor valor foi: ${menor}.</p>`
        resp.innerHTML += `<p> A soma dos valores: ${soma}.</p>`
        resp.innerHTML += `<p> A média foi: ${media}.</p>`
    }
} 
