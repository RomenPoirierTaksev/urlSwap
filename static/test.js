let button = document.getElementById('go-button');

function doSomething(){
    let url = document.getElementById('url').value;
    fetch('/hello', {

        // Declare what type of data we're sending
        headers: {
          'Content-Type': 'application/json'
        },
    
        // Specify the method
        method: 'POST',
    
        // A JSON payload
        body: JSON.stringify(
            url
        )
    }).then(function (response) { // At this point, Flask has printed our JSON
        if(response.status == 500){
            return response.status;
        }
        return response.text();
    }).then(function (text) {
        if(text == 500){
            document.getElementById("output").innerHTML = "Unable to find song";
        }else{
            if(text == "Invalid URL"){
                document.getElementById("output").innerHTML = text;
            }else{
                document.getElementById("output").innerHTML = "New URL: " + text;
            }
            
            
        }
    });
}

button.addEventListener("click", doSomething);