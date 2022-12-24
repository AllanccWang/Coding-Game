//https://www.codingame.com/training/easy/credit-card-verifier-luhns-algorithm
//CREDIT CARD VERIFIER (LUHN’S ALGORITHM)
const n = parseInt(readline());
for (let i = 0; i < n; i++) {
    const card = readline().split(' ').reverse().map(e=>{
        var a=parseInt(e[0])*2;
        var b=parseInt(e[2])*2;
        var c=parseInt(e[1])+parseInt(e[3]);
        if(a.toString().length==2) a-=9
        if(b.toString().length==2) b-=9
        return [a,b,c]
    }).flat(1).reduce((acc,curr)=>acc+curr,0);
    console.log(card%10?"NO":"YES");
}
