
function factorial(num){
    if (num<0){
        console.log(0)
    }
    else if (num==0 || num==1){
        console.log(1)
    }
    else{
        fact=1
        while(num>1){
            fact=fact*num
            num=num-1
    }
    console.log(fact)
    }
  }

factorial(7)