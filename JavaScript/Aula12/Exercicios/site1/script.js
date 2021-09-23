function carregar() {
    let msg = window.document.getElementById("msg")
    let img = window.document.getElementById("imagem")
    let data = new Date()
    let hora = data.getHours()

    msg.innerHTML = `Agora são ${hora} horas`
    if (hora >= 6 && hora < 12) {
        img.src = 'fotomanha.png'
        document.body.style.background = 'rgba(218, 163, 12, 0.788)'
    } else if (hora > 13 && hora <= 18) {
        img.src = 'fototarde.png'
        document.body.style.background = 'rgba(236, 95, 0, 0.836)'
    } else {
        img.src = 'fotonoite.png'
        document.body.style.background = 'rgba(12, 1, 77, 0.836)'
    }
}