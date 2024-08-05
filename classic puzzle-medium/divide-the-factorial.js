//https://www.codingame.com/training/medium/divide-the-factorial
//DIVIDE THE FACTORIAL
var inputs = readline().split(' ');
var A = parseInt(inputs[0]);
var B = parseInt(inputs[1]);
var a=[];
function primeCheck(num){
	for(let i=2;i<num;i++)
		if(num%i==0) return false;
	return true;
}
while(A!=1){
	let i;
	for(i=2;i<A;i++)
		if(primeCheck(i) && A%i==0)
			break
	let count=0;
	while(A%i==0){
		A/=i;
		count++;
	}
	a.push([i,count])
}
var b=a.map(e=>{
	let [t,qi]=[1,0];
	while(t<B){
		qi+=parseInt(B/(t*=e[0]));
	}
	return parseInt(qi/e[1]);
})
console.log(Math.min(...b));
