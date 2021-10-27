//토큰 유출 방지를 위해 일부 코드가 제거되었습니다.

function number_click(s) {
if(document.getElementById("text").innerHTML == ' '){
    document.getElementById("text").innerHTML = s;
    } else if(document.getElementById("text").innerHTML.length > 12){
    } else{
        document.getElementById("text").innerHTML = document.getElementById("text").innerHTML + s;
        if(document.getElementById("text").innerHTML.length == 3){
            document.getElementById("text").innerHTML = document.getElementById("text").innerHTML + " ";
        } else if(document.getElementById("text").innerHTML.length == 7){
            document.getElementById("text").innerHTML = document.getElementById("text").innerHTML + " ";
        } else if(document.getElementById("text").innerHTML.length == 13){
            var pnb = document.getElementById("text").innerHTML.replaceAll(/(\s*)/g,"");
            var pnb1 = pnb.substring(0, 3);
            var pnb2 = pnb.substring(3, 7);
            var pnb3 = pnb.substring(7, 11);
            document.getElementById("text").innerHTML = pnb1 + " " + pnb2 + " " + pnb3;
        }
    }
}

function bs_click() {
if(document.getElementById("text").innerHTML == ' '){
} else if(document.getElementById("text").innerHTML.length == 4){
    document.getElementById("text").innerHTML = document.getElementById("text").innerHTML.slice(0, -2)
} else if(document.getElementById("text").innerHTML.length == 8){
    document.getElementById("text").innerHTML = document.getElementById("text").innerHTML.slice(0, -2)
} else if(document.getElementById("text").innerHTML.length == 13){
    var pnb = document.getElementById("text").innerHTML.replaceAll(/(\s*)/g,"");
    var pnb1 = pnb.substring(0, 3);
    var pnb2 = pnb.substring(3, 6);
    var pnb3 = pnb.substring(6, 10);
    document.getElementById("text").innerHTML = pnb1 + " " + pnb2 + " " + pnb3;
} else {
    document.getElementById("text").innerHTML = document.getElementById("text").innerHTML.slice(0, -1);
}
}

function conf_click() {
if(document.getElementById("text").innerHTML.length < 11){
document.getElementById("date").innerHTML = '올바른 전화번호를 입력하세요'
} else {
    setTimeout(function(){location.href="temp";}, 350);
}
}
