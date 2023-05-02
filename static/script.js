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
        })

        const result = await response.json();
        if (move === "x") {
            outputBox.value += "\n" + result.message;
            setTimeout(() => {
                outputBox.value = "";
            }, 2000); // Clear after 3 seconds
        } else {
            outputBox.value += "\n" + JSON.stringify(result);
        }
        // inputBox.value = "";
    }

});

