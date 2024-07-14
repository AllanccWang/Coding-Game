//https://www.codingame.com/training/medium/sum-of-divisors
//sum-of-divisors
//ref:https://www.geeksforgeeks.org/sum-divisors-1-n/
const n = parseInt(readline());
var s=0;
for(let i=1;i<=n;i++)
    s+=Math.floor(n/i)*i;
console.log(s);
