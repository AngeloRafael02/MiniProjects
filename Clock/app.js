
setInterval(function countdown(){
    function getResetDay() {
        var now = new Date();
        var ResetDay = new Date();
            ResetDay.setDate(now.getDate() + (8 - 1 - now.getDay() + 7) % 7 + 1); //Monday
            ResetDay.setHours(4, 0, 0, 0); //4:00 AM
        return ResetDay;
    }
    const now = new Date().getTime();
    const deadLine = new Date(getResetDay()).getTime();
    const gap = deadLine - now;

    const second = 1000;
    const minute = second * 60;
    const hour = minute * 60;
    const day = hour * 24;

    const textDay = Math.floor(gap / day);
    const textHour = Math.floor((gap % day) / hour);
    const textMinute = Math.floor((gap % hour) / minute);
    const textSecond = Math.floor((gap % minute) / second);

    document.querySelector('.day').innerText = textDay;
    document.querySelector('.hour').innerText = textHour;
    document.querySelector('.minute').innerText = textMinute;
    document.querySelector('.second').innerText = textSecond;
},1000);

