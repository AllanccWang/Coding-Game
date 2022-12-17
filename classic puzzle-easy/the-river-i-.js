//https://www.codingame.com/training/easy/the-river-i-
//THE RIVER I.
var r1 = parseInt(readline());
var r2 = parseInt(readline());

while(r1!=r2){
    if(r1<r2)
        r1=[...r1.toString()].reduce((x, y)=>{
            return x + parseInt(y);
        },r1);
    else if(r2<r1)
        r2=[...r2.toString()].reduce((x, y)=>{
            return x + parseInt(y);
        },r2);
}
console.log(r1);
