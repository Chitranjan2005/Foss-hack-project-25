let playerscore = 0;
let compscore = 0;

const icons = document.querySelectorAll(".icon");
const result = document.querySelector("h4");
const showmove = document.querySelector("h3");
const playercount = document.querySelector("#player");
const compcount = document.querySelector("#comp");

const gencompchoice = () => {
    const options = ["rock", "paper", "scissors"];
    return options[Math.floor(Math.random() * options.length)];
};

const draw = () => {
    result.innerText = "GAME IS DRAW, TRY AGAIN";
    result.style.backgroundColor = "#0a0908";
};

const game = (playerchoice) => {
    const compchoice = gencompchoice();
    showmove.innerText = `Computer chose ${compchoice}`; // Display computer's choice
    
    if (playerchoice === compchoice) {
        draw();
    } else {
        let playerwin =
            (playerchoice === "rock" && compchoice === "scissors") ||
            (playerchoice === "scissors" && compchoice === "paper") ||
            (playerchoice === "paper" && compchoice === "rock");

        if (playerwin) {
            result.innerText = "YOU WIN";
            result.style.backgroundColor = "#55a630";
            playerscore++;
            playercount.innerText = playerscore;
        } else {
            result.innerText = "YOU LOSE";
            result.style.backgroundColor = "#dd1c1a";
            compscore++;
            compcount.innerText = compscore;
        }
    }
};

icons.forEach((icon) => {
    icon.addEventListener("click", () => {
        const playerchoice = icon.getAttribute("id");
        game(playerchoice);
    });
});











 