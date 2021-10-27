//토큰 유출 방지를 위해 일부 코드가 제거되었습니다.

function number_click(s) {
document.getElementById("text").innerHTML = document.getElementById("text").innerHTML + "*";
}

function bs_click() {
document.getElementById("text").innerHTML = document.getElementById("text").innerHTML.slice(0, -1);
}

function conf_click() {
if(document.getElementById("text").innerHTML.length < 3){
document.getElementById("date").innerHTML = '올바른 비밀번호를 입력하세요'
} else {
    setTimeout(function(){location.href="vein";}, 350);
}
}
