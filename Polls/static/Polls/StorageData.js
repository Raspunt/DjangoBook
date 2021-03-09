
const MyParams = new URLSearchParams(window.location.search)
const queryUrl = window.location.pathname


let  genreId = localStorage.getItem('genreId')
let AuthorId = localStorage.getItem('authorId')




sq = localStorage.setItem('SearchPar', MyParams.get('sq'))
checkB = localStorage.setItem('checkB',MyParams.get('checkFilter'))




function setGenre(genre){
    let check = $(`.filtBtnG${genre}`).prop('checked') 

    if (check){
        if ( !genreIdArr.includes(genre) ){
            genreIdArr.push(genre);
        }
        

    } else {
        const index = genreIdArr.indexOf(genre);

        if (index > -1) {
            genreIdArr.splice(index, 1);
        }

    }
    
genreId = localStorage.setItem('genreId',genreIdArr);
console.log(check + " " + genreIdArr.indexOf(genre));
}

function setAuthor(author){
    let check = $(`.filtBtnA${author}`).prop('checked') 

if (check) {
    if ( !authorIdArr.includes(author) ){
        authorIdArr.push(author)
    }


}else {
    const index = authorIdArr.indexOf(author);

    if (index > -1){
        authorIdArr.splice(index,1)
    }
}

AuthorId = localStorage.setItem('authorId',authorIdArr)

}




