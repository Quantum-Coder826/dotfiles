let turn = 1; // 1 indicates circle and 2 indicates cross
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
    console.table(board);

    // update the visual board
    if (turn == 1) {
        elements[1].id = 'circle';
        turn = 2;
    } else if (turn == 2) {
        elements[1].id = 'cross';
        turn = 1;
    };
    turnCount++; // increment the turn counter
    console.log(turnCount);
    checkBoard();
};

function checkBoard() { // will check the board if a player has won.
    for(let i=0; i<=2; i++) {
        let sum = 
    };
};