//https://www.codingame.com/training/hard/the-greatest-number
//THE GREATEST NUMBER
const N = parseInt(readline());
const s = readline();
var a=s.match(/[0-9]/gm);
var num;
if(s.includes('-')){
    num='-'+a.sort((a,b)=>a-b).join('');
    if(s.includes("."))
        num=num.slice(0,2)+"."+num.slice(2,)
}else{
    num=a.sort((a,b)=>b-a).join('');
    if(s.includes("."))
        num=num.slice(0,-1)+"."+num.slice(-1)
}
console.log(parseFloat(num).toString());
