//https://www.codingame.com/training/easy/prefix-code
var dy={}
const n = parseInt(readline());
for (let i = 0; i < n; i++) {
    var inputs = readline().split(' ');
    const b = inputs[0];
    const c = parseInt(inputs[1]);
    dy[b]=String.fromCharCode(c);
}
const s = readline();
var ans="";
var r=0,l=0;
while (r<s.length){
    var a=s.slice(l, r+1);
    if (dy.hasOwnProperty(a)){
        ans+=dy[a];
        l=r+1;
    }
    r+=1;
}
if (l!=s.length) console.log("DECODE FAIL AT INDEX "+l);
else console.log(ans)
