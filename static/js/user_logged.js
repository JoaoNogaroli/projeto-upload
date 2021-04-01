firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
        var email_user = firebase.auth().currentUser.email;
        var user_id = firebase.auth().currentUser.uid;
        document.getElementById("email").innerHTML = "Logado como: "+ email_user;
        console.log("EMAIL :" + email_user);
        console.log("Usuario ID:" +  user_id);

        document.getElementById("user_id").value = user_id;
        document.getElementById("user_id_dois").value = user_id;


    } else {
        // No user is signed in.
        console.log("ERROR");
  
      }
  });

function vis(){
    console.log("ES")
    var storageRef = storage.ref("File");
    var user_uid = document.getElementById('user_id').value;
    var storage_res =  storageRef.child("user:_"+user_uid);/*.child("análise.xlsx")*/
    /*console.log('File/'+'user:_'+user_uid)*/
    //console.log(storage_res)
    /*var teste = storage_res.getDownloadUrl();
    console.log(teste)*/
    /*storage_res.getDownloadURL().then(function(url) {
        console.log(url);
      });*/
    
    storage_res.listAll().then(function(result) {
        var div_lista = document.getElementById("div_lista");
        var select = document.createElement('select');
        select.id="selecao";
        select.className="form-select";
        
        result.items.forEach(function(imageRef) {
            // And finally display them
            console.log(imageRef);
            console.log(imageRef.name);
            var nome_file = imageRef.name;
            var options = document.createElement('option')
            options.value = nome_file;
            options.id=nome_file
            options.innerHTML=nome_file;
            select.appendChild(options)
            div_lista.appendChild(select);
        });
  });
}

function analise(){
    var escolha = document.getElementById("selecao").value;
    console.log(escolha);
    document.getElementById("filename").value = escolha;
}