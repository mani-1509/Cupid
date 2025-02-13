const gameConfig = {
  type: Phaser.AUTO,
  parent: "gameCanvas",
  width: 800,
  height: 450,
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
  },
  physics: {
    default: "arcade",
    arcade: {
      gravity: { y: 300 },
      debug: false,
    },
  },
  scene: {
    preload: preload,
    create: create,
    update: update,
  },
};

// Check screen width before initializing the game
if (window.innerWidth >= 1024) {
  let game = new Phaser.Game(gameConfig);
} else {
  document.getElementById("screenSizeMessage").classList.remove("hidden");
}

let score = 0; // Initialize score variable here
let scoreText;
let gameObjects = [];

function preload() {
  // Preload assets if needed
}

function create() {
  // Check which game is being played and initialize accordingly
  if (window.location.pathname.includes("ice_breaker")) {
    createIceBreaker(this);
  } else if (window.location.pathname.includes("heart_catcher")) {
    createHeartCatcher(this);
  }
}

function update() {
  // Update logic if needed
}

function createIceBreaker(scene) {
  // Create 9 ice blocks in a 3x3 grid
  for (let i = 0; i < 9; i++) {
    const x = 200 + (i % 3) * 200;
    const y = 100 + Math.floor(i / 3) * 150;

    // Create a block with a love-themed color
    const block = scene.add.rectangle(x, y, 150, 100, 0x87ceeb); // Light blue for ice
    block.setInteractive();
    block.on("pointerdown", () => {
      block.destroy(); // Destroy the block when clicked
      updateScore(1); // Increment the score
    });
    gameObjects.push(block);
  }

  // Display the score
  scoreText = scene.add.text(16, 16, "Score: 0", {
    fontSize: "32px",
    fill: "#ff4da6", // Pink color for the score text
  });
}

function createHeartCatcher(scene) {
  // Create the player (a love-themed paddle)
  const player = scene.add.rectangle(400, 400, 100, 10, 0xff4da6); // Pink paddle
  scene.physics.add.existing(player, false);
  player.body.setCollideWorldBounds(true);

  // Add keyboard controls
  const cursors = scene.input.keyboard.createCursorKeys();

  // Spawn hearts at regular intervals
  scene.time.addEvent({
    delay: 1000, // Spawn a heart every second
    callback: () => {
      const x = Phaser.Math.Between(0, 800); // Random x position
      const heart = scene.add.text(x, 0, "❤️", {
        fontSize: "48px", // Larger heart emoji
      });
      scene.physics.add.existing(heart);
      heart.body.setVelocityY(200); // Fall speed

      // Check for collision between player and heart
      scene.physics.add.overlap(player, heart, () => {
        heart.destroy(); // Destroy the heart on collision
        updateScore(1); // Increment the score
      });
    },
    loop: true, // Repeat indefinitely
  });

  // Display the score
  scoreText = scene.add.text(16, 16, "Score: 0", {
    fontSize: "32px",
    fill: "#ff4da6", // Pink color for the score text
  });

  // Update player movement
  scene.events.on("update", () => {
    if (cursors.left.isDown) {
      player.body.setVelocityX(-550); // Move left
    } else if (cursors.right.isDown) {
      player.body.setVelocityX(550); // Move right
    } else {
      player.body.setVelocityX(0); // Stop moving
    }
  });
}

function updateScore(points) {
  score += points; // Update the score
  scoreText.setText("Score: " + score); // Update the score text in the game
  document.getElementById("scoreDisplay").innerText = score; // Update the score display in HTML

  // Send the score to the server
  fetch("/api/score", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      game_id: window.location.pathname.split("/").pop(), // Get the game ID from the URL
      score: score,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.victory) {
        // Show the victory message if the game is won
        document.getElementById("message").classList.remove("hidden");
        document.getElementById("confessionMessage").textContent = data.message;
      }
    });
}
