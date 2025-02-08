const canvas = document.getElementById("canvas");
const canvasContext = canvas.getContext("2d");

const fps = 60;
count = 0;
speed = 0;
score = 0;
highest_score = 0;
playing = true;
var refreshId;

class Snake {
    constructor(x,y,size) {
        this.x = x;
        this.y = y;
        this.size = size;                           // Size of each rectangular
        this.tail = [ {x: this.x , y: this.y} ];    // List: Tail (First element) -> Head (Last element)
        this.rotateX = 0;
        this.rotateY = 1;
    };

    move() {
        let newRect;
        if (this.rotateX == 1) {
            newRect = {
                x: this.tail[this.tail.length - 1].x + this.size,
                y: this.tail[this.tail.length - 1].y
            };
        }
        if (this.rotateX == -1) {
            newRect = {
                x: this.tail[this.tail.length - 1].x - this.size,
                y: this.tail[this.tail.length - 1].y
            };
        }
        if (this.rotateY == 1) {
            newRect = {
                x: this.tail[this.tail.length - 1].x,
                y: this.tail[this.tail.length - 1].y + this.size
            };
        }
        if (this.rotateY == -1) {
            newRect = {
                x: this.tail[this.tail.length - 1].x,
                y: this.tail[this.tail.length - 1].y - this.size
            };
        }
        this.tail.shift();          // Delete first element
        this.tail.push(newRect);    // Add at the end
    }
}
class Apple {
    constructor() {
        let isTouching;
        while (true) {
            isTouching = false;
            this.x = Math.floor(Math.random() * canvas.width/snake.size) * snake.size;
            this.y = Math.floor(Math.random() * canvas.height/snake.size) * snake.size;
            for (var i = 0; i < snake.tail.length; i++) {
                if (this.x == snake.tail[i].x && this.y == snake.tail[i].y)
                    isTouching = true;
            }
            this.size = snake.size;
            this.color = "red";
            if (!isTouching) break;
        }
    };
}

let snake = new Snake(20, 20, 20);
let apple = new Apple();

window.onload = () => {
    gameLoop();
}
canvas.addEventListener("click", (event) => {
    if (!playing) {
        let rect = canvas.getBoundingClientRect();
        let x = event.clientX - rect.left;
        let y = event.clientY - rect.top;

        // Check if click is inside the replay button
        if (
            x >= canvas.width / 2 - 60 &&
            x <= canvas.width / 2 + 60 &&
            y >= canvas.height / 2 + 30 &&
            y <= canvas.height / 2 + 70
        ) {
            restartGame();
        }
    }
});

function gameLoop() {
    refreshId = setInterval(show, 1000/fps);
}

function show() {
    count++;
    if (count == 10 - speed) update();
    else if (count > 10 - speed) count = 0;
    draw();
    if (!playing) clearInterval(refreshId);
}

function update() {
    canvasContext.clearRect(0, 0, canvas.width, canvas.height);
    // console.log("update");
    snake.move();
    checkHitWall();
    checkHitSelf();
    eatApple();
}

function checkHitSelf() {
    let hit = false;
    let snake_head = snake.tail[snake.tail.length - 1];

    // function duplicates(element) {
    //     return element.x == snake_head.x && element.y == snake_head.y;
    // }
    // let collision = arr => arr.filter(duplicates);
    let collision = arr => arr.filter(element => element.x == snake_head.x && element.y == snake_head.y);
    if (collision(snake.tail).length > 1) hit = true;
    
    if (hit == true) {
        count = 0;
        speed = 0;
        playing = false;
    }
}

function eatApple() {
    if (snake.tail[snake.tail.length - 1].x == apple.x &&
        snake.tail[snake.tail.length - 1].y == apple.y) {
            snake.tail.unshift({x: snake.tail[0].x, y: snake.tail[0].y})
            apple = new Apple();
            if (speed != 6 && snake.tail.length % 5 == 0) speed++;
    }
}

function checkHitWall() {
    let snake_head = snake.tail[snake.tail.length - 1]

    if (snake_head.x == - snake.size) {
        snake_head.x = canvas.width - snake.size
    } else if (snake_head.x == canvas.width) {
        snake_head.x = 0
    } else if (snake_head.y == - snake.size) {
        snake_head.y = canvas.height - snake.size
    } else if (snake_head.y == canvas.height) {
        snake_head.y = 0 
    }
}

function draw() {
    createRect(0, 0, canvas.width, canvas.height, "black");

    score = snake.tail.length - 1
    canvasContext.font = "20px Arial";
    canvasContext.fillStyle = "#00FF42";
    canvasContext.fillText(
        "Score: " + (score),
        canvas.width - 70 - ((snake.tail.length - 1).toString().length)*10,
        18
    );

    (highest_score < score) && (highest_score = score);
    canvasContext.font = "20px Arial";
    canvasContext.fillStyle = "#00FF42";
    canvasContext.fillText(
        "Highest Score: " + (highest_score),
        5,
        18
    );

    // createRect(0, 0, canvas.width, canvas.height);
    for (var i = 0; i < snake.tail.length; i++) {
        createRect(
            snake.tail[i].x + 2.5,
            snake.tail[i].y + 2.5,
            snake.size - 5,
            snake.size - 5,
            "white"
        );
    }

    createRect(
        apple.x,
        apple.y,
        apple.size,
        apple.size,
        apple.color
    );

    // If Game Over, Show Replay Screen
    if (!playing) {
        canvasContext.fillStyle = "rgba(0, 0, 0, 0.7)"; // Semi-transparent black overlay
        canvasContext.fillRect(0, 0, canvas.width, canvas.height);

        // Display Game Over Text
        canvasContext.fillStyle = "white";
        canvasContext.font = "30px Arial";
        canvasContext.fillText(
            "Game Over!",
            canvas.width / 2 - 80,
            canvas.height / 2 - 50
        );

        // Display Highest Score
        canvasContext.font = "20px Arial";
        canvasContext.fillStyle = "#00FF42";
        canvasContext.fillText(
            "Highest Score: " + highest_score,
            canvas.width / 2 - 80,
            canvas.height / 2 - 10
        );

        // Display Highest Score
        canvasContext.font = "20px Arial";
        canvasContext.fillStyle = "#00FF42";
        canvasContext.fillText(
            "Score: " + score,
            canvas.width / 2 - 80,
            canvas.height / 2 + 20
        );

        // Display Replay Button
        canvasContext.fillStyle = "#00FF42";
        canvasContext.fillRect(canvas.width / 2 - 60, canvas.height / 2 + 40, 120, 40);

        canvasContext.fillStyle = "black";
        canvasContext.font = "20px Arial";
        canvasContext.fillText(
            "Replay",
            canvas.width / 2 - 30,
            canvas.height / 2 + 65
        );
    }
}

function createRect(x, y, width, height, color) {
    canvasContext.fillStyle = color;
    canvasContext.fillRect(x, y, width, height);
}

window.addEventListener("keydown", (event) => {
    setTimeout(() => {
        if (event.keyCode == 37 && snake.rotateX != 1) {            //left
            snake.rotateX = - 1;
            snake.rotateY = 0;
        } else if (event.keyCode == 38 && snake.rotateY != 1) {     //up
            snake.rotateX = 0;
            snake.rotateY = - 1;
        } else if (event.keyCode == 39 && snake.rotateX != -1) {    //right
            snake.rotateX = 1;
            snake.rotateY = 0;
        } else if (event.keyCode == 40 && snake.rotateY != -1) {    //down
            snake.rotateX = 0;
            snake.rotateY = 1;
        }
    }, 1);
});

function restartGame() {
    snake = new Snake(20, 20, 20); // Reset snake
    apple = new Apple(); // Generate new apple
    playing = true; // Set playing to true
    count = 0;
    speed = 0;
    gameLoop(); // Restart game loop
}
