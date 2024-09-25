function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var content = document.getElementById("main-content");
    var burgerMenu = document.getElementById("toggle-button");

    // Toggle the sidebar width
    if (sidebar.style.width === "250px") {
        sidebar.style.width = "0";
        content.classList.remove("shifted");
        burgerMenu.style.color = ""; // Reset color of burger menu
    } else {
        sidebar.style.width = "250px"; 
        burgerMenu.style.color = "white"; // Set color of burger menu to white
        content.classList.add("shifted"); 
    }
}
