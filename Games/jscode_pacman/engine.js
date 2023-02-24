const canvas = document.getElementById("canvas");
const canvasContext = canvas.getContext("2d");
const pacmanFrames = document.getElementById("animation");
const ghostFrames = document.getElementById("ghost");

const DIRECTION_RIGHT = 4;
const DIRECTION_UP = 3;
const DIRECTION_LEFT = 2;
const DIRECTION_BOTTOM = 1;

let createRect = (x, y, width, height, color) => {
    canvasContext.fillStyle = color;
    canvasContext.fillRect(x,y,width,height);
};

let fps = 30;
let pacman;
let oneBlockSize = 20;
let wallSpaceWidth = oneBlockSize/1.5;
let wallOffset = (oneBlockSize - wallSpaceWidth)/2;

let map= [
    [1,1,1,1,1, 1,1,1,1,1, 1, 1,1,1,1,1, 1,1,1,1,1],
    [1,2,2,2,2, 2,2,2,2,2, 1, 2,2,2,2,2, 2,2,2,2,1],
    [1,2,1,1,1, 2,1,1,1,2, 1, 2,1,1,1,2, 1,1,1,2,1],
    [1,2,1,1,1, 2,1,1,1,2, 1, 2,1,1,1,2, 1,1,1,2,1],
    [1,2,2,2,2, 2,2,2,2,2, 1, 2,2,2,2,2, 2,2,2,2,1],
    [1,2,1,1,1, 2,1,2,1,1, 1, 1,1,2,1,2, 1,1,1,2,1],
    [1,2,2,2,2, 2,1,2,2,2, 1, 2,2,2,1,2, 2,2,2,2,1],
    [1,1,1,1,1, 2,1,1,1,2, 2, 2,1,1,1,2, 1,1,1,1,1],
    [0,0,0,0,1, 2,1,2,2,2, 2, 2,2,2,1,2, 1,0,0,0,0],
    [1,1,1,1,1, 2,1,2,1,1, 2, 1,1,2,1,2, 1,1,1,1,1],
    [2,2,2,2,2, 2,2,2,1,2, 2, 2,1,2,2,2, 2,2,2,2,2],
    [1,1,1,1,1, 2,1,2,1,2, 2, 2,1,2,1,2, 1,1,1,1,1],
    [0,0,0,0,1, 2,1,2,1,1, 1, 1,1,2,1,2, 1,0,0,0,0],
    [0,0,0,0,1, 2,1,2,2,2, 2, 2,2,2,1,2, 1,0,0,0,0],
    [1,1,1,1,1, 2,2,2,1,1, 1, 1,1,2,2,2, 1,1,1,1,1],
    [1,2,2,2,2, 2,2,2,2,2, 1, 2,2,2,2,2, 2,2,2,2,1],
    [1,2,1,1,1, 2,1,1,1,2, 1, 2,1,1,1,2, 1,1,1,2,1],
    [1,2,2,2,1, 2,2,2,2,2, 2, 2,2,2,2,2, 1,2,2,2,1],
    [1,1,2,2,1, 2,1,2,1,1, 1, 1,1,2,1,2, 1,2,2,1,1],
    [1,2,2,2,2, 2,1,2,2,2, 1, 2,2,2,1,2, 2,2,2,2,1],
    [1,2,1,1,1, 1,1,1,1,2, 1, 2,1,1,1,1, 1,1,1,2,1],
    [1,2,2,2,2, 2,2,2,2,2, 2, 2,2,2,2,2, 2,2,2,2,1],
    [1,1,1,1,1, 1,1,1,1,1, 1, 1,1,1,1,1, 1,1,1,1,1],
];

let createNewPacman = () => {
    pacman = new Pacman(
        oneBlockSize,
        oneBlockSize,
        oneBlockSize,
        oneBlockSize,
        oneBlockSize/5
    );
};

let gameLoop=()=>{
    update();
    draw();
};

let update = () => {
    pacman.moveProcess();
};

let gameInterval = setInterval(gameLoop, 1000 / fps);

/*
let restartPacmanAndGhosts = () => {
    createNewPacman();
    createGhosts();
};
*/

let draw = () => {
    createRect(0,0,canvas.width,canvas.height,"black");
    drawWalls();

    pacman.draw();
};


let drawWalls = () => {
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[0].length; j++) {
            if(map[i][j] == 1) createRect(
                j * oneBlockSize,
                i * oneBlockSize,
                oneBlockSize,
                oneBlockSize,
                "#3420CA"
            );
            if (j > 0 && map[i][j-1] == 1) createRect(
                j * oneBlockSize,
                i * oneBlockSize + wallOffset,
                wallSpaceWidth + wallOffset,
                wallSpaceWidth,
                "black"
            );
            if (j < map[0].length-1 && map[i][j+1] == 1) createRect(
                j * oneBlockSize + wallOffset,
                i * oneBlockSize + wallOffset,
                wallSpaceWidth + wallOffset,
                wallSpaceWidth,
                "black"
            );
            if (i > 0 && map[i-1][j] == 1) createRect(
                j * oneBlockSize + wallOffset,
                i * oneBlockSize,
                wallSpaceWidth,
                wallSpaceWidth + wallOffset,
                "black"
            );
            if (i < map.length-1 && map[i+1][j] == 1) createRect(
                j * oneBlockSize + wallOffset,
                i * oneBlockSize + wallOffset,
                wallSpaceWidth,
                wallSpaceWidth + wallOffset,
                "black"
            );
            
        }
    }
};

/*
let drawFoods = () => {
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[0].length; j++) {
            if (map[i][j] == 2) {
                createRect(
                    j * oneBlockSize + oneBlockSize / 3,
                    i * oneBlockSize + oneBlockSize / 3,
                    oneBlockSize / 3,
                    oneBlockSize / 3,
                    "#FEB897"
                );
            }
        }
    }
};
*/
/*
let drawScore = () => {
    canvasContext.font = "20px Emulogic";
    canvasContext.fillStyle = "white";
    canvasContext.fillText(
        "Score: " + score,
        0,
        oneBlockSize * (map.length + 1)
    );
};
*/
/*
let drawRemainingLives = () => {
    canvasContext.font = "20px Emulogic";
    canvasContext.fillStyle = "white";
    canvasContext.fillText("Lives: ", 220, oneBlockSize * (map.length + 1));

    for (let i = 0; i < lives; i++) {
        canvasContext.drawImage(
            pacmanFrames,
            2 * oneBlockSize,
            0,
            oneBlockSize,
            oneBlockSize,
            350 + i * oneBlockSize,
            oneBlockSize * map.length + 2,
            oneBlockSize,
            oneBlockSize
        );
    }
};
*/

createNewPacman();
//createGhosts();
gameLoop();

window.addEventListener("keydown",(event)=>{
    let k = event.keyCode;
    setTimeout(()=>{
        if(k == 37|| k == 65){
            pacman.nextDirection = DIRECTION_LEFT;
        } else if(k == 38|| k == 87){
            pacman.nextDirection = DIRECTION_UP;
        } else if(k == 39|| k == 68){
            pacman.nextDirection = DIRECTION_RIGHT;
        } else if(k == 40|| k == 83){
            pacman.nextDirection = DIRECTION_BOTTOM;
        }
    })
});