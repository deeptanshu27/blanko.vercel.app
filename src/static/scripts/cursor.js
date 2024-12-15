function setupCursor() {
    console.log("daymn")
    document.addEventListener("mousemove", (e) => moveCursor(e));
}

function moveCursor(e) {
    let smallCursor = document.getElementById("small-cursor");
    smallCursor.style.top = (e.pageY - 8) + "px";
    smallCursor.style.left = (e.pageX - 8) + "px";

    let bigCursor = document.getElementById("big-cursor");
    bigCursor.style.top = (e.pageY - 17) + "px";
    bigCursor.style.left = (e.pageX - 17) + "px";
}