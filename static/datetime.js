//토큰 유출 방지를 위해 일부 코드가 제거되었습니다.

var Target = document.getElementById("clock");
function clock() {
var time = new Date();
var hours = time.getHours();
var minutes = time.getMinutes();

Target.innerText = `${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}`;
}

var Target2 = document.getElementById("date");
function date() {
var time = new Date();

var month = time.getMonth();
var date = time.getDate();
var day = time.getDay();
var year = time.getYear();
var week = ['일', '월', '화', '수', '목', '금', '토'];

Target2.innerText = `2021년 10월 8일 (금)`;

}
date();
clock();
setInterval(clock, 1000);
setInterval(date, 1000);

function checkin_click(){
    setTimeout(function(){location.href="num";}, 350);
}

function register_click(){
    setTimeout(function(){location.href="regi1";}, 350);
}

jQuery(function($) {
$("body").css("display", "none");
$("body").fadeIn(2000);
$("a.transition").click(function(event){
event.preventDefault();
linkLocation = this.href;
$("body").fadeOut(1000, redirectPage);
});
function redirectPage() {
window.location = linkLocation;
}
});
