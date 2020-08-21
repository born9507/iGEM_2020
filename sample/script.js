let teamPhotoDesc = document.getElementById("teamPhotoDesc");
let teamphoto1 = document.getElementById("teamphoto1");
let teamphoto2 = document.getElementById("teamphoto2");

function teamDescShow(){
    teamphoto1.style.display = "none"
    teamphoto2.style.display = "block"
    teamPhotoDesc.style.display = "block";
}
function teamDescHide(){
    teamphoto1.style.display = "block"
    teamphoto2.style.display = "none"
    teamPhotoDesc.style.display = "none";
}