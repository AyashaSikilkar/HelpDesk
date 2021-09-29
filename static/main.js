const copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click',()=>{
    const mobile= btn.getAttribute('data-mobileno')
    navigator.clipboard.writeText(mobile)

    navigator.clipboard.readText().then(cliptext =>{
    console.log(cliptext)
    btn.textContent = `Copied No- ${cliptext}`    

    })

    if (previous)
    {
        previous.textContent = 'Copy Number'
    }
    previous = btn
}))
