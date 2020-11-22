function login () {

let login = document.getElementById("login").value;
let password = document.getElementById("password").value;

if ( login === "admin" && password === "admin"){

  window.location.href = "layout.html";}

else {
  window.alert("fail");
}
}
