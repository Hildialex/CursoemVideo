function repeticao() {
    let txtInicio = window.document.querySelector("input#txtInicio")
    let txtFim = window.document.querySelector("input#txtFim")
    let txtPasso = window.document.querySelector("input#qtdPasso")
    let inicio = Number(txtInicio.value)
    let fim = Number(txtFim.value)
    let passo = Number(txtPasso.value)
    let frase = " "
    let resp = window.document.querySelector("div#resp")
    if (txtFim.value.length == 0 || txtInicio.value.length == 0) {
        resp.innerHTML = "Impossivel contar!"
    } else if (passo <= 0) {
        window.alert('ERRO, Digite valores válidos!')
    } else {
        if (fim < inicio) {
            for (let i = inicio; i >= fim; i -= passo) {
                frase += i
                frase += String.fromCodePoint(0x1F525)
            }
        } else {
            for (let i = inicio; i <= fim; i += passo) {
                frase += i
                frase += String.fromCodePoint(0x1F525)
            }
        }
        //frase += String.fromCodePoint(x1F3C1)
        resp.innerHTML = frase
    }


} 