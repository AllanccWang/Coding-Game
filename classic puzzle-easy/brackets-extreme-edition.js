//https://www.codingame.com/training/easy/brackets-extreme-edition
//BRACKETS, EXTREME EDITION.
function areBracketsBalanced(expr){
    let stack = [];
    for(let i = 0; i < expr.length; i++)
    {
        let x = expr[i];
        if (x == '(' || x == '[' || x == '{'){
            stack.push(x);
            continue;
        }

        if (stack.length == 0)
            return false;
             
        let check;
        switch (x){
        case ')':
            check = stack.pop();
            if (check == '{' || check == '[')
                return false;
            break;
 
        case '}':
            check = stack.pop();
            if (check == '(' || check == '[')
                return false;
            break;
 
        case ']':
            check = stack.pop();
            if (check == '(' || check == '{')
                return false;
            break;
        }
    }
    return (stack.length == 0);
}

const expression = readline();
expr=expression.match(/\W+/gm);
console.log(areBracketsBalanced(expr.join('')));
