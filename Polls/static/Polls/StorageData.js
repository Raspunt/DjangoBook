
const MyParams = new URLSearchParams(window.location.search)
const queryUrl = window.location.pathname


let paramText = localStorage.getItem('countRefresh')
let sq = localStorage.getItem('sq')
let genre_id = localStorage.getItem('genre_id')


console.log(sq);
console.log(MyParams.get('genre_id') != null);

console.log(paramText);








if (queryUrl == '/filter/' && MyParams.get('sq') != null  ){
    window.location.href = '/';
    localStorage.setItem('sq',MyParams.get('sq'));
    queryUrl = '/'
} else if (queryUrl == '/' && MyParams.get('sq') == null){
    window.location.search = `?sq=${sq}`
    console.log("log  ебучий");
}

