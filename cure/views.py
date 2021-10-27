# Team DEBUGGERS 2021, Project CURE

# Django Views

# Latest update : 2021.10.19
# Developer : LEE Seok Ho

from django.shortcuts import render
import hardware

def index(request): #메인 화면
    return render(request, 'cure/main.html')

def regikeypad1(request): #가입 화면 1
    hardware.sound('start')
    return render(request, 'cure/regikeypad1.html')

def regikeypad2(request): #가입 화면 2
    hardware.sound('ding')
    return render(request, 'cure/regikeypad2.html')

def vein(request): #정맥 등록
    hardware.sound('ding')
    return render(request, 'cure/vein.html')

def veincomplete(request): #정맥 등록 완료
    hardware.sound('dong')
    hardware.led('blue')
    hardware.sanitizer()
    return render(request, 'cure/veincomplete.html')

def numpad(request): #비회원 체크인
    hardware.sound('start')
    return render(request, 'cure/numkeypad.html')

def temp(request): #체온 측정
    hardware.sound('ding')
    return render(request, 'cure/temp.html')

def tempcomplete(request): #체온 측정 완료
    context = {'temp': hardware.temp()}
    hardware.sanitizer()
    return render(request, 'cure/tempcomplete.html', context)
