let turn = 1; // 1 indicates circle and 10 indicates cross
let turnCount = 0; // count the amount of turns

let board = [ // this multidimensinoal arry will contain the board state.
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
];

function buttonPressed(x, y) {
    let elements = document.getElementById("pos:" + x + "," + y).children;
    elements[0].style.display = 'none';
    elements[1].style.display = 'block';
    // update the real board
    board[y][x] = turn;
    console.table({board});

    // update the visual board
    if (turn == 1) {
        elements[1].id = 'circle';
        turn = 10;
    } else if (turn == 10) {
        elements[1].id = 'cross';
        turn = 1;
    };
    turnCount++; // increment the turn counter
    console.log({turnCount});
    checkBoard();
};

function checkBoard() { // will check the board if a player has won.
    // go tru the board rows and check for a win
    for(i=0;i<=2;i++) {
        let sum = board[i][0] + board[i][1] + board[i][2]
        console.log({sum})
        checkWin(sum)
    };

    // go tru the board columbs and check for a win
    for(i=0;i<=2;i++) {
        let sum = board
    };
};

function checkWin(num) {
    if (num == 3) {
        console.log("circle won!!")
    } else if (num == 30) {
        console.log("cross won!!")
    };
};