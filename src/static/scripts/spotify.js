function shorten() {
    try {
        let original_name = document.getElementById("name").innerText;
        let new_name = original_name.length > 16 ? original_name.slice(0, 16) + ".." : original_name;
        document.getElementById("name").innerText = new_name;
    
        let original_artists = document.getElementById("artists").innerText;
        let new_artists = original_artists.length > 20 ? original_artists.slice(0, 20) + ".." : original_artists;
        document.getElementById("artists").innerText = new_artists;
    } catch (e) {
        console.log("No song is currently playing...")
    }
}