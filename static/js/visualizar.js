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
            imagem_card.setAttribute("src", "/static/um.PNG");
            divteste_tres = document.createElement("div");
            divteste_tres.className = "card-body";
            texto = document.createElement('h5')
            texto.className = "card-title";
            texto.innerHTML = imageRef.name;
            var select_mes = document.createElement("select");
            select_mes.name = "select_mes";
            select_mes.className = 'form-select form-select-lg mb-3';
            let lista_mes=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
            let lista_numero=["1","2","3","4","5","6","7","8","9","10","11","12"]
            for (var i = 0; i < lista_mes.length; i++) {
                var option = document.createElement("option");
                option.value = lista_numero[i];
                option.text = lista_mes[i];
                select_mes.appendChild(option);
            }
            botao_card = document.createElement('button');
            botao_card.className = "btn btn-outline-success btn-lg";
            botao_card.innerHTML="Ver Tabela";
            botao_card.onclick = function() {
                
                console.log(imageRef.name);
                document.getElementById("filename_dois").value = imageRef.name;

            }

            var escolha_mes = document.createElement('h4');
            escolha_mes.innerHTML =  "Escolha o Mês de Análise";
            escolha_mes.className = "display-4";
            var br = document.createElement('br');

            divteste_tres.appendChild(imagem_card);
            divteste_tres.appendChild(texto);
            divteste_tres.appendChild(br);
            divteste_tres.appendChild(br);
            divteste_tres.appendChild(escolha_mes);
            divteste_tres.appendChild(select_mes);
            divteste_tres.appendChild(br);
            divteste_tres.appendChild(br);
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