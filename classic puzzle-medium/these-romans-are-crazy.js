//https://www.codingame.com/training/medium/these-romans-are-crazy!
//THESE ROMANS ARE CRAZY!
var roman={M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1}
function Roman2Int(rom){
    var num=0,last=0,curr;
    rom.split("").reverse().forEach(e=>{
        curr=roman[e]
        if(curr>=last) num+=roman[e]
        else num-=roman[e]
        last=curr
    })
    return num;
}
function Int2Roman(num){
    var s='';
    for(let i in roman){
        while(num>=roman[i]){
            s+=i;
            num-=roman[i];
        }
    }
    return s;
}
const rom1 = readline();
const rom2 = readline();
var num=Roman2Int(rom1)+Roman2Int(rom2);
console.log(Int2Roman(num))
