//console.log("cześć")
var images = document.querySelectorAll('img')
var index = 0

function showImage(n){
    images[n].classList.add('visible')
}

function hideImage(n){
    images[n].classList.remove('visible')
}

showImage(0)


function update(){
if (index===images.length-1)
    next.disabled = true
    else next.disabled=false

if(index===0)
    prev.disabled=true    
    else prev.disabled=false
}

function goNext(){
    hideImage(index)
    index++
    showImage(index)
    update()
}

function goPrev(){
    hideImage(index)
    index--
    showImage(index)
    update()
}

var next =document.querySelector('#next')
var prev =document.querySelector('#prev')
next.addEventListener('click', goNext)
prev.addEventListener('click', goPrev)

update()
