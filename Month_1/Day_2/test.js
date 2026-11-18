function printArr(n) {
    let arr = [];

    for (let i = 0; i <= n; i++) {
        if(i%3 === 0 && i%5 === 0) {
            arr.push("thrisFries");
        } else if(i%3 === 0){
            arr.push("thris");
        }else if(i%5 === 0){
            arr.push("Fries");
        }else{
            arr.push(i)
        }
    }
    return arr;
}


const result = printArr(100);
console.log(result);    
