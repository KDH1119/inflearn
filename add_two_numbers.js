function dosomething(){
    let a = document.getElementById("inputA").value;
    let b = document.getElementById("inputB").value;
    let c = Number(a) + Number(b);
    if(isNaN(c)){
        alert("잘못된 값을 입력하였습니다.")
        document.getElementById("inputA").value = 0;
        document.getElementById("inputB").value = 0;
        document.getElementById("valueA").innerHTML = 0;
        document.getElementById("valueB").innerHTML = 0;
        document.getElementById("valueC").innerHTML = 0;
    } else {
        document.getElementById("valueA").innerHTML = a;
        document.getElementById("valueB").innerHTML = b;
        document.getElementById("valueC").innerHTML = Number(a) + Number(b);
    }
}