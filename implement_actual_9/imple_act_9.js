
function sol(str){
    let answer  = 0;
    let cnt = 0;
    let str_1 = "";
    let ar1 = [];
    let min = Number.MAX_SAFE_INTEGER;
    let sum = 0;


    for(let i = 1; i <= str.length; i++){
        for(let j = 0; j < str.length; j++){
            if(str_1.length != i){
                str_1 += str[j];
            }else{
                ar1.push(str_1);
                i++;
            }
        }
    }

    for(let k = 0; k < ar1.length; k++){
        let cpy = str;
        for(let x = 0; x < str.length; x++){
            if(ar1[k] == cpy[x]){
                console.log(x);
                x++;
            }else{
                cpy.slice(0,x-1);
                break;
            }
            sum = cpy.length+1;
        }
        if(sum < min){
            min = sum;
        }
      }
      answer = sum;

    return answer;
}

str = "aabbaccc";
str1 = "ababcdcdababcdcd";
str2 = "ababcdcdababcdcd";
console.log(sol(str2));