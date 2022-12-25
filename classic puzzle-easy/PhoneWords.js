//https://www.codewars.com/kata/635b8fa500fba2bef9189473/javascript
//PhoneWords
function phoneWords(s) {
  if(s=='') return '';
  var a=s.match(/([0-9])\1*/g);
  var m='';
  dy={'0':' ','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'};
  for(const x of a)
    if(x[0]!='1'){
        var l=x.length;
        while(l>0){
          if(l>=dy[x[0]].length)
            m+=dy[x[0]][dy[x[0]].length-1];
          else
            m+=dy[x[0]][l%dy[x[0]].length-1]
          l=l-dy[x[0]].length;
        }
     }
    return m;
}
