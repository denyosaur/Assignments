class PlayBoggle {
    constructor(boardID) {
        this.totalPoints = 0;
        this.board = $("#" + boardID);
        this.submittedWord = [];
        this.setTimer();
        $("form").on("click", "#sendAnswer", this.checkAnswer.bind(this))

    }

    async setTimer() {
        let timer = 60;
        let countdown = setInterval(() => {
            timer -= 1;
            if (timer >= 0) {
                $("#time").empty().append(`${timer}`);
            } else {
                $(".go-hide").hide();
                clearInterval(countdown);
                $(".left").prepend("<p>Game Over</p>")
                this.postScore();
            }
        }, 1000);
    }

    async checkAnswer(evt) {
        evt.preventDefault();
        $(".status-msg").empty();
        let guess = $("#guess").val();

        if (this.submittedWord.includes(guess)) {
            $(".status-msg").append(`<p>already submitted!</p>`);
            return;
        }

        const res = await axios.get("/check-word", { params: { guess: guess } });
        let msgResult = res.data.result;

        if (msgResult == "ok") {
            $(".status-msg").append(`<p>Good Find!</p>`);
            this.submittedWord.push(guess);
            this.score(guess);
        } else if (msgResult == "not-on-board") {
            $(".status-msg").append(`<p>Not on board.</p>`);
        } else {
            $(".status-msg").append(`<p>Not a real word...</p>`);
        }
    }

    async postScore() {
        const post_score = await axios.post("/high-score", {
            score: this.totalPoints;
        })
        console.log(post_score);
        if (post_score.data.brokeRecord) {
            $(".scoreboard").append("NEW RECORD");
        } else {
            $(".scoreboard").append("didn't break record");
        }
    }

    score(word) {
        this.totalPoints += word.length;
        $(".total-points").empty().append(this.totalPoints);
    }
}



