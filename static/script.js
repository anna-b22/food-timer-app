function startTimer(minutes) {
    let time = minutes * 60;
    const timerDisplay = document.getElementById("timer");

    const countdown = setInterval(() => {
        let min = Math.floor(time / 60);
        let sec = time % 60;
        timerDisplay.textContent = `${min}:${sec < 10 ? "0" : ""}${sec}`;
        if (time <= 0) {
            clearInterval(countdown);
            alert("Time's up!");
        }
        time--;
    }, 1000);
}