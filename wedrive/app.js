document.addEventListener("DOMContentLoaded", () => {
    var myTimer = setInterval(function () {
       
        var countDownDate = new Date("Dec 31, 2023 15:47:00").getTime();
        var now = new Date().getTime();
        var timeLeft = countDownDate - now;
        
        var days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        var hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        let timeBeforeLaunch = `${days} days & ${hours}:${minutes}:${seconds}`
        let dateOfLaunch = document.getElementById('dateOfLaunch');
        dateOfLaunch.innerHTML = "Launching in " + timeBeforeLaunch;

    }, 1000

    )
    // disable the form when timer expires
    if (timeBeforeLaunch === now ){
        let formInfo = document.getElementsByClassName('form-info');
        formInfo.disabled = true;
    }
})
