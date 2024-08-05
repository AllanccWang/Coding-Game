//https://www.codingame.com/training/medium/ip-mask-calculating
//IP MASK CALCULATING
const ip = readline().split("/");
var s='1'.repeat(ip[1])+'0'.repeat(32-ip[1]);
var mask=[];
for(let i=0;i<s.length;i+=8)
    mask.push(parseInt(s.slice(i,i+8),2));
var boardcast=[];
var net=ip[0].split('.').map(Number).map((e, i)=>{
    boardcast.push(((e | ~mask[i]) & 0xff));
    return (e & mask[i]);
});
console.log(net.map(String).join('.'));
console.log(boardcast.map(String).join('.'));
