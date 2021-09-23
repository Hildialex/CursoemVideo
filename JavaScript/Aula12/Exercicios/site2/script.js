function verificar() {
    let data = new Date()
    let ano = data.getFullYear()
    let fano = document.getElementById("txtAno")
    let res = document.querySelector("div#res")
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert("[ERRO] Verifique os dados digitados!")
    } else {
        let fsex = document.getElementsByName("radSex")
        let idade = ano - Number(fano.value)
        let genero = ''
        let img = document.createElement("img")
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 10) {
                //bebe crianca
                img.setAttribute('src', 'bebehomem.png')
            } else if (idade < 21) {
                //adolescente
                img.setAttribute('src', 'adolescentehomem.png')
            } else if (idade < 50) {
                //adulto
                img.setAttribute('src', 'jovemhomem.png')
            } else {
                img.setAttribute('src', 'idoso.png')
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                img.setAttribute('src', 'bebemulher.png')
            } else if (idade < 21) {
                img.setAttribute('src', 'adolescentemulher.png')
            } else if (idade < 50) {
                img.setAttribute('src', 'jovemmulher.png')
            } else {
                img.setAttribute('src', 'idosa.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos<br>`
        res.appendChild(img)
    }
}