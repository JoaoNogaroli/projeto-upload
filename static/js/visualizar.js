firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
        var email_user = firebase.auth().currentUser.email;
        var user_id = firebase.auth().currentUser.uid;
        document.getElementById("email").innerHTML = "Olá "+ email_user;
        console.log("EMAIL :" + email_user);
        console.log("Usuario ID:" +  user_id);

        //document.getElementById("user_id_dois").value = user_id;
        document.getElementById("user_id_tres").value = user_id;


    } else {
        // No user is signed in.
        console.log("ERROR");
  
      }
  });

function vis(){
    var button = $('#botao_vis');

    button.prop('disabled', true);
    console.log("ES")
    var storageRef = storage.ref("File");
    var user_uid = document.getElementById('user_id_tres').value;
    var storage_res =  storageRef.child("user:_"+user_uid);/*.child("análise.xlsx")*/
    /*console.log('File/'+'user:_'+user_uid)*/
    //console.log(storage_res)
    /*var teste = storage_res.getDownloadUrl();
    console.log(teste)*/
    /*storage_res.getDownloadURL().then(function(url) {
        console.log(url);
      });*/
    
    storage_res.listAll().then(function(result) {
        /*var div_lista = document.getElementById("div_lista");
        var select = document.createElement('select');
        select.id="selecao";
        select.className="form-select";
        */
        //--------teste
        divteste = document.getElementById("row");
                
        result.items.forEach(function(imageRef) {
            // And finally display them
            /*console.log(imageRef);
            console.log(imageRef.name);
            var nome_file = imageRef.name;
            var options = document.createElement('option')
            options.value = nome_file;
            options.id=nome_file
            options.innerHTML=nome_file;
            select.appendChild(options)
            div_lista.appendChild(select);*/

            //--------teste
            divteste_dois = document.createElement('div');
            divteste_dois.className = "col-sm";
            divteste_dois_card = document.createElement('div');
            divteste_dois_card.className = "card";
            imagem_card = document.createElement('img');
            imagem_card.className = "card-img-top";
            imagem_card.setAttribute("src", "um.png");
            divteste_tres = document.createElement("div");
            divteste_tres.className = "card-body";
            texto = document.createElement('h5')
            texto.className = "card-title";
            texto.innerHTML = imageRef.name;
            botao_card = document.createElement('button');
            botao_card.className = "btn btn-outline-success";
            botao_card.innerHTML="Analisar";
            botao_card.onclick = function() {
                
                console.log(imageRef.name);
                document.getElementById("filename_dois").value = imageRef.name;
            }
            divteste_tres.appendChild(imagem_card);
            divteste_tres.appendChild(texto);
            divteste_tres.appendChild(botao_card);
            divteste_dois_card.appendChild(divteste_tres);
            divteste_dois.appendChild(divteste_dois_card);
            divteste.appendChild(divteste_dois);

        });
  });




}
/*
function analise(){
    var escolha = document.getElementById("selecao").value;
    console.log(escolha);
    document.getElementById("filename").value = escolha;

}*/