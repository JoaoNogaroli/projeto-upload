var email = document.getElementById("email");
var senha = document.getElementById("senha");

function logar(){
    firebase.auth().signInWithEmailAndPassword(email.value, senha.value)
      .then((user) => {
        // Signed in
        // ...
        var email_user = firebase.auth().currentUser.email;
        window.alert("OK: " + email_user)      

        window.location.replace('/user_logged');

      })
      .catch((error) => {
        window.alert("ERROR")
        var errorCode = error.code;
        var errorMessage = error.message;
      });

}