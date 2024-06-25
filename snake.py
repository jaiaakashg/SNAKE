#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import display, HTML

display(HTML('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Snake Game</title>
<style>
    body {
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #000;
    }
    canvas {
        border: 1px solid #fff;
        background-color: #000;
    }
    .scoreboard {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        color: #fff;
        font-size: 24px;
    }
</style>
</head>
<body>
<div class="scoreboard" id="scoreboard">Score: 0</div>
<canvas id="gameCanvas" width="600" height="400"></canvas>
<script>
    const canvas = document.getElementById('gameCanvas');
    const context = canvas.getContext('2d');
    const scoreboard = document.getElementById('scoreboard');

    const gridSize = 20;
    let snake = [{x: 10, y: 10}];
    let direction = {x: 1, y: 0};
    let food = {x: Math.floor(Math.random() * canvas.width / gridSize), y: Math.floor(Math.random() * canvas.height / gridSize)};
    let score = 0;
    let isChangingDirection = false;

    function drawGrid() {
        context.strokeStyle = '#555';
        for (let x = 0; x < canvas.width; x += gridSize) {
            context.beginPath();
            context.moveTo(x, 0);
            context.lineTo(x, canvas.height);
            context.stroke();
        }
        for (let y = 0; y < canvas.height; y += gridSize) {
            context.beginPath();
            context.moveTo(0, y);
            context.lineTo(canvas.width, y);
            context.stroke();
        }
    }

    function drawSnake() {
        context.fillStyle = '#fff';
        for (let segment of snake) {
            context.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize, gridSize);
        }
    }

    function drawFood() {
        context.fillStyle = '#f00';
        context.fillRect(food.x * gridSize, food.y * gridSize, gridSize, gridSize);
    }

    function moveSnake() {
        const newHead = {x: snake[0].x + direction.x, y: snake[0].y + direction.y};

        if (newHead.x === food.x && newHead.y === food.y) {
            score++;
            updateScoreboard();
            placeFood();
        } else {
            snake.pop();
        }

        if (checkCollision(newHead)) {
            resetGame();
            return;
        }

        snake.unshift(newHead);
        isChangingDirection = false;
    }

    function checkCollision(segment) {
        if (segment.x < 0 || segment.x >= canvas.width / gridSize || segment.y < 0 || segment.y >= canvas.height / gridSize) {
            return true;
        }
        for (let part of snake) {
            if (segment.x === part.x && segment.y === part.y) {
                return true;
            }
        }
        return false;
    }

    function placeFood() {
        food = {x: Math.floor(Math.random() * canvas.width / gridSize), y: Math.floor(Math.random() * canvas.height / gridSize)};
    }

    function updateScoreboard() {
        scoreboard.textContent = `Score: ${score}`;
    }

    function resetGame() {
        snake = [{x: 10, y: 10}];
        direction = {x: 1, y: 0};
        score = 0;
        updateScoreboard();
        placeFood();
    }

    function gameLoop() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        drawGrid();
        drawSnake();
        drawFood();
        moveSnake();
        setTimeout(gameLoop, 100);
    }

    window.addEventListener('keydown', function(event) {
        if (isChangingDirection) return;

        switch (event.key) {
            case 'ArrowUp':
                if (direction.y === 0) {
                    direction = {x: 0, y: -1};
                }
                break;
            case 'ArrowDown':
                if (direction.y === 0) {
                    direction = {x: 0, y: 1};
                }
                break;
            case 'ArrowLeft':
                if (direction.x === 0) {
                    direction = {x: -1, y: 0};
                }
                break;
            case 'ArrowRight':
                if (direction.x === 0) {
                    direction = {x: 1, y: 0};
                }
                break;
        }
        isChangingDirection = true;
    });

    gameLoop();
</script>
</body>
</html>
'''))

