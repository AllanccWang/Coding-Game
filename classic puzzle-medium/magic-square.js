//https://www.codingame.com/training/medium/magic-square
//magic-square
var map=[...Array(100)].map(e=>Array(100));
var a=new Array(100);

function check_in_array(n){
    for(let i=0;i<n*n;i++)
        if(a[i]!=0)return false;
    return true;
}

const n = parseInt(readline());

for(let i=1;i<=n*n;i++)
    a[i-1]=i;
for (let i = 0; i < n; i++) {
    var inputs = readline().split(' ');
    for (let j = 0; j < n; j++) {
        const c = parseInt(inputs[j]);
        map[i][j]=c;
        a[c-1]=0;// check 1,2,...n*n is distinct and in array
    }
}

if(!check_in_array(n)){
    console.log("MUGGLE");
}else{
    var flag=true;
    var num=0,s=0;
    for(let i=0;i<n;i++) num+=map[0][i];
    //check sum per row
    for(let i=0;i<n;i++){
        s=0;
        for(let j=0;j<n;j++)
            s+=map[i][j];
        if(s!=num){
            flag=false;
            break;
        } 
    }
    //check sum per col
    for(let i=0;i<n;i++){
        s=0;
        for(let j=0;j<n;j++)
            s+=map[j][i];
        if(s!=num){
            flag=false;
            break;
        } 
    }
    //check diagonal sum
    s=0;
    for(let i=0;i<n;i++) s+=map[i][i];
    if(s!=num) flag=false;
    s=0;
    for(let i=0;i<n;i++) s+=map[i][n-i-1];            
    if(s!=num) flag=false;
    if(flag) console.log("MAGIC");
    else console.log("MUGGLE")
}
