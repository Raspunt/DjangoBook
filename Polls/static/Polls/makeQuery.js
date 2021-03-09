


let newParams ;
let checkB ;

function GetParams(){
    newParams = new URLSearchParams(window.location.search);
    checkB = newParams.get('checkB');
}



let sq = localStorage.getItem('SearchPar')

let data = {
    'checkB':checkB,
    'sq':sq
}

alert(`checkB ${checkB} \n sq ${sq}`)

let newp = new URLSearchParams(data)
localStorage.setItem('newParam',newp)



