//https://www.codingame.com/training/medium/rubik%C2%AE
//RUBIK®
const N = parseInt(readline())
let ans=N*N*2+((N*2)+2*(N-2))*(N-2)
if(N==1) ans=1
console.log(ans);
