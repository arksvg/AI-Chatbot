
// Below function Executes on click of login button.
function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "root" && password == "admin"){
alert ("Login successfully");
window.location = "admin.html"; // Redirecting to other page.
}
else{
alert ("Login Failed");
window.location = "index.html";
}
}