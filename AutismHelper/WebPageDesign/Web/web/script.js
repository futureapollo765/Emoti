function checkAccount() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if(username == '' && password == ''){
        alert("Please Enter Username or Password!");
       
    }
    else{
        window.location = "main.html";
        return false;
    }
}