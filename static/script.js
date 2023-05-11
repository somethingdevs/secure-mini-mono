document.getElementById("submit").addEventListener("click", async () => {
    const inputBox = document.getElementById("input");
    const outputBox = document.getElementById("output");
    const move = inputBox.value;
    // console.log(move);

    if (move) {
        const response = await fetch("/submit_move", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ move }),
        });

        const result = await response.json();
        outputBox.value += "\n" + result.message.move;
        move.value = "";
    }
});

